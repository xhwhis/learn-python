#!/usr/bin/env python
# coding=utf-8
from selenium import webdriver

dirver = webdriver.Chrome()
url = 'https://passport.jisuanke.com/?n=https://www.jisuanke.com/#/'
driver.get(url)
name_input = driver.find_element_by_xpath('//*[@id='entry-panel']/div/div[1]/div/div/div[1]/input')
name_input.send_keys('13125141400')
passwd_input = driver.find_element_by_xpath('//*[@id='entry-panel']/div/div[1]/div/div/div[2]/input')
passwd_input.send_keys('hahaha597')
login = driver.find_element_by_xpath('//*[@id='entry-panel']/div/div[1]/div/div/a')
login.click()
