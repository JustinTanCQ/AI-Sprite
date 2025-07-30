from LLM import LLMService
import argparse
import logging

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Unsupported value encountered.')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stream", type=str2bool, nargs='?', required=True)
    parser.add_argument("--character", type=str, nargs='?', required=True)
    parser.add_argument("--brainwash", type=str2bool, nargs='?', required=False)
    return parser.parse_args()


if __name__ == '__main__':
    try:
        args = parse_args()
        llm = LLMService.LLMService(args)
        text = '作为一位成功的商人，您有没有什么关于管理时间和高效工作的建议可以分享？'
        if args.stream: 
          resp_text = llm.ask_stream(text)
          for text in resp_text:
            print(text)
        else:
            resp_text = llm.ask(text)
            print(resp_text)
    except Exception as e:
        logging.error(e.__str__())
        raise e

