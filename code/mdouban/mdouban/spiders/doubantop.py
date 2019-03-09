# -*- coding: utf-8 -*-
import scrapy
from mdouban.items import MdoubanItem

class DoubantopSpider(scrapy.Spider):
    name = 'doubantop'
    allowed_domains = ['douban.com']
    offset = 0
    url = 'https://movie.douban.com/top250?start='
    start_urls = [url  + str(offset)]

    def parse(self, response):
        item = MdoubanItem()
        moveis = response.xpath('//div[@class="info"]')
        for m in moveis:
            item['moveName'] = m.xpath('.//span[@class="title"][0]/text()').extract()[0]
            item['moveInfo'] = m.xpath('.//div[@class="bd"]/p/text()').extract()[0]
            item['moveStar'] = m.xpath('.//div[@class="star"]/span[@class="rating_num"]').extract()[0]
            item['moveQuote'] = m.xpath('.//p[@class="quote"]/span/text()').extract()[0]
            yield item
        
        
        self.offset += 20
        if self.offset > (250 - self.offset - 20):
            self.offset = 250
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
