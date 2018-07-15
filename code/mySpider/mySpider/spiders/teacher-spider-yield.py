#coding=utf-8

import scrapy
from mySpider.items import SueItems

class TeSpider(scrapy.Spider):
    # 爬虫名字
    name = 'sue'
    # 允许爬虫作用的范围 固定属性名allowed_domains
    allowed_domains = ['http://www.itcast.cn/']
    # 爬虫起始的url 固定属性名start_urls
    start_urls = [
        'http://www.itcast.cn/channel/teacher.shtml',
        'http://www.itcast.cn/channel/teacher.shtml#ac',
        'http://www.itcast.cn/channel/teacher.shtml#acloud',
        'http://www.itcast.cn/channel/teacher.shtml#ads',
        'http://www.itcast.cn/channel/teacher.shtml#ago',
        'http://www.itcast.cn/channel/teacher.shtml#ajavaee',
        'http://www.itcast.cn/channel/teacher.shtml#aLinux',
        'http://www.itcast.cn/channel/teacher.shtml#amovies',
        'http://www.itcast.cn/channel/teacher.shtml#anetmarket',
        'http://www.itcast.cn/channel/teacher.shtml#aphp',
        'http://www.itcast.cn/channel/teacher.shtml#apm',
        'http://www.itcast.cn/channel/teacher.shtml#apython',
        'http://www.itcast.cn/channel/teacher.shtml#astack',
        'http://www.itcast.cn/channel/teacher.shtml#atest',
        'http://www.itcast.cn/channel/teacher.shtml#aui',
        'http://www.itcast.cn/channel/teacher.shtml#auijp',
        'http://www.itcast.cn/channel/teacher.shtml#aweb',
        'http://www.itcast.cn/channel/teacher.shtml#awlw'
    ]

    def parse(self, response):
        # with open('teacher.html', 'w') as f:
        #     f.write(response.body.decode())

        tearcherList = response.xpath('//div[@class="li_txt"]')

        # itemTeachs = []
        for item in tearcherList:
            itemTeach = SueItems()
            # name
            name = item.xpath('./h3/text()').extract()
            # title
            title = item.xpath('./h4/text()').extract()
            # info
            info = item.xpath('./p/text()').extract()

            itemTeach['name'] = name[0]
            itemTeach['title'] = title[0]
            itemTeach['info'] = info[0]

            yield itemTeach
            # itemTeachs.append(itemTeach)

        # return itemTeachs
