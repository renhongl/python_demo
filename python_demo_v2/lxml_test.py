

import requests
from lxml import etree

def get_one_page(url):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'cookie': 'prov=75cc3cab-0ed5-5eb2-d18c-b312a24350db; _ga=GA1.2.1662857097.1537756289; __qca=P0-1944747911-1537756288975; __gads=ID=07b4138067dfdc8b:T=1537756486:S=ALNI_MZZ_k0v-XqE5eG_swFphVY1MMMqpQ; hero-dismissed=1537756342543!stk_a; _gid=GA1.2.968380875.1539586485'
        }
        res = requests.get(url, headers=headers)
        
        if res.status_code != 200:
            return res.status_code

        else:
            html = etree.parse(res.text, etree.HTMLParser())
            results = html.xpath('//a/@href')
            return results

    except Exception as e:
        return e

def main():
    url = 'https://stackoverflow.com/questions/tagged/react-leaflet'
    html = get_one_page(url)
    print(html)


main();