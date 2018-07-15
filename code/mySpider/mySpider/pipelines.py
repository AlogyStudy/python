# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


# class MyspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item

class suePipeline():
    def __init__(self):
        self.file = open('teacher.json', 'wb')

    # process_item 是类中必须要的方法，用来处理item数据
    def process_item(self, item, spider): # item: yield返回的数据
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content.encode('utf-8'))
        return item

    # 可选方法，执行结束后执行该方法
    def close_spider(self, spider):
        self.file.close()
