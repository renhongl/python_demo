

import requests
from bs4 import BeautifulSoup
import json

def get_one_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    question = soup.select('.question-summary h3 a')
    vote = soup.select('.vote-count-post')
    results = []
    for i in range(len(question)):
        temp = {
            'question': question[i].string,
            'vote': vote[i].string
        }
        results.append(temp)

    return results


def write_to_json(data):
    with open('./output/bs_test.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)

def main():
    url = 'https://stackoverflow.com/search?q=react+leaflet'
    data = get_one_page(url)
    write_to_json(data)
    print('finished')

main()
