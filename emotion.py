#!/usr/bin/env python
# coding: utf-8

import os,json
import httplib, urllib, base64
import requests
from wxbot import *

import ConfigParser


class Emotion_api(WXBot):
    
    def __init__(self):
        WXBot.__init__(self)
        if os.path.exists('conf.ini'):
            cf = ConfigParser.ConfigParser()
            cf.read('conf.ini')
            self.emotion_key = cf.get('main', 'emotion_key')
        else:
            self.emotion_key = os.environ.get("emotion_key") or 'NULL'
        self.robot_switch = False
        print self.emotion_key

        self.headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': self.emotion_key ,
        }

        self.emotion_max = ''
    
    def emotion_api(self, uid, url, msg_id):
        if self.emotion_key == 'NULL':
            return
        print msg_id

        fn = 'img_' + msg_id + '.jpg'

        print fn
        b = open(fn, 'rb')
        print b

        try:
            conn = httplib.HTTPSConnection('api.projectoxford.ai')
            conn.request("POST", "/emotion/v1.0/recognize", b, self.headers)
            response = conn.getresponse()
            data = response.read()

            data = json.loads(data)

            emotion_list = [u'sadness', u'neutral', u'contempt', u'disgust', u'anger', u'surprise', u'fear', u'happiness']
            
            max_value = 0
            for i in emotion_list:
                if data[0]['scores'][i] > max_value:
                    self.emotion_max = i
                    max_value = data[0]['scores'][i]

            conn.close()
        except Exception as e:
            print 2
            print e
        emotion_dir = {u'sadness': u'很悲伤', u'neutral': u'不动声色', u'contempt': u'轻蔑', u'disgust': u'厌恶', u'anger': u'生气', u'surprise': u'惊讶', u'fear': u'害怕', u'happiness': u'开心'}
        return emotion_dir[self.emotion_max]

    def auto_switch(self, msg):
        msg_data = msg['content']['data']
        stop_cmd = [u'退下', u'走开', u'关闭', u'关掉', u'休息', u'滚开']
        start_cmd = [u'出来', u'启动', u'工作']
        if self.robot_switch:
            if msg_data in stop_cmd:
                self.robot_switch = False
                self.send_msg_by_uid(u'[Robot]' + u'机器人已停止判断情绪！', msg['to_user_id'])

                self.send_msg_by_uid(u'[Robot]' + u'机器人已停止判断情绪！', msg['user']['id'])
        else:
            if msg_data in start_cmd:
                self.robot_switch = True
                self.send_msg_by_uid(u'[Robot]' + u'机器人已开始判断情绪！', msg['to_user_id'])
 
                self.send_msg_by_uid(u'[Robot]' + u'机器人已开始判断情绪！', msg['user']['id'])

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
                self.send_msg_by_uid(self.emotion_api(msg['user']['id'], msg['content']['data'], msg['msg_id']), msg['user']['id'])
            elif msg['msg_type_id'] == 3:
                self.send_msg_by_uid(self.emotion_api(msg['content']['user']['id'], msg['content']['desc'], msg['msg_id']), msg['user']['id'])

def main():
    bot = Emotion_api()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()

if __name__ == '__main__':
    main()