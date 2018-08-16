# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MdoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    moveName = scrapy.Field()
    moveInfo = scrapy.Field()
    moveStar = scrapy.Field()
    moveQuote = scrapy.Field()
    # pass
