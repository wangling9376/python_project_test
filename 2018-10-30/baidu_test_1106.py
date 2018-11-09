# chrom derierhttps://npm.taobao.org/mirrors/chromedriver/70.0.3538.67/
# coding:utf-8
from selenium import webdriver
import time
import os

# import thread
chrome_path = "/usr/local/bin/chromedriver"
url = "https://www.baidu.com"
url_1 = "http://test.gs-robot.com/#/analysis"
#from macos chrome
#deiver = webdriver.Chrome(chrome_path)
# chrome start of windows
deiver = webdriver.Chrome()
deiver.implicitly_wait(8)
deiver.get(url_1)
#deiver.find_element_by_name("wd").send_keys("python")
deiver.find_element_by_id("email").send_keys("zy@gs-robot.com")
deiver.find_element_by_id("password").send_keys("1")
#deiver.find_element_by_id("su").click()
deiver.find_element_by_css_selector("[type='submit']").click()
# time.sleep(5)
# deiver.quit()
