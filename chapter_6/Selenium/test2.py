#-*-coding:utf-8-*-
from selenium import webdriver
#声明浏览器对象
browser = webdriver.Chrome()

# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# browser = webdriver.PhantomJS()
# browser = webdriver.Safari()

#访问页面
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')

print(input_first , input_second , input_third)
browser.close()