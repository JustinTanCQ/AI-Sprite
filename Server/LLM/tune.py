import logging
import os

def get_tune(character):
    filename = character+'.txt'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'charactor-prompt', filename)
    logging.info('load charactor prompt: %s' % filename)
    return open(file_path, 'r', encoding='utf-8').read()


exceed_reply = """
你问的太多了，有问题慢慢问。
"""

error_reply = """
你等一下，我连接不上大脑了。你的网络是不是有问题？
"""