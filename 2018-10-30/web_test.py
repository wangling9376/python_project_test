#Author:Wl
# coding = uft-8
import os,time
import _thread
from selenium import webdriver

chromedriver_path = "/usr/local/bin/chromedriver"
url = 'https://www.baidu.com'
url_2 = 'https://www.alipay.com/'
def open_url(threadName, delay):
    count = 0
    while (count < 5):
        driver = webdriver.Chrome(chromedriver_path)
        # driver.maximize_window() # 最大化浏览器
        driver.implicitly_wait(8)  # 设置隐式时间等待
        driver.get(url)
        driver.find_element_by_name("wd").send_keys("python")
        driver.find_element_by_id("su").click()
        # time.sleep(10)
        # driver.quit()
        count = count + 1

def open_url_2(threadName, delay):
    count_1 = 0
    while (count_1 < 5):
        count_1 = count_1 + 1
        driver = webdriver.Chrome(chromedriver_path)
        # driver.maximize_window() # 最大化浏览器
        driver.implicitly_wait(8)  # 设置隐式时间等待
        driver.get(url)
        driver.find_element_by_name("wd").send_keys("支付宝")
        driver.find_element_by_id("su").click()
        # time.sleep(10)
        #driver.quit()

try:
    _thread.start_new_thread(open_url, ("Thread-1", 2,))
    _thread.start_new_thread(open_url_2, ("Thread-2", 4,))
except:
    print("Error")

while 1:
    pass
