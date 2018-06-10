#!/usr/local/bin/python

import http.cookiejar
import urllib.request

filename = 'cookie.txt'

# 声明一个MozillaCookieJar(有save实现)对象实例来保存cookie，之后写入文件
cookiejar = http.cookiejar.MozillaCookieJar(filename)

handler = urllib.request.HTTPCookieProcessor(cookiejar)
opener = urllib.request.build_opener(handler)
req = opener.open('http://www.baidu.com')

# 保存cookie到本地文件
cookiejar.save()

print(1)
