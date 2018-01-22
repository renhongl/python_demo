# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from unicode_icon.items import UnicodeIconItem


class UnicodeTwoSpider(CrawlSpider):
    name = 'unicode_two'
    allowed_domains = ['xahlee.info']
    start_urls = ['http://xahlee.info/comp/unicode_index.html']

    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=False),
    )
    total = 0

    def parse_item(self, response):
        items = []
        url_title = response.xpath('/html/head/title/text()').extract()[0]
        titles = response.xpath('//mark[@class="unicode"]/@title').extract()
        for title in titles:
            item = UnicodeIconItem()
            item['code_title'] = title.split(': ')[1].replace(' ', '-').lower()
            item['code'] = title.split(': ')[0].replace('U+', '\\')
            items.append(item)
        self.total = self.total + 1
        print(str(self.total) + ': ' + url_title + '          --------解析成功')
        return items
