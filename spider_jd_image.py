
import requests
import re
from bs4 import BeautifulSoup

total_page = 3
current_page = 1

def parse_by_re(html):
    img_pat = '//.+?.jpg'
    result = re.compile(img_pat).findall(html)
    print(result)

def parse_by_bs4(html):
    global current_page
    global total_page
    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup.select('#plist img')
    i = 0
    for img in imgs:
        if (img.get('data-lazy-img')): 
            img_url = 'http:' + img.get('data-lazy-img')
            save_img(img_url, i)
            i = i + 1

    if (current_page < total_page):
        current_page = current_page + 1
        main()

def save_img(url, i):
    global current_page
    print('save: ' + url)
    img_data = requests.get(url).content
    with open('./output/jd/page'+ str(current_page)+'-'+ str(i) + '.jpg', 'wb') as img:
        img.write(img_data)


def main():
    global current_page
    root_url = 'https://coll.jd.com/list.html?sub=22575&page='+str(current_page)+'&JL=6_0_0'
    response = requests.get(root_url)
    html = response.text
    # parse_by_re(html)
    parse_by_bs4(html)

if __name__ == '__main__':
    main()