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

def write_to_file(file_name, soup_text):
    f = open(file_name, 'w')
    for line in soup_text.find_all('p'):
        f.write(line.text)
        f.write('\n')
    f.close()

def book_spider(url, chapter):
    html = load_page(url)
    bs = BeautifulSoup(html, 'html.parser')
    chapter_name = bs.find('h1').text
    print(chapter_name)
    soup_text = bs.find('div', class_ = 'chapter_content')
    file_name = str(chapter) + '.%s.txt' % chapter_name
    write_to_file(file_name, soup_text)

if __name__ == '__main__':
    url = 'http://www.shicimingju.com/book/sanguoyanyi/'
    for chapter in range(1, 121):
        chapter_url = url + str(chapter) + '.html'
        book_spider(chapter_url, chapter)
