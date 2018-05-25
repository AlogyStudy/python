#encoding=utf-8

import urllib.request as urllib2
import random

url = 'http://www.baidu.com/'

# 可以是User-Agent列表，也可以是代理列表。 作用：反反爬虫
ua_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50'
]

# 在User-Agent列表里随机选择一个User-Agent
user_agent = random.choice(ua_list)

# 构造一个请求
request = urllib2.Request(url)

# add_header()方法，添加/修改 一个HTTP报头
request.add_header('User-Agent', user_agent)

# get_header() 获取一个已有的HTTP报头值，只能第一个字母大写，其它的必须小写
request.get_header('User-agent')

response = urllib2.urlopen(request)

html = response.read()
print(html)
