

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time
import pymongo

songs = ['追光者']
current = 0
total_page = 100
current_page = 1
show_browser = False
save_to_db = False

def save_to_db(comment):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.wangyi
    collection = db.comments
    collection.insert_one(comment)

def search_by_page(browser, song):
    global total_page
    global current_page
    print('搜索歌曲: <' + song + '>第' + str(current_page) + '页')
    items = browser.find_elements_by_css_selector('.cnt.f-brk')
    with open('../output/wangyi/' + song + '.txt', 'a', encoding='utf-8') as comment_file:
        lines = ''
        for item in items:
            arr = str.split(item.text, '：')
            comment = {
                'song': song,
                'name': arr[0],
                'comment': arr[1]
            }
            save_to_db(comment)
            lines = lines + item.text + '\n\n'
        comment_file.write(lines)
        
    print('搜索结束')
    if(current_page < total_page):
        current_page = current_page + 1
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        next_btn = browser.find_element_by_class_name('znxt')
        ActionChains(browser).move_to_element(next_btn).click().perform()
        time.sleep(3)
        search_by_page(browser, song)

def search_by_song(song):
    global songs
    global current
    global current_page
    global show_browser
    current_page = 1
    if show_browser:
        browser = webdriver.Chrome()
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(chrome_options=chrome_options)
        # browser = webdriver.PhantomJS()
        
    try:
        browser.maximize_window()
        browser.implicitly_wait(10)
        browser.get('http://music.163.com/#/search/m/')
        browser.switch_to_frame('g_iframe')
        input = browser.find_element_by_css_selector('#m-search-input')
        input.send_keys(song)
        input.send_keys(Keys.ENTER)

        items = browser.find_elements_by_css_selector('.text a')
        for item in items:
            if(item.text == songs[current]):
                item.click()
                time.sleep(3)
                search_by_page(browser, song)
                break

    finally:
        browser.close()
        time.sleep(3)
        if(current < len(songs) - 1):
            current = current + 1
            search_by_song(songs[current])



if __name__ == '__main__':
    search_by_song(songs[current])












