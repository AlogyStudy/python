#coding=utf-8

# import cookielib
import http.cookiejar
import urllib.request
import urllib.parse

# 通过CookieJar()类构建一个cookieJar()对象，用来保存cookie的值
cookie = http.cookiejar.CookieJar()

# 通过HTTPCookieProcessor()处理器构建一个处理器对象，用来处理cookie
cookie_headler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(cookie_headler)
print(dir(cookie))

opener.add_handler = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')]
# 先post数据，然后保存起来，后续再次使用

url = ''

data = {
    'email': '',
    'password': ''
}

data = urllib.parse.urlencode(data)

req = urllib.request.Request(url, data=data)

res = opener.open(req)

print(res.read().decode())
