
import requests
from pyquery import PyQuery as pq
import json


def get_one_page(url):
    res = requests.get(url)
    doc = pq(res.text)
    summary = doc.find('.question-summary')
    results = []
    for item in summary.items():
        question = item.find('h3 a')
        asked = item.find('.started')
        if question != None and asked != None:
            temp = {
                'question': question.text(),
                'asked': asked.text()
            }
            results.append(temp)
    return results

def write_to_json(data):
    with open('./output/pyquery_test.json', 'w') as f:
        json.dump(data, f)

def main():
    url = 'https://stackoverflow.com/search?q=react+leaflet'
    html = get_one_page(url)
    write_to_json(html)
    print('finished')

main()