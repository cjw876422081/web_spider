#-*-coding:utf-8-*-

from selenium import  webdriver

import  time
brower = webdriver.Chrome()
brower.get('https://www.taobao.com')
input = brower.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(2)
input.clear()
input.send_keys('iPad')
button = brower.find_element_by_class_name('btn-search')
button.click()