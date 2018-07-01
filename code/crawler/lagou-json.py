#coding=utf-8

import json
import urllib.request
import jsonpath

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36 QQBrowser/4.3.4986.400'
}
# url = 'https://www.lagou.com/jobs/companyAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false'
url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)
html = response.read().decode()

unicodeStr = json.loads(html)
# content = unicodeStr['msg']
content = jsonpath.jsonpath(unicodeStr, '$..name')
print(content)
array = json.dumps(content, ensure_ascii=False)

with open('lagoucontent.json', 'w') as f:
    f.write(array)
