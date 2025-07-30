import logging
import os
import json
import time
import boto3
import LLM.tune as tune
import re


class LLMService():
    def __init__(self, args):
        logging.info('Initializing LLM Service...')

        self.counter = 0
        self.brainwash = args.brainwash
        self.tune = tune.get_tune(args.character)

        self.client = boto3.client("bedrock-runtime", region_name="us-west-2")
        self.model_id = "anthropic.claude-3-5-sonnet-20241022-v2:0"
        # self.model_id = "anthropic.claude-3-5-haiku-20241022-v1:0"
        
    def get_prompt(self, text):
        prompt = json.dumps({
            "system": self.tune,
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 2048,
            "temperature": 1,
            "messages": [
                {
                    "role": "user",
                    "content": [{"type": "text", "text": text}],
                }
            ],
        })

        return prompt

    def ask(self, text):
        stime = time.time()

        body = self.get_prompt(text)

        response = self.client.invoke_model(
            body=body,
            modelId=self.model_id,
            accept="application/json",
            contentType="application/json",
        )

        response_body = json.loads(response.get('body').read())

        prev_text = response_body['content'][0]['text']
        new_text = self.remove_paragraphs_and_newlines(prev_text)

        logging.info('LLM Response: %s, time used %.2f' % (new_text, time.time() - stime))
        return new_text
    

    def ask_stream(self, text):
        prev_text = ""
        complete_text = ""
        stime = time.time()
        if self.counter % 5 == 0:
            if self.brainwash:
                logging.info('Brainwash mode activated, reinforce the tune.')
            else:
                logging.info('Injecting tunes')
            asktext = self.tune + '\n' + text
        else:
            asktext = text
        self.counter += 1

        body = self.get_prompt(asktext)
        
        response = self.client.invoke_model_with_response_stream(
            body=body,
            modelId=self.model_id,
            accept="application/json",
            contentType="application/json",
        )

        stream = response["body"]

        for event in stream:
            chunk = event.get("chunk")
            if chunk:
                data = json.loads(chunk.get("bytes").decode())
                message = data.get("delta", {}).get("text", "")
                if ("。" in message or "！" in message or "？" in message or "\n" in message) and len(complete_text) > 3:
                    complete_text += message
                    logging.info('LLM Stream Response: %s, @Time %.2f' % (complete_text, time.time() - stime))
                    yield complete_text.strip()
                    complete_text = ""
                else:
                    complete_text += message

                prev_text += message

        if complete_text.strip():
            logging.info('LLM Stream Response: %s, @Time %.2f' % (complete_text, time.time() - stime))
            yield complete_text.strip()

    
    def replace_english_punctuation(self, text):
        # 定义英文标点与中文标点的映射
        punctuation_map = {
            ',': '，',
            '.': '。',
            '!': '。',
            '?': '？',
            ':': '：',
            ';': '；',
            '"': '“',
            "'": '’',
            '(': '（',
            ')': '）',
            '-': '—',
            '~': '～'
        }
        
        # 使用正则表达式替换英文标点为中文标点
        for eng_punc, zh_punc in punctuation_map.items():
            text = re.sub(re.escape(eng_punc), zh_punc, text)
        
        return text
    
    def remove_paragraphs_and_newlines(self, text):
        return ' '.join(text.split())
