## Scrapy框架

- `Scrapy`是用纯`Python`实现一个为了爬取网站数据、提取结构性数据而编写的应用框架
- `Scrapy`使用了(`Twisted`:`['twɪstɪd]`)(其主要对手是`Tornado`)异步网络框架来处理网络通讯


> 安装

通过`pip`安装`Scrapy`框架: `pip install Scrapy`

[Scrapy中文维护站点](http://scrapy-chs.readthedocs.io/zh_CN/latest/index.html)

## 基本使用

创建项目：`scrapy startproject mySpider`

项目目录结构：
```
scrapy.cfg：项目的配置文件

mySpider/：项目的Python模块，将会从这里引用代码

mySpider/items.py：项目的目标文件

mySpider/pipelines.py：项目的管道文件

mySpider/settings.py：项目的设置文件

mySpider/spiders/ ：存储爬虫代码目录
```

在`items.py`文件中配置字段
```
import scrapy


class SueItems(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
```

爬取数据：
```
#coding=utf-8

import scrapy
from mySpider.items import SueItems

class TeSpider(scrapy.Spider):
    # 爬虫名字
    name = 'ing'
    # 允许爬虫作用的范围 固定属性名allowed_domains
    allowed_domains = ['http://www.itcast.cn/']
    # 爬虫起始的url 固定属性名start_urls
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # with open('teacher.html', 'w') as f:
        #     f.write(response.body.decode())

        tearcherList = response.xpath('//div[@class="li_txt"]')

        itemTeachs = []
        for item in tearcherList:
            itemTeach = SueItems()
            # name
            name = item.xpath('./h3/text()').extract()
            # title
            title = item.xpath('./h4/text()').extract()
            # info
            info = item.xpath('./p/text()').extract()

            itemTeach['name'] = name[0]
            itemTeach['title'] = title[0]
            itemTeach['info'] = info[0]
            itemTeachs.append(itemTeach)

        return itemTeachs
```

`scrapy`项目基本步骤:
1. 创建项目`scrapy startproject xxxx`
2. 编写`items.py`文件，设置需要保存的数据字段
3. 进入`xxxx/spiders`,编写爬虫文件，文件中name就是爬虫名
4. 运行`scrapy crawl 爬虫名`，`scrapy crawl 爬虫名 -o json/csv/xml`


> Selectors选择器

`Scrapy Selectors` 内置 `XPath` 和 `CSS Selector` 表达式机制

- xpath(): 传入xpath表达式，返回该表达式所对应的所有节点的selector list列表
- extract(): 序列化该节点为Unicode字符串并返回list
- css(): 传入CSS表达式，返回该表达式所对应的所有节点的selector list列表，语法同 BeautifulSoup4
- re(): 根据传入的正则表达式对数据进行提取，返回Unicode字符串list列表

最常用到是`xpath()`


## pipeline

`yield`把一个函数当作生成器使用,这个函数会肯定有迭代或者循环，每次函数执行到`yield`到时候会返回一个值，程序会在这里暂停，函数返回生成器。


在`settings.py`文件中打开`pipline`的配置
```
ITEM_PIPELINES = {
   'mySpider.pipelines.MyspiderPipeline': 300,
    # '项目.pipeline文件.class名': 300
}
```

在`piplines.py`中写对应的`class`

```
import json


class suePipeline():
    def __init__(self):
        self.file = open('teacher.json', 'wb')

    # process_item 是类中必须要的方法，用来处理item数据
    def process_item(self, item, spider): # item: yield返回的数据
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content.encode('utf-8'))
        return item

    # 可选方法，执行结束后执行该方法
    def close_spider(self, spider):
        self.file.close()
```

把数据交给管道文件和重新发起请求：
```
# 将数据重新发给调度器入队列，出队列，交给下载器下载 新的数据
yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

# 将数据交给管道文件处理
yield item
```

`spider`文件中的编写：
```
class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['tencent.com']
    # https://hr.tencent.com/position.php?&start=3720#a
    offset = 0
    url = 'https://hr.tencent.com/position.php?&start='
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            # 初始化模型对象
            item = TencenthrItem()
            item['positionName'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['positionLink'] = each.xpath('./td[1]/a/@href').extract()[0]
            item['positionType'] = each.xpath('./td[2]/text()').extract()[0]
            item['positionNum'] = each.xpath('./td[3]/text()').extract()[0]
            item['workLocation'] = each.xpath('./td[4]/text()').extract()[0]
            item['publishTime'] = each.xpath('./td[5]/text()').extract()[0]

            # 将数据交给管道文件处理
            yield item

        if self.offset < 3720:
            self.offset += 10
        # 将数据重新发给调度器入队列，出队列，交给下载器下载 新的数据
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
```

## scrapy整体步骤

> 创建项目

通过命令行创建`scrapy`项目`scrapy startproject xxxx`

> 设置需要的字段

编写`items.py`文件，设置需要保存的数据字段
![clipboard.png](/img/bVbdNsV)

> 编写爬虫文件
 
1. 进入`xxxx/spiders`,编写爬虫文件，文件中`name`就是创建的爬虫名
2. 可以通过命令行创建爬虫文件：`scrapy genspider tencentPosition 'tencent.com'`
![clipboard.png](/img/bVbdNta)

需要初始化模型数据,导入配置的字段名的文件：
```
from tencenthr.items import TencenthrItem
```

> 使用piplines文件

在`settings.py`配置`piplines.py`中的类名
![clipboard.png](/img/bVbdNtQ)

在`piplines.py`编写逻辑：
![clipboard.png](/img/bVbdNt3)

> 运行

运行: `scrapy crawl 爬虫名`

1. `item`文件
2. 爬虫文件
3. `piplines`文件
4. `setting`文件


> 使用配置文件和重写scrapy中的类的方法

`pipeline`文件中

```
# -*- coding: utf-8 -*-
import os

import scrapy
# 引入scrapy中的处理pipelines中的images文件，继承ImagesPipeline，并重写其中`get_media_requests（重新发送请求）`,`item_completed（爬取结果处理逻辑）`方法
from scrapy.pipelines.images import ImagesPipeline
# 获取`setting.py`中定义的变量。
from scrapy.utils.project import get_project_settings


class ImagePipeline(ImagesPipeline):
    # 获取setting.py中的变量值
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        image_url = item['imagelink']
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        os.rename(self.IMAGES_STORE + '/' + image_path[0], self.IMAGES_STORE + '/' + item['nickname'] + '.jpg')
        item['imagePath'] = self.IMAGES_STORE + '/' + item['nickname']
        return item

```


> parse() 方法工作机制

```
1. 因为使用yield,而不是return,prase函数将会被当成生成器使用。scrapy会逐一获取parse方法中生成的结果，并判断该结果是一个什么样的类型；
2. 如果是request则加入爬取队列，如果是item类型则使用pipline处理，其它类型则返回错误信息。
3. scrapy取到第一部分的request不会立马就发送这个request，只是把这个request放到队列里，然后接着从生成器里获取；
4. 取尽第一部分的request，然后再获取第二部分的item，取到item了，就会放到对应的pipline里处理；
5. prase()方法作为回调函数赋值给了Request，指定parse()方法来处理这些请求scrapy.Requset(url, callback=self.parse)
6. Request对象经过调度，执行生成scrapy.http.response()的响应对象，并送回给parse()方法，直到调度器中没有Request（递归思路）
7. 取尽之后，parse()工作结束，引擎再根据队列和piplines中内容去执行响应的操作；
8. 程序在取得各个页面的items前，会先处理完之前所有resquest队列里的请求，然后再提取items。
```

## crawlSpiders

`srawlSpiders`作用：通过匹配规则，自动发送其它请求，不需要通过`yeild scrapy.Response()`手动发送

使用命令来创建`crawlSpiders`文件：
```
scrapy  genspider -t crawl tencent tencent.com
```


使用`scrapy`终端：
```
scrapy shell 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=0'
```

> LinkExtract链接提取规则

`LinkExtractors`作用: 提取连接
```
from scrapy.linkextractors import LinkExtractor
page_lx = LinkExtractor(allow=('&start=\d+')) # 正则匹配
page_lx.extract_links(response) # 提取链接，接收response对象，并返回一个scrapy.link.Link对象
```
LinkExtractor参数：
```
class scrapy.linkextractors.LinkExtractor(
    allow = (),
    deny = (),
    allow_domains = (),
    deny_domains = (),
    deny_extensions = None,
    restrict_xpaths = (),
    tags = ('a','area'),
    attrs = ('href'),
    canonicalize = True,
    unique = True,
    process_value = None
)
```
`allow`: 满足括号中“正则表达式”的值会被提取，如果为空，则全部匹配.
`allow_domains`: 会被提取的链接的domains.

> Rule爬取规则

```
class scrapy.spiders.Rule(
        link_extractor, 
        callback = None, 
        cb_kwargs = None, 
        follow = None, 
        process_links = None, 
        process_request = None
)
```

`link_extractor`: 是一个Link Extractor对象，用于定义需要提取的链接.
`callback`: 从link_extractor中每获取到链接时，参数所指定的值作为回调函数，该回调函数接受一个response作为其第一个参数。（不能重写`parse`方法）
`follow `: 是一个布尔(boolean)值，指定了根据该规则从response提取的链接是否需要跟进。 如果callback为None，follow 默认设置为True ，否则默认为False。

```
rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )
```

爬虫文件：
```
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencentSpider.items import tencentSpiderItem

class TencentSpiders(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://tencent.com/']

    page_link = LinkExtractor(allow=(r'start=\d+'))

    # 批量处理请求
    rules = [
        Rule(page_link, callback='parse_Tencent', follow=True) # follow:True 跟进连接请求
    ]

    def parse_Tencent(self, response):
        i = tencentSpiderItem()
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            i['positionName'] = each.xpath('./td[1]/a/text()').extract()[0]
            i['positionLink'] = each.xpath('./td[1]/a/@href').extract()[0]
            i['positionType'] = each.xpath('./td[2]/text()').extract()[0]
            i['positionNum'] = each.xpath('./td[3]/text()').extract()[0]
            i['workLocation'] = each.xpath('./td[4]/text()').extract()[0]
            i['publishTime'] = each.xpath('./td[5]/text()').extract()[0]

            yield i

```

## logging

Scrapy提供了log功能，可以通过`logging`模块使用。

可以修改配置文件`settings.py`，任意位置添加:
```
LOG_FILE = "TencentSpider.log"
LOG_LEVEL = "INFO"
```

> Log levels

Scrapy提供5层`logging`级别：

- `CRITICAL` - 严重错误(critical)
- `ERROR` - 一般错误(regular errors)
- `WARNING` - 警告信息(warning messages)
- `INFO` - 一般信息(informational messages)
- `DEBUG` - 调试信息(debugging messages)

> logging设置


- `LOG_ENABLED` 默认: True，启用logging
- `LOG_ENCODING` 默认: 'utf-8'，logging使用的编码
- `LOG_FILE` 默认: None，在当前目录里创建logging输出文件的文件名
- `LOG_LEVEL` 默认: 'DEBUG'，log的最低级别
- `LOG_STDOUT` 默认: False 如果为 True，进程所有的标准输出(及错误)将会被重定向到log中。例如，执行 print "hello" ，其将会在Scrapy log中显示。

一般设置保存日志的文件名和日志等级：
```
# 保存日志信息的文件名
LOG_FILE = 'tencent.log'
# 保存日志等级，高于或者等于该等级信息都被保存
LOG_LEVEL = 'INFO'
```

## scrapy模拟登陆

scrapy框架模拟登陆与中间件

模拟登陆的几种策略：
 
- 拿取cookie
- 需要提供账户密码(只需要提供post数据)
- scrapy模拟登陆方法

```
'''
提供账户/用户名/邮件 和 密码 模拟登陆
'''
import scrapy


class RenrenSpider(scrapy.Splider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = []

    def start_requires(self):
        url = 'http://www.renren.com/PLogin.do'
        yield scrapy.FormRequest(url=url, formdata={ 'email': 'xxxxxx@163.com',  'password': 'alarmchime'}, callback=self.parse_page)
    
    def parse_page(self, response):
        with open('mo.html', 'w') as f:
            f.write(response.body)
```
-----
```
'''
首先发送登陆页面的get请求，获取到页面里的登陆必须的参数，
然后和账户密码一起post到服务器，登陆成功。
'''
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'example.com'
    start_urls = ['http://www.example.com/users/login.php']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'john', 'password': 'secret'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.log("Login failed", level=log.ERROR)
            return

        # continue scraping with authenticated session...
```

[模拟登陆](https://docs.pythontab.com/scrapy/scrapy0.24/topics/request-response.html#topics-request-response-ref-request-userlogin)

> 发送POST请求

1. 可以使用:`yield scrapy.FormRequest(url, formdata, callback)`
2. 使用：重写Spider类的`start_requests(self)`方法

如果希望程序执行一开始就发送POST请求，可以重写Spider类的`start_requests(self)`方法，并且不在调用`start_urls`里的url。
```
class mySpider(scrapy.Spider):
    # start_urls = ["http://www.example.com/"]

    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'

        # FormRequest 是Scrapy发送POST请求的方法
        yield scrapy.FormRequest(
            url = url,
            formdata = {"email" : "xxx@163.com", "password" : "axxxxe"},
            callback = self.parse_page
        )
    def parse_page(self, response):
        # do something
```

## 反反爬虫相关机制

有些些网站使用特定的不同程度的复杂性规则防止爬虫访问，绕过这些规则是困难和复杂的，有时可能需要特殊的基础设施：
[scrpay自定义爬虫机制](http://doc.scrapy.org/en/master/topics/practices.html#avoiding-getting-banned)

> 通常防止爬虫被反主要有以下几个策略

- 动态设置`User-Agent`（随机切换`User-Agent`，模拟不同用户的浏览器信息）
- 禁用`Cookies`(不启用`cookies middleware`, 不想Server发送cookies, 有些网站通过cookie的使用发现爬虫行为)
    在`settings`文件中配置`COOKIES_ENABLED`设置`CookiesMiddleware`的开关
- 设置延迟下载（防止访问过于频繁，设置为 2秒 或更高）
    在`settings`文件中配置`DOWNLOAD_DELAY = 3`
- `Google Cache` 和 `Baidu Cache`使用谷歌/百度等搜索引擎服务器页面缓存获取页面数据。
- 使用IP地址池：VPN和代理IP，现在大部分网站都是根据IP来。
- 使用 [Crawlera](https://scrapinghub.com/crawlera)（专用于爬虫的代理组件），正确配置和设置下载中间件后，项目所有的`request`都是通过`crawlera`发出。
    ```
      DOWNLOADER_MIDDLEWARES = {
          'scrapy_crawlera.CrawleraMiddleware': 600
      }
    
      CRAWLERA_ENABLED = True
      CRAWLERA_USER = '注册/购买的UserKey'
      CRAWLERA_PASS = '注册/购买的Password'
    ```

## scrapy中间件

中间件作用：

- 当引擎传递给下载器当过程中，下载中间件可以对请求进行处理（例如增加http，header信息，增加proxy）
- 在下载器完成http请求，传递响应给引擎的过程中，下载中间件可以对响应进行处理（例如进行zip解压）

在`settings`配置文件中配置中间件
```
DOWNLOADER_MIDDLEWARES = {
    'scrapyProject.fileNameMiddlewares.className': 400
    # 项目名.中间件文件名.类名
    # 值是优先级，数字越小，优先级越高
}
``` 

创建`settings`取的中间件类，类中必须写`process_request`方法
```
import base64
import random

from scrapy import signals

# 获取setting中参数
from scrapy.conf import settings

# 随机User-Agent
class RandUserAgent(object):
    def process_response(self, request, spider):
        useragent = random.choice(settings['USER_AGENTS'])
        request.headers.setdefault('User-Agent', useragent)

class RandomProxy(object):
    def process_response(self, request, spider):
        proxy = random.choice(settings['PROXIES'])

        if proxy['user_parss'] is None:
            # 没有代理账户验证的代理使用方式
            request.mate['proxy'] = 'http://' + proxy['ip_prot']
        else:
            # 对账户密码进行base64编码转换
            b64_userpass = base64.b64encode(proxy['user_parss'])
            '''
                b64encode的原理
                1. 字符串转ascii码
                2. ascii码 转 二进制
                3. 6个一组（4组）
                4. 高位补0
                5. 然后得到十进制
                6. 得出的结果对照base64编码表
            '''
            # 对应到代理服务器的信令格式
            request.headers['Proxy-Authorization'] = 'Basic ' + b64_userpass

            request.meta['proxy'] = "http://" + proxy['ip_port']
```


> 为什么HTTP代理要使用base64编码

HTTP代理的原理： 就是通过HTTP协议于代理服务器**建立连接**，协议信令中包含要连接到到远程主机到IP和端口号，如果有需要身份验证的话还需要加上授权信息，服务器收到信令后首先进行身份证验证，通过后才与远程主机建立连接，连接成功之后会返回给客户端200，表示验证通过。

客户端收到收面的信令后表示成功建立连接，接下来要发送给远程主机的数据就可以发送给代理服务器了，代理服务器建立连接后会在根据IP地址和端口号对应的连接放入缓存，收到信令后再根据IP地址和端口号从缓存中找到对应的连接，将数据通过该连接转发出去。

信令格式：
```
CONNECT 59.64.128.198:21 HTTP/1.1
Host: 59.64.128.198:21
Proxy-Authorization: Basic bGV2I1TU5OTIz
User-Agent: OpenFetion
```

`Proxy-Authorization`: 身份验证信息，`Basic`后面是字符串，是用户名和密码组合后进行base64编码的结果，也就是`username:password`进行`base64.b64encode()`编码


## settings

提供了，定制Scrapy组件的方法。

[settings文档](http://scrapy-chs.readthedocs.io/zh_CN/1.0/topics/settings.html#topics-settings-ref)

> BOT_NAME

默认: `scrapybot`

当使用`startproject`命令创建项目时其也被自动赋值。

> CONCURRENT_ITEMS

默认: 100

`Item Processor`(即 Item Pipeline) 同时处理(每个response的)item的最大值。

> CONCURRENT_REQUESTS

默认: 16

Scrapy downloader 并发请求(concurrent requests)的最大值。

> DEFAULT_REQUEST_HEADERS

```
{
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en',
}
```
Scrapy HTTP Request使用的默认header。
其他地方没有配置，才使用`settings`里面的`headers`配置

> DEPTH_LIMIT

默认: 0

爬取网站最大允许的深度(depth)值。如果为0，则没有限制。


> DOWNLOAD_DELAY

默认: 0
下载器在下载同一个网站下一个页面前需要等待的时间。该选项可以用来限制爬取速度， 减轻服务器压力。同时也支持小数

> DOWNLOAD_TIMEOUT

默认: 180

下载器超时时间(单位: 秒)。

> ITEM_PIPELINES

保存项目中启用的pipeline及其顺序的字典

值(value)任意，不过值(value)习惯设置在0-1000范围内，值越小优先级越高。

> LOG_ENABLED

默认: True

是否启用logging

> LOG_LEVEL

默认: 'DEBUG'

log的最低级别。可选的级别有: CRITICAL、 ERROR、WARNING、INFO、DEBUG 。


## scrapy-redis分布式

`scrapy-redis`源码：
```
git clone https://github.com/rmax/scrapy-redis.git
```
`scrapy-redis`源码项目事例中的`setting.py`配置
```
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

# 使用了scrapy-redis里的去重组件，不使用scrapy中的去重组件
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用了scrapy-redis里的调度组件，不使用scrapy中的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 允许暂停，redis请求记录不丢失
SCHEDULER_PERSIST = True

# 默认按照scrapy请求（按优先级顺序）队列形式
# 按stored 排序顺序出队列
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# 队列形式，先进先出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 栈形式，先进后出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

# scrapy_redis.pipleines.RedisPipeline 支持将数据存储到Redis数据库里，必须启动
ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

# redis指定数据库的主机IP
REDIS_HOST = '192.168.21.63'
# 指定数据库的端口号
REDIS_PROT = 6379

# LOG日志
LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.

# 下载延迟
DOWNLOAD_DELAY = 1
```

> spiders

```
from scrapy_redis.spiders import RedisSpider


class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'
    redis_key = 'myspider:start_urls'
    # 在redis启动的时候，`lpush mysipder:start_urls http://dmoz.org(爬取的第一个站点入口)`确认当前运行的地址

    # `__init__`动态的获取allowd_domains = ['']
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
```
执行命令对改变：
```
scrapy runspider myspidre_reids.py
```

