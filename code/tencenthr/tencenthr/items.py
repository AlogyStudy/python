# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencenthrItem(scrapy.Item):
    # define the fields for your item here like:
    positionName = scrapy.Field() # 职位名称
    positionLink = scrapy.Field() # 详情链接
    positionType = scrapy.Field() # 职位类别
    positionNum = scrapy.Field() # 招聘人数
    workLocation = scrapy.Field() # 工作地点
    publishTime = scrapy.Field() # 发布时间
