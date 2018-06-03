#enconding=utf-8

import urllib.request
import urllib.parse

url = 'http://www.baidu.com/s'

headre = {
    'User-Agent': 'Mozilla'
}

keyword = input('请输入查询的关键字：')

wd = {
    'wd': keyword
}

# 通过urllib.parse.urlencode()参数是一个dict类型的，转化成url参数形式 =号链接起来
wd = urllib.parse.urlencode(wd)

# 构造get请求url和参数
fullurl = url + '?' + wd

print(fullurl)
request = urllib.request.Request(fullurl, headers=headre)

response = urllib.request.urlopen(request)

print(response.read())
