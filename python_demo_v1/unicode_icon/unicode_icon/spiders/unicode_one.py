# -*- coding: utf-8 -*-
import scrapy
from unicode_icon.items import UnicodeIconItem

class UnicodeOneSpider(scrapy.Spider):
    name = 'unicode_one'
    allowed_domains = ['xahlee.info']
    start_urls = [
        'http://xahlee.info/comp/unicode_index.html',
        'http://xahlee.info/comp/unicode_hand_gesture.html',
        'http://xahlee.info/comp/unicode_food_drink.html',
        'http://xahlee.info/comp/unicode_love_symbols.html',
        'http://xahlee.info/comp/unicode_clothing.html',
        'http://xahlee.info/comp/unicode_things_icons.html',
        'http://xahlee.info/comp/unicode_tech_devices.html',
        'http://xahlee.info/comp/unicode_office_icons.html',
        'http://xahlee.info/comp/unicode_place_icons.html',
        'http://xahlee.info/comp/unicode_animals.html',
        'http://xahlee.info/comp/unicode_insects.html',
        'http://xahlee.info/comp/unicode_plants_flowers.html',
        'http://xahlee.info/comp/unicode_sports_games.html',
        'http://xahlee.info/comp/unicode_games_cards.html',
        'http://xahlee.info/comp/unicode_astronomy.html',
        'http://xahlee.info/comp/unicode_weather_symbols.html',
        'http://xahlee.info/comp/unicode_transport_and_map_symbols.html',
        'http://xahlee.info/comp/cars_trains_airplanes_boats.html',
        'http://xahlee.info/comp/unicode_music_symbols.html',
        'http://xahlee.info/comp/unicode_flags.html',
        'http://xahlee.info/comp/unicode_sex_symbols.html',
        'http://xahlee.info/comp/unicode_stars.html',
        'http://xahlee.info/comp/unicode_crosses.html',
        'http://xahlee.info/comp/unicode_dingbats.html',
        'http://xahlee.info/comp/unicode_computing_symbols.html',
        'http://xahlee.info/comp/unicode_user_interface_icons.html',
        'http://xahlee.info/comp/unicode_clocks.html',
        'http://xahlee.info/comp/unicode_arrows.html',
        'http://xahlee.info/comp/unicode_drawing_shapes.html',
        'http://xahlee.info/comp/unicode_8_new_chars.html',
        'http://xahlee.info/comp/unicode_9_new_chars.html'
    ]

    def parse(self, response):
        items = []
        url_title = response.xpath('/html/head/title/text()').extract()[0]
        titles = response.xpath('//mark[@class="unicode"]/@title').extract()
        for title in titles:
            item = UnicodeIconItem()
            item['code_title'] = title.split(': ')[1].replace(' ', '-').lower()
            item['code'] = title.split(': ')[0].replace('U+', '\\')
            items.append(item)
        print(url_title + '          --------解析成功')
        return items
