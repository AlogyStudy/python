#conding=utf-8

import urllib.request
import urllib.parse
from lxml import etree # 我乃河北，姓氏颜良

class getQdailyImg:
    def __init__(self, url):
        self.url = url

    def loadPage(self):
        print('正在下载...')
        headres = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36 QQBrowser/4.3.4986.400'
        }
        req = urllib.request.Request(self.url, headers=headres)
        html = urllib.request.urlopen(req).read().decode()
        xmlDom = etree.HTML(html)
        linkList = xmlDom.xpath('//div[@class="pic imgcover"]/img/@src')
        print(linkList)
        self.writePage(linkList)

    def writePage(self, data):
        for item in data:
            with open('img.txt', 'w') as f:
                f.write(item)

if __name__ == '__main__':
    qdI = getQdailyImg('http://www.qdaily.com/')
    qdI.loadPage()