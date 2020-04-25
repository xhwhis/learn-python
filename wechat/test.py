#!/usr/bin/env python
# coding=utf-8
import requests
import itchat

def get_response(msg):
    api_url = 'http://openapi.tuling123.com/openapi/api'
    data = {
        'info': msg,
        'api_key': 'a271387d60054e30ab399ea83fab9e88',
    }
    r = requests.post(api_url, data=data).json()
    print(r.get('text'))
    return r

def text_reply(msg):
    return get_response(msg["Text"])["text"]

if __name__ == '__main__':
    itchat.auto_login(True)
    itchat.run()
