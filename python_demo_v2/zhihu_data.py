

import requests
from pyquery import PyQuery as pq
import json



def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    text = res.text
    doc = pq(text)
    results = []
    for item in doc.find('.explore-feed.feed-item').items():
        temp = {
            'title': item.find('h2').text(),
            'anwser': item.find('.zh-summary.summary').text(),
            'author': item.find('.author-link-line').text()
        }
        results.append(temp)
    return results


def write_to_txt(results):
    for item in results:
        with open('./output/zhihu_data.txt', 'a', encoding='utf-8') as f:
            print(item)
            question = ''
            question = question + item['title'] + '\n'
            question = question + item['anwser'] + '\n'
            question = question + item['author'] + '\n'
            question = question + '========\n'
            f.write(question)

def write_to_json(results):
    with open('./output/zhihu_data.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(results, indent=4, ensure_ascii=False))


def main():
    url = 'https://www.zhihu.com/explore'
    results = get_one_page(url)
    # write_to_txt(results)
    write_to_json(results)
    print(results)

main()