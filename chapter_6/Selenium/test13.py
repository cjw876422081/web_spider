#-*-coding:utf-8-*-

import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
browser.execute_script("window.open()")
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
browser.execute_script("window.close()")
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://www.zhihu.com')
