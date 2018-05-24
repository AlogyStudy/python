#encoding=utf-8

import urllib.request as urllib2

# 返回类文件对象
response = urllib2.urlopen('http://www.baidu.com/')
# urlopen不支持构造

# 服务器返回类文件对象支持python文件对象的操作方法
# read()方法就是读取文件里面的全部内容，返回字符串
html = response.read()

print(html)
