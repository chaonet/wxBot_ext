#!/usr/bin/env python
# coding: utf-8

from wxbot import *

class Emotion_api(WXBot):

    def handle_msg_all(self, msg):





def main():
    bot = Emotion_api()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()