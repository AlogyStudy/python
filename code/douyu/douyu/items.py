# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=0

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    nickname = scrapy.Field()
    imagelink = scrapy.Field()
    imagePath = scrapy.Field()
    # pass
