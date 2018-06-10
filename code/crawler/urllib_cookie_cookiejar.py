#!/usr/local/bin/python

import urllib.request
import http.cookiejar

cookiejar = http.cookiejar.CookieJar()

http_handler = urllib.request.HTTPCookieProcessor(cookiejar)

opener = urllib.request.build_opener(http_handler)

opener.open('http://www.baidu.com')

cook_str = ''
for item in cookiejar:
    cook_str = cook_str + item.name + '=' + item.value + ';'

print(cook_str[:-1])

# BAIDUID=5DB0FC0C0DC9692BB8EE6EDC93A2EDEA:FG=1;BIDUPSID=5DB0FC0C0DC9692BB8EE6EDC93A2EDEA;H_PS_PSSID=1468_26259_21099_26350_26580;PSTM=1528615563;BDSVRTM=0;BD_HOME=0
