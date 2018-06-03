#conding=utf-8

import urllib.request
import urllib.parse

def loadPage(url, filename):
    '''
        作用: 根据url发送请求，获取服务器响应文件
        url: 需要爬取的url地址
        filename: 处理的文件名
    '''
    print('正在下载' + filename)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request).read()
    

def writePage(html, filenmae):
    '''
        作用：将html内容写入到本地
        html: 服务器响应文件内容
    '''
    print('正在保存' + filenmae)
    # 文件写入
    with open(filenmae, 'w') as f: #  with 之后，不需要做文件关闭还有其它上下文处理的操作 等同于 open(), write(), close()
        f.write(html.decode('utf-8'))
    print('-' * 30)    
    print('thanks')


def tiebaSpider(url, beginPage, endPage):
    '''
        作用: 贴吧爬虫调度器，负责组合处理
        url: 贴吧url的前部分
        beginPage: 起始页
        endPage: 结束页
    '''
    for page in range(beginPage, endPage+1):
        pn = (page - 1) * 50
        filename = '第' + str(page) + '页.html'
        fullurl = url + '&pn=' + str(pn)
        # print(fullurl)
        html = loadPage(fullurl, filename)
        writePage(html, filename)
        # print(html)

if __name__ == '__main__':
    kw = input('请输入需要爬取的贴吧名：')
    beginPage = int(input('请输入起始页：'))
    endPage = int(input('请输入结束页：'))
    
    # https://tieba.baidu.com/f?ie=utf-8&kw=javascirpt&fr=search
    url = 'https://tieba.baidu.com/f?'
    key = urllib.parse.urlencode({'kw': kw})
    fullurl = url + key

    tiebaSpider(fullurl, beginPage, endPage)
