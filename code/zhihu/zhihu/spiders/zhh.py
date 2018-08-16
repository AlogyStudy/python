# -*- coding: utf-8 -*-
import scrapy


class ZhhSpider(scrapy.Spider):
    name = 'zhh'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/explore']

    def parse(self, response):
        print(response, 'response')
