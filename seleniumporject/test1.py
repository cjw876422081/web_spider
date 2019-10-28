#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib.parse import quote
browser = webdriver.Chrome()
wait = WebDriverWait(browser ,10 )
KEYWORD = "ipad"


def index_page(page):
    print("爬取"+page+"页")
    try:
        url = "https://s.taobao.com/search?q="+quote(KEYWORD)
        if page > 1 :
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')),
    submit = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit'))),)
    except:
        pass