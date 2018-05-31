#enconding=utf-8

import urllib.request
import urllib.parse

url = 'http://www.baidu.com/'

headre = {
    'User-Agent': 'Mozilla'
}

keyword = input('请输入查询的关键字：')

wd = {
    'w': keyword
}

wd = urllib.parse.urlencode(wd)

# 构造get请求url和参数
fullurl = url + '?' + wd

request = urllib.request.Request(fullurl, headers=headre)

response = urllib.request.urlopen(request)

print(response.read())
