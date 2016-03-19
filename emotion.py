#!/usr/bin/env python
# coding: utf-8

import os
import httplib, urllib, base64
from wxbot import *

class Emotion_api(WXBot):
    
    def __init__(self):
        WXBot.__init__(self)
        emotion_key = os.environ.get("emotion_key") or 'NULL'
    
    def emotion_api(url):
        pass

    def auto_switch(self, msg):
        msg_data = msg['content']['data']
        stop_cmd = [u'退下', u'走开', u'关闭', u'关掉', u'休息', u'滚开']
        start_cmd = [u'出来', u'启动', u'工作']
        if self.robot_switch:
            if msg_data in stop_cmd:
                self.robot_switch = False
                self.send_msg_by_uid(u'[Robot]' + u'机器人已停止判断情绪！', msg['to_user_id'])
        else:
            if msg_data in start_cmd:
                self.robot_switch = True
                self.send_msg_by_uid(u'[Robot]' + u'机器人已开始判断情绪！', msg['to_user_id'])

    def handle_msg_all(self, msg):
        pass

def main():
    bot = Emotion_api()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()

if __name__ == '__main__':
    main()