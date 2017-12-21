"""Simple spider for get links from website"""

import requests
from bs4 import BeautifulSoup

def get_link(url, file_name):
    """Get link function"""
    header_infor = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    headers = {'User-Agent': header_infor}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    with open('./output/'+file_name+'.txt', 'a', encoding='utf-8') as simple_spider_data:
        for link in soup.find_all('a'):
            if link.find('h4'):
                name = link.find('h4').string
                uri = 'http:' + link.get('href')
                # print(name + ': ' + uri)
                simple_spider_data.write(name + ': ' + uri + '\n')
            elif link.find('span'):
                name = link.find('span').string
                uri = link.get('href')
                # print(name + ': ' + uri)
                simple_spider_data.write(name + ': ' + uri + '\n')

if __name__ == '__main__':
    runoob_url = 'http://www.runoob.com/'
    get_link(runoob_url, 'runoob')

    douban_movie = 'https://movie.douban.com/tag/%E7%88%B1%E6%83%85'
    get_link(douban_movie, 'douban_movie')