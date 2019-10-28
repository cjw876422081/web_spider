#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

EMAIL = "test@test.com"
PASSWORD = "123456"

class CrackGeetest():
    def __init__(self):
        self.url = 'http://account.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser  ,20)