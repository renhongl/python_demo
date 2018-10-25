

from selenium import webdriver
import threading
import queue
import time
import requests
import json
import pymongo

song_hash_queue = queue.Queue()
ROOT_URL = 'http://www.kugou.com/yy/special/index/1-3-0.html'
PLAY_URL = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash=' #1FF3CB3D374E44AAC3AC98BE047748E3
SHOW_BROWSER = True
SAVE_TO_DB = False

class Fetch_Song_Hash_From_Rank(threading.Thread):
    rank_list = []
    browser = None

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self._search_rank()
        self._search_hash()

    def _search_hash(self):
        for rank in self.rank_list:
            print('搜索：' + rank['name'] + '的hash')
            self.browser.get(rank['url'])
            song_links = self.browser.find_elements_by_css_selector('#songs li a')
            for link in song_links:
                song = {
                    "name": link.get_attribute('title'),
                    "hash": str.split(link.get_attribute('data'), '|')[0]
                }
                song_hash_queue.put(song)
            print('搜索hash结束')

    def _search_rank(self):
        global song_hash_queue
        global ROOT_URL
        if SHOW_BROWSER:
            self.browser = webdriver.Chrome()
        else:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            self.browser = webdriver.Chrome(chrome_options=chrome_options)
        
        self.browser.get(ROOT_URL)
        ranks = self.browser.find_elements_by_css_selector('.detail strong a')
        print('搜索所有排行榜')
        for rank in ranks:
            temp = {
                "name": rank.get_attribute('title'),
                "url": rank.get_attribute('href')
            }
            self.rank_list.append(temp)
        print('搜索排行榜结束')


class Fetch_Song_Data_From_Hash(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self._connect_db()
        self._search_song_from_hash()

    def _connect_db(self): 
        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client.kugou
        self.collection = db.songs

    def _search_song_from_hash(self):
        global song_hash_queue
        global PLAY_URL
        global SAVE_TO_DB
        song = song_hash_queue.get()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        }
        if song:
            print('正在搜索: <' + song['name'] + '>的信息')
            response = requests.get(PLAY_URL + song['hash'], headers=headers)
            song_obj = response.json()['data']
            with open('../output/kugou/songs.txt', 'a', encoding='utf-8') as song_file:
                json.dump(song_obj, song_file, ensure_ascii=False)
                song_file.write('\n')
            if SAVE_TO_DB:
                self.collection.insert_one(song_obj)
            print('搜索成功，正在保存')
            self._search_song_from_hash()


if __name__ == '__main__':
    t1 = Fetch_Song_Hash_From_Rank()
    t1.start()
    t2 = Fetch_Song_Data_From_Hash()
    t2.start()
    t1.join()
    t2.join()