#conding=utf-8

import json
import threading
from queue import Queue

import requests
from lxml import etree

CREAWL_EXIT = False
PARSE_EXIT = False

'''
    采集线程
'''
class ThreadCrawl(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        # threading.Thread.__init__(self)
        super(ThreadCrawl, self).__init__() # 多个父类，多重继承
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.headers = {
            'user-agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)'
        }

    def run(self):
        print('start' + self.threadName)
        while not CREAWL_EXIT:
            try:
                page = self.pageQueue.get(False)
                url = 'https://www.qiushibaike.com/8hr/page/' + str(page) + '/'
                res = requests.get(url, headers=self.headers).text
                self.dataQueue.put(res)
            except:
                pass
        print('end' + self.threadName)      

'''
    解析线程
'''
class ThreadParse(threading.Thread):
    def __init__(self, threadingName, dataQueue, filename):
        super(ThreadParse, self).__init__()
        self.threadingName = threadingName
        self.dataQueue = dataQueue
        self.filename = filename

    def run(self):
        print('start' + self.threadingName)
        while not PARSE_EXIT:
            try:
                html = self.dataQueue.get(False)
                self.parse(html)
            except:
                pass
        print('end' + self.threadingName)


    def parse(self, html):
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
            self.filename.write(json.dumps(items, ensure_ascii=False) + '\n')


def main():
    # 页码
    pageQueue = Queue(10)
    # 放入1～10的数字
    for i in range(1, 10+1):
        pageQueue.put(i)

    # 采集结果（每页的HTML源码）
    dataQueue = Queue()

    filename = open('duanzi.json', 'a')

    crawlList = ['采集线程1', '采集线程2', '采集线程3']

    threadcrawl = []
    for threadName in crawlList:
        thread = ThreadCrawl(threadName, pageQueue, dataQueue)
        thread.start()
        threadcrawl.append(thread)
    
    parseList = ['解析线程1', '解析线程2', '解析线程3']
    threadparse = []
    for threadName in parseList:
        thread = ThreadParse(threadName, dataQueue, filename)
        thread.start()
        threadparse.append(thread)
    
    # 等待pageQueue队列为空， 或者 数据队列为空，也就是等待之前执行的操作执行完毕
    while not pageQueue.empty() or not dataQueue.empty():
        pass

    global CREAWL_EXIT
    CREAWL_EXIT = True
    print('queue队列为空')

    global PARSE_EXIT
    PARSE_EXIT = True
    print('data队列为空')

    for threadItem in crawlList:
        threadItem.join('')
        print('1')

if __name__ == '__main__':
    main()