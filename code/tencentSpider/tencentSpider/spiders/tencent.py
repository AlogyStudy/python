# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencentSpider.items import tencentSpiderItem

class TencentSpiders(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://tencent.com/']

    page_link = LinkExtractor(allow=(r'start=\d+'))

    # 批量处理请求
    rules = [
        Rule(page_link, callback='parse_Tencent', follow=True) # follow:True 跟进连接请求
    ]

    def parse_Tencent(self, response):
        i = tencentSpiderItem()
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            i['positionName'] = each.xpath('./td[1]/a/text()').extract()[0]
            i['positionLink'] = each.xpath('./td[1]/a/@href').extract()[0]
            i['positionType'] = each.xpath('./td[2]/text()').extract()[0]
            i['positionNum'] = each.xpath('./td[3]/text()').extract()[0]
            i['workLocation'] = each.xpath('./td[4]/text()').extract()[0]
            i['publishTime'] = each.xpath('./td[5]/text()').extract()[0]

        return i
