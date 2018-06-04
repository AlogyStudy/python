#coding=utf-8

import urllib.request
import urllib.parse

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

key = input('请输入查询翻译的文字：')

# 发送到服务器的表单数据，如果是中文需要转码
fromdata = {
    'i': key,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '1528127663128',
    'sign': 'c060b56b628f82259225f751c12da59a',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTIME',
    'typoResult': 'false'
}

data = urllib.parse.urlencode(fromdata).encode('utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

request = urllib.request.Request(url, data=data, headers=headers)

html = urllib.request.urlopen(request).read().decode()

print(html)