#coding=utf-8

import urllib.request
import ssl

# 表示忽略未经核实的SSL证书认证
# context = ssl._create_unverified_context()

url = "https://www.12306.cn/mormhweb/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

request = urllib.request.Request(url, headers = headers)

# 在urlopen()方法里 指明添加 context 参数
# response = urllib.request.urlopen(request, context = context)
response = urllib.request.urlopen(request)

print(response.read().decode())
