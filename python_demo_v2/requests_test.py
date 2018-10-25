

import requests
import re

def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    rank = re.findall('<i class="board-index.*?>(.*?)</i>', res.text)
    return rank

    

def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)


main()