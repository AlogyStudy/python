# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import base64
import random

from scrapy import signals

# 获取setting中参数
from scrapy.conf import settings

# 随机User-Agent
class RandUserAgent(object):
    pass
    # def process_response(self, request, spider):
    #     useragent = random.choice(settings['USER_AGENTS'])
    #     print(useragent, '----------')
    #     request.headers.setdefault('User-Agent', useragent)

class RandomProxy(object):
    pass
    # def process_response(self, request, spider):
    #     proxy = random.choice(settings['PROXIES'])

    #     if proxy['user_parss'] is None:
    #         # 没有代理账户验证的代理使用方式
    #         request.mate['proxy'] = 'http://' + proxy['ip_prot']
    #     else:
    #         # 对账户密码进行base64编码转换
    #         b64_userpass = base64.b64encode(proxy['user_parss'])
    #         '''
    #             b64encode的原理
    #             1. 字符串转ascii码
    #             2. ascii码 转 二进制
    #             3. 6个一组（4组）
    #             4. 高位补0
    #             5. 然后得到十进制
    #             6. 得出的结果对照base64编码表
    #         '''
    #         # 对应到代理服务器的信令格式
    #         request.headers['Proxy-Authorization'] = 'Basic ' + b64_userpass

    #         request.meta['proxy'] = "http://" + proxy['ip_port']

class MdoubanSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MdoubanDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
