# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest, Request
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule

from zhihu.items import ZhihuItem


class ZhihuspiderSpider(CrawlSpider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://zhihu.com/']

    rules = (
        Rule(LinkExtractor(allow=(r'/question/\d+#.*?', )), callback='parse_page', follow=True),
        Rule(LinkExtractor(allow=(r'/question/\d+', )), callback='parse_page', follow=True)
    )

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "http://www.zhihu.com/"
    }

    # 重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    def start_requests(self):
        return [Request('https://www.zhihu.com/signup?next=/', headers=self.headers, meta={'cookiejar': 1}, callback=self.post_login)]

    def post_login(self, response):
        # https://www.zhihu.com/api/v3/oauth/sign_in
        # xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value')
        # T05pz5fbRI1KZhdxz0ysNWMheM8FHoSO
        return [FormRequest.from_response(response,
            meta= {'cookiejar': response.meta['cookiejar']},
            headers= self.headers,
            formdata= {
                '_xsrf': 'T05pz5fbRI1KZhdxz0ysNWMheM8FHoSO',
                'emial': '1129507496@qq.com',
                'password': '1231312'
            },
            callback= self.after_login,
            dont_click= True
        )]

    def after_login(self, response):
        print(response, 'response')
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse_page(self, response):
        problem = Selector(response)
        item = ZhihuItem()
        item['url'] = response.url
        item['name'] = problem.xpath('//span[@class="name"]/text()').extract()
        item['title'] = problem.xpath('//h2[@class="zm-item-title zm-editable-content"]/text()').extract()
        item['description'] = problem.xpath('//div[@class="zm-editable-content"]/text()').extract()
        item['answer']= problem.xpath('//div[@class=" zm-editable-content clearfix"]/text()').extract()
        return item

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
