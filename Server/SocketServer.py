import argparse
import asyncio
import websockets
import logging
import traceback
import base64
import json
import re
import numpy as np

import librosa
import requests
import soundfile

from utils.FlushingFileHandler import FlushingFileHandler
from ASR import ASRService
from LLM import LLMService
from TTS import GPTSoVitsService
from SentimentEngine import SentimentEngine

console_logger = logging.getLogger()
console_logger.setLevel(logging.INFO)
FORMAT = '%(asctime)s %(levelname)s %(message)s'
console_handler = console_logger.handlers[0]
console_handler.setFormatter(logging.Formatter(FORMAT))
console_logger.setLevel(logging.INFO)
file_handler = FlushingFileHandler("log.log", formatter=logging.Formatter(FORMAT))
file_handler.setFormatter(logging.Formatter(FORMAT))
file_handler.setLevel(logging.INFO)
console_logger.addHandler(file_handler)
console_logger.addHandler(console_handler)


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Unsupported value encountered.')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--proxy", type=str, nargs='?', required=False)
    parser.add_argument("--stream", type=str2bool, nargs='?', required=True)
    parser.add_argument("--character", type=str, nargs='?', required=True)
    parser.add_argument("--ip", type=str, nargs='?', required=False)
    parser.add_argument("--brainwash", type=str2bool, nargs='?', required=False)
    return parser.parse_args()

def remove_asterisk_content(text):
    # This regex pattern will match anything between asterisks, including the asterisks themselves.
    return re.sub(r'\*.*?\*', '', text)

class Server():
    def __init__(self, args):
        self.args = args
        self.tmp_recv_file = 'tmp/server_received.wav'
        self.tmp_proc_file = 'tmp/server_processed.wav'

        ## hard coded character map
        self.char_name = {
            'paimon': ['TTS/models/paimon6k.json', 'TTS/models/paimon6k_390k.pth', 'character_paimon', 1],
            'yunfei': ['TTS/models/yunfeimix2.json', 'TTS/models/yunfeimix2_53k.pth', 'character_yunfei', 1.1],
            'catmaid': ['TTS/models/catmix.json', 'TTS/models/catmix_107k.pth', 'character_catmaid', 1.2],
            'zhongli': ['TTS/models/zhongli.json', 'TTS/models/zhongli_44k.pth', 'character_zhongli', 1],
            'nahida': ['TTS/models/nahida.json', 'TTS/models/nahida_129k.pth', 'character_nahida', 1.1],
            'aorun': ['TTS/models/nahida.json', 'TTS/models/nahida_129k.pth', 'character_aorun', 1.0]
        }

        # PARAFORMER
        self.paraformer = ASRService.ASRService('./ASR/resources/config.yaml')
        # LLM
        # self.chat_gpt = GPTService.GPTService(args)
        self.claude = LLMService.LLMService(args)
        # TTS
        # self.tts = TTService.TTService(*self.char_name[args.character])
        self.tts = GPTSoVitsService.GPTSoVitsService()
        # Sentiment Engine
        self.sentiment = SentimentEngine('SentimentEngine/models/sentiment.onnx')

    async def handle_connection(self, websocket, path):
        try:
            incoming_file = await websocket.recv()
            file_data = b''  # Binary data of the file
            file_data += incoming_file  # Concatenate all binary data
            # Save the received audio file
            with open('tmp/server_received.wav', 'wb') as f:
                f.write(file_data)
                logging.info('WAV file received and saved.')
            ask_text = self.process_voice()
            if self.args.stream:
                for sentence in self.claude.ask_stream(ask_text):
                    await self.send_voice(websocket, sentence)
            else:
                resp_text = self.claude.ask(ask_text)
                await self.send_voice(websocket, resp_text)
        except Exception as e:
            logging.error(traceback.format_exc())
            await websocket.send("Error processing the request")


    async def send_voice(self, websocket, resp_text):
        # self.tts.read_save(resp_text, 'tmp/server_processed.wav', self.tts.hps.data.sampling_rate)
        final_text = remove_asterisk_content(resp_text)
        self.tts.read_save(final_text, 'tmp/server_processed.wav')
        with open('tmp/server_processed.wav', 'rb') as f:
            audio_data = f.read()
        # sentiment_score = self.sentiment.infer(resp_text)
        sentiment_score = 0
        # if isinstance(sentiment_score, np.integer):
        #     sentiment_score = int(sentiment_score)
        response = {
            'audio': base64.b64encode(audio_data).decode('utf-8'),
            'text': resp_text,
            'sentiment': sentiment_score
        }
        await websocket.send(json.dumps(response))

    def process_voice(self):
        # stereo to mono
        y, sr = librosa.load(self.tmp_recv_file, sr=None, mono=False)
        y_mono = librosa.to_mono(y)
        y_mono = librosa.resample(y_mono, orig_sr=sr, target_sr=16000)
        soundfile.write(self.tmp_recv_file, y_mono, 16000)
        text = self.paraformer.infer(self.tmp_recv_file)

        return text


if __name__ == '__main__':
    try:
        args = parse_args()
        server = Server(args)
        start_server = websockets.serve(server.handle_connection, "0.0.0.0", 8765)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    except Exception as e:
        logging.error(e.__str__())
        logging.error(traceback.format_exc())
        raise e
