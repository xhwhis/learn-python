#!/usr/bin/env python
# coding=utf-8
from urllib import request
from bs4 import BeautifulSoup

def load_page(url):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    headers = {'User_Agent': user_agent}
    req = request.Request(url, headers = headers)
    response = request.urlopen(req)
    return response.read()

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    bs = BeautifulSoup(load_page(url), 'html.parser')
    ans = bs.find('a', attrs = {'id' : 'jgwab'}).text
    print(ans)
