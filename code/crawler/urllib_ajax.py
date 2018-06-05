#coding=utf-8

import urllib.request
import urllib.parse


url = 'https://movie.douban.com/j/search_subjects?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}
formdata = {
    'type': 'movie',
    'tag': '热门',
    'sort': 'recommend',
    'page_limit': 20,
    'page_start': 40
}

data = urllib.parse.urlencode(formdata).encode('utf-8')
request = urllib.request.Request(url, data=data, headers=headers)
html = urllib.request.urlopen(request).read().decode()

print(html)
