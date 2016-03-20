#!/usr/bin/env python
# coding: utf-8

import os
import httplib, urllib, base64
from wxbot import *

class Emotion_api(WXBot):
    
    def __init__(self):
        WXBot.__init__(self)
        self.emotion_key = os.environ.get("emotion_key") or 'NULL'
        self.robot_switch = False
    
    def emotion_api(self, uid, url):
        return url

    def auto_switch(self, msg):
        msg_data = msg['content']['data']
        stop_cmd = [u'退下', u'走开', u'关闭', u'关掉', u'休息', u'滚开']
        start_cmd = [u'出来', u'启动', u'工作']
        if self.robot_switch:
            if msg_data in stop_cmd:
                self.robot_switch = False
                self.send_msg_by_uid(u'[Robot]' + u'机器人已停止判断情绪！', msg['to_user_id'])
                # self.send_msg_by_uid(u'[Robot]' + u'机器人已停止判断情绪！', msg['FromUserName'])
        else:
            if msg_data in start_cmd:
                self.robot_switch = True
                self.send_msg_by_uid(u'[Robot]' + u'机器人已开始判断情绪！', msg['to_user_id'])
                # self.send_msg_by_uid(u'[Robot]' + u'机器人已开始判断情绪！', msg['FromUserName'])

    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 1:
            return
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            self.auto_switch(msg)
        elif msg['msg_type_id'] == 3 and msg['content']['type'] == 0:
            if 'detail' in msg['content']:
                
                my_names = self.get_group_member_name(self.my_account['UserName'], msg['user']['id'])
                if my_names is None:
                    my_names = {}
                if 'NickName' in self.my_account and self.my_account['NickName']:
                    my_names['nickname2'] = self.my_account['NickName']
                if 'RemarkName' in self.my_account and self.my_account['RemarkName']:
                    my_names['remark_name2'] = self.my_account['RemarkName']

                is_at_me = False
                for detail in msg['content']['detail']:
                    if detail['type'] == 'at':
                        for k in my_names:
                            if my_names[k] and my_names[k] == detail['value']:
                                is_at_me = True
                                break
                if is_at_me:
                    self.auto_switch(msg)

        if self.robot_switch and msg['content']['type'] == 3:
            if msg['msg_type_id'] == 4:
                self.send_msg_by_uid(self.emotion_api(msg['user']['id'], msg['content']['data']), msg['user']['id'])
            elif msg['msg_type_id'] == 3:
                self.send_msg_by_uid(self.emotion_api(msg['content']['user']['id'], msg['content']['desc']), msg['user']['id'])

def main():
    bot = Emotion_api()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()

if __name__ == '__main__':
    main()