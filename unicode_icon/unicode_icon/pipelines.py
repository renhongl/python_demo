# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class UnicodeIconPipeline(object):
    def __init__(self):
        self.file = open('./output/source.txt', 'w', encoding='utf-8')
        self.html = open('./output/html.txt', 'w', encoding='utf-8')
        self.css = open('./output/css.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        source = str(item) + '\n'
        html = '<i class="mr-icon mr-'+item['code_title']+'"></i>\n'
        css = '.mr-' + item['code_title'] + '::before{content:"' + item['code'] + '";}\n'
        self.file.write(source)
        self.html.write(html)
        self.css.write(css)
        return item

    def close_spider(self):
        self.file.close()
        self.html.close()
        self.css.close()
        