# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
# import pythondb

class MdoubanPipeline(object):
    pass
    # def __init__(self):
    #     self.f = open('movie.json', 'w')

    # def process_item(self, item, spider):
    #     print(dict(item), spider)
    #     # text = json.dumps(dict(item), ensure_ascii=False) + '\n'
    #     # self.f.write(text.encode('utf-8'))
    #     # return item

    # def close_spider(self, spider):
    #     self.f.close()
