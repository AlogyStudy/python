#coding=utf-8

import urllib.request
import json
from lxml import etree

url = 'http://www.qiushibaike.com/8hr/page/1'
headers = {
    'user-agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)'
}

req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req).read()
text = etree.HTML(html)

node_list = text.xpath('//div[contains(@id, "qiushi_tag")]')

items = {}
for node in node_list:
    username = node.xpath('./div[@class="author clearfix"]//h2/text()')[0]

    image = node.xpath('.//div[@class="thumb"]//@src')

    content = node.xpath('.//div[@class="content"]/span')[0].text

    zan = node.xpath('.//i')[0].text

    comment = node.xpath('.//i')[1].text

    items = {
        'username': username,
        'image': image,
        'content': content,
        'zan': zan,
        'comment': comment
    }

    with open('qiushi.json', 'a') as f:
        f.write(json.dumps(items, ensure_ascii=False) + '\n')

print('ok')
