#coding=utf-8

import urllib.request

# 构建一个HTTPHandler处理器对象，支持处理HTTP的请求
http_hander = urllib.request.HTTPHandler()

# 调用build_opener()方法构建一个自定义的opener对象，参数是构建的处理器对象
opener = urllib.request.build_opener(http_hander)

req = urllib.request.Request('http://www.baidu.com')

res = opener.open(req)

print(res.read().decode())
