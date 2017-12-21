
import requests
from bs4 import BeautifulSoup

"""
    =&flag=dc&=&pre_step_flag=index
"""

def run():
    url = 'https://kyfw.12306.cn/otn/leftTicket/init'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    playdata = (('leftTicketDTO.from_station_name', '%E5%8C%97%E4%BA%AC'), ('leftTicketDTO.to_station_name', '%E4%B8%8A%E6%B5%B7'), ('leftTicketDTO.from_station', 'BJP'), ('leftTicketDTO.to_station', 'SHH'), ('leftTicketDTO.train_date', '2017-12-14'), ('back_train_date', '2017-12-14'), ('purpose_code', 'ADULT'),('flag', 'dc'),('pre_step_flag', 'index'))
    response = requests.post(url, headers=headers, data=playdata)
    soup = BeautifulSoup(response.text, 'html.parser')
    a = soup.find_all("a", attrs={"class": "bgc"})


run()