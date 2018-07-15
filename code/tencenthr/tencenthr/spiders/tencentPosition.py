# -*- coding: utf-8 -*-
import scrapy
from tencenthr.items import TencenthrItem

class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['tencent.com']
    # https://hr.tencent.com/position.php?&start=3720#a
    offset = 0
    url = 'https://hr.tencent.com/position.php?&start='
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            # 初始化模型对象
            item = TencenthrItem()
            item['positionName'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['positionLink'] = each.xpath('./td[1]/a/@href').extract()[0]
            item['positionType'] = each.xpath('./td[2]/text()').extract()[0]
            item['positionNum'] = each.xpath('./td[3]/text()').extract()[0]
            item['workLocation'] = each.xpath('./td[4]/text()').extract()[0]
            item['publishTime'] = each.xpath('./td[5]/text()').extract()[0]

            # 将数据交给管道文件处理
            yield item

        if self.offset < 3720:
            self.offset += 10
        # 将数据重新发给调度器入队列，出队列，交给下载器下载 新的数据
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
