#encoding=utf-8

import urllib.request as urllib2


ua_headres = {
    'User_Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36'
}

# urllib2.Request(url, data, headres)
# 通过urllib2.Request()方法构造一个请求对象
requset = urllib2.Request('http://www.baidu.com', headers=ua_headres)


# 返回类文件对象, urlopen不支持构造
response = urllib2.urlopen(requset)

# 服务器返回类文件对象支持python文件对象的操作方法
# read()方法就是读取文件里面的全部内容，返回字符串
html = response.read()

print(html)
