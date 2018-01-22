

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

index = 0
browser = None
links = None

def get_mark():
    global index
    global links
    browser.get(links[index].get_attribute('href'))
    links = browser.find_elements_by_css_selector('.emoji_box_5wc42 a')
    marks = browser.find_elements_by_css_selector('.unicode')
    html_codes = ''
    css_codes = ''
    for mark in marks:
        title = mark.get_attribute('title').split(': ')[1].lower().replace(' ', '-')
        code = mark.get_attribute('title').split(': ')[0].replace('U+', '\\')
        html_codes = html_codes + '<i class="mr-icon mr-'+title+'"></i>\n'
        css_codes = css_codes + '.mr-' + title + '::before{content:"' + code + '";}\n'

    with open('./output/newIcon2/icon_html.txt', 'a', encoding='utf-8') as icon_html:
        icon_html.write(html_codes)

    with open('./output/newIcon2/icon_css.txt', 'a', encoding='utf-8') as icon_css:
        icon_css.write(css_codes)

    print(links[index].get_attribute('href') + '获取成功')
        
    
    if index < len(links) - 1:
        index = index + 1
        get_mark()



def run():
    global browser
    global links
    show_browser = True
    chrome_options = webdriver.ChromeOptions()

    if show_browser:
        browser = webdriver.Chrome()
    else:
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(chrome_options=chrome_options)

    # try:
    browser.get('http://xahlee.info/comp/unicode_index.html')
    links = browser.find_elements_by_css_selector('.emoji_box_5wc42 a')
    get_mark()
        

    # except Exception as e:
    #     print(e)
    # finally:
    #     browser.close()


if __name__ == '__main__':
    run()