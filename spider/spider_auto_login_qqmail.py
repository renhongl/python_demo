
import time
import win32api
import win32con
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


ROOT_URL = 'https://en.mail.qq.com/cgi-bin/loginpage'

def read(url, mail, pwd):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(url)
    time.sleep(3)
    browser.switch_to_frame('login_frame')
    mail_input = browser.find_element_by_id('u')
    mail_input.send_keys(mail)
    pwd_input = browser.find_element_by_id('p')
    pwd_input.send_keys(pwd)
    login_button = browser.find_element_by_id('login_button')
    login_button.send_keys(Keys.ENTER)
    time.sleep(5)
    try:
        browser.switch_to_frame('mainFrame')
        new_mails = browser.find_elements_by_class_name('Ru')
        if len(new_mails) > 0:
            print('您有' + str(len(new_mails)) + '封新邮件')
            win32api.MessageBox(0, '您有' + str(len(new_mails)) + '封新邮件', "邮件提醒")  

        time.sleep(60)
        read(url, mail, pwd)
    except Exception as e:
        print('登录失败')


if __name__ == '__main__':
    read(ROOT_URL, '1075220132', '11')
        

