#coding=utf-8

import scrapy

class TeSpider(scrapy.Spider):
    # 爬虫名字
    name = 'te'
    # 允许爬虫作用的范围
    allowdDomains = ['http://www.itcast.cn/']
    # 爬虫起始的url
    startUrls = ['http://www.itcast.cn/channel/teacher.shtml#']

    def parse(self, response):
        with open('teacher.html', 'w') as f:
            f.write(response.body.decode())
