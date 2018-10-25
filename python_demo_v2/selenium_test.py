

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)


def baidu_test():
    try:
        browser.get('https://www.baidu.com')
        input = browser.find_element_by_id('kw')
        input.send_keys('python')
        input.send_keys(Keys.ENTER)
        time.sleep(10)


    finally:
        browser.close()
        

baidu_test()