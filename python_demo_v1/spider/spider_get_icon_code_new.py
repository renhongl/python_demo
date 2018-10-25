

from selenium import webdriver
import time
import json
from bs4 import BeautifulSoup


urls = [
    'https://unicode-table.com/en/sets/emoji/',
    'https://unicode-table.com/en/sets/arrows-symbols/',
    'https://unicode-table.com/en/sets/hearts-symbols/',
    'https://unicode-table.com/en/sets/flowers-symbols/',
    'https://unicode-table.com/en/sets/stars-symbols/'
]

def run(i):
    global urls
    show_browser = False
    chrome_options = webdriver.ChromeOptions()

    if show_browser:
        browser = webdriver.Chrome()
    else:
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(chrome_options=chrome_options)

    try:
        browser.get(urls[i])
        time.sleep(3)
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        titles = soup.select('.stitle')
        codes = soup.select('.code')
        html_codes = ''
        css_codes = ''
        for i in range(len(titles)):
            title = titles[i].text.lower().replace(' ', '-')
            code = codes[i].text.replace('U+', '\\')
            html_code = '<i class="mr-icon mr-'+title+'"></i>\n'
            css_code = '.mr-' + title + '::before{content:"' + code + '";}\n'
            html_codes = html_codes + html_code
            css_codes = css_codes + css_code
        with open('../output/newIcon/icon_html.txt', 'a', encoding='utf-8') as icon_html:
            icon_html.write(html_codes)

        with open('../output/newIcon/icon_css.txt', 'a', encoding='utf-8') as icon_css:
            icon_css.write(css_codes)

        print('Save finish')

    except Exception as e:
        print(e)
    finally:
        browser.close()


if __name__ == '__main__':
    for i in range(len(urls)):
        run(i)