#-*-coding:utf-8-*-
import time

from selenium import  webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
def get_info(qq , add ):
    print(qq)
    browser.get("https://user.qzone.qq.com/{}".format(qq))
    # time.sleep(3)
    try:
        browser.find_elements_by_id("loginform")
        login_sign = True
    except :
        login_sign = False
    if login_sign == True :
        browser.switch_to.frame('login_frame')
        choose = browser.find_elements_by_id("switcher_plogin")
        choose = choose[0]
        choose.click()
        browser.find_elements_by_id('u')[0].clear()
        browser.find_elements_by_id('u')[0].send_keys("876422081")
        browser.find_elements_by_id('p')[0].clear()
        browser.find_elements_by_id('p')[0].send_keys('cjw271118')
        browser.find_elements_by_id('login_button')[0].click()
        time.sleep(6)
        do_first = browser.find_elements_by_class_name("btn-fs-sure")
        do_first[0].click()
        browser.find_elements_by_css_selector("#menuContainer > div > ul > li.menu_item_311 > a")[0].click()

        # browser.switch_to.frame('app_canvas_frame')

        # Images = browser.find_elements_by_class_name("img-attachments-inner clearfix")
        # for image in  Images:
        #     print(image)





if __name__ == '__main__':

    get_info(int("175083909") ,"test1.text" )
