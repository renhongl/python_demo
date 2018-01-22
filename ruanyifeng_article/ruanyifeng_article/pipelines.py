# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class RuanyifengArticlePipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        with open('./output/' + item['title'][0] + '.txt', 'w', encoding='utf-8') as article_txt:
            article_txt.write(item['content'])
        return item

    def close_spider(self, spider):
        pass