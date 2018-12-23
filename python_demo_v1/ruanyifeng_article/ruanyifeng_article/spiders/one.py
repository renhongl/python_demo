# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ruanyifeng_article.items import RuanyifengArticleItem

class OneSpider(CrawlSpider):
    name = 'one'
    allowed_domains = ['ruanyifeng.com']
    start_urls = ['http://www.ruanyifeng.com/blog/']

    rules = (
        Rule(LinkExtractor(allow=r'blog/\w+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = RuanyifengArticleItem()
        item['title'] = response.xpath('//h1[@id="page-title"]/text()').extract()
        data = response.xpath('//div[@id="main-content"]')
        item['content'] = data.xpath('string(.)').extract()[0]
        return item
