#!/usr/bin/env python
# coding=utf-8
import itchat
import requests

def get_response(msg):
    api_url = 'http://i.itpk.cn/api.php'
    data={
        "question": msg,
        "api_key": "4ecbd7ce1362f67fe365fc8e37f27626",
        "api_secret": "hahaha597"
    }
    r=requests.post(api_url,data=data)
    return r.text

def print_content(msg):
    return get_response(msg['Text'])

itchat.auto_login(True)
itchat.run()
