> MVC

- 大部分开发语言中都有`MVC`框架
- `MVC`框架的核心思想是：**解耦**
- 降低各功能模块之间的耦合性，方便变更，更容易重构代码，最大程度上实现代码的重用
- `m`表示`model`，主要用于对数据库层的封装
- `v`表示`view`，用于向用户展示结果
- `c`表示`controller`，是核心，用于处理请求、获取数据、返回结果

> MVT

- `Django`是一款python的web开发框架
- 与`MVC`有所不同，属于`MVT`框架
- `m`表示`model`，负责与数据库交互
- `v`表示`view`，是核心，负责接收请求、获取数据、返回结果
- `t`表示`template`，负责呈现内容到浏览器

客户端 -> 视图`View` -> 模型`Model` -> `Mysql` -> 模型`Model` -> 视图`View` -> 模版`Template` -> 视图`View` -> 客户端



![clipboard.png](/img/bVbkVAp)



![clipboard.png](/img/bVbkVy5)


## Django环境

安装：
```
pip install django==1.8.2
```

创建项目：
```
django-admin startproject test1
```


目录说明：

![clipboard.png](/img/bVbapaZ)

- `manage.py`：一个命令行工具，可以使你用多种方式对Django项目进行交互- 
- 内层的目录：项目的真正的Python包
- `_init _.py`：一个空文件，它告诉Python这个目录应该被看做一个Python包
- `settings.py`：项目的配置
- `urls.py`：项目的URL声明
- `wsgi.py`：项目与WSGI兼容的Web服务器入口


启动项目：
```
python manage.py runserver 8181
```

> 扩展项目目录

```
|-- app/                     # 应用主目录
    |-- templates/           # html 模板目录
        |-- app/
            |-- home.html    # 主页html
            |-- login.html   # 登陆页html
            |-- about.html   # 关于页html
            |-- ...
    |-- static/              # 静态资源目录
        |-- js/              # js资源目录
            |-- lib/         # js library 资源目录
            |-- page1/       # 页面1 js资源目录
            |-- page2/       # 页面2 js资源目录
            |-- ...
        |-- css/             # css资源目录
        |-- images/          # 图片资源目录
        |-- ...



    |-- admin.py             # 配置模型models在django原生后台的管理
    |-- apps.py              # 应用级别的配置
    |-- forms.py             # 表单处理逻辑
    |-- managers.py          # 模型处理逻辑
    |-- models.py            # 模型定义
    |-- urls.py              # 路由设置
    |-- views.py             # 控制层
    |-- tests.py
```

> 前后端项目分离

后端：
```
|-- app/                     # 应用主目录
    |-- admin.py             # 配置模型models在django原生后台的管理
    |-- apps.py              # 应用级别的配置
    |-- forms.py             # 表单处理逻辑
    |-- managers.py          # 模型处理逻辑
    |-- models.py            # 模型定义
    |-- urls.py              # 路由设置
    |-- views.py             # 控制层
    |-- tests.py
```
前端：
```
|-- src/
    |-- app/
        |-- home/            # 主页工作目录
            |-- index.html   # html 入口文件
            |-- index.js     # js 入口文件
            |-- ...
        |-- login/           # 登陆页工作目录
        |-- about/           # 关于页工作目录
        |-- ...
```

> Django有关命令

`django`安装:
```
pip install django==1.11.11
pip install -i yuan django=1.11.11
```
创建目录:
```
django-admin startproject filename
```
创建`App`:
```
python manage.py startapp appname
```
启动项目:
```
python manage.py runserver # 127.0.0.1:8000
python manage.py runserver 80 # 127.0.0.1:80
python manage.py runserver 0.0.0.0:80 # 0.0.0.0:80
```
数据库相关:
```
python manage.py makemigrations # 记录modules的变化，将变更的记录更新到 对应App下到migrations
python manage.py migrate # 翻译成SQL语句，去数据库执行
```

## Django基础使用

app的概念：一个大项目中划分成很多功能模块

> 配置静态目录

```
# 在setting.py中， Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/' # alise

STATIC_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

> django基础三件套

```
from django.shortcuts import HttpResponse, render

HttpResponse
render
redirect // 返回一条命令，浏览器再去请求重定向的地址
```

> 使用PY链接MySql


使用pymysql模块

1. 导入pymysql模块
2. 创建连接
3. 获取执行命令的游标
4. 用游标去执行SQL语句
5. 获取SQL语句的执行结果
6. 关闭游标
7. 关闭连接


> ORM

相似的数据，一类的数据放在同一张表中。具有相同属性，放在同一张表中。 

```
ORM      DB
类       数据表
属性     字段
对象     数据行
```

优点：开发效率高；不用直接写SQL语句；后端数据库变动，ORM适配。
缺点：执行效率低；SQL语句可能不是最优。

> 创建视图与ORM的app

不同的功能放在不同的包中

```
> python manage.py startapp appname
```

- 重新在使用的地方引入新的`views`的视图
- 在`settings.py`中重新配置，在字段`INSTALL_APPS`增加: `app.apps.AppConfig`


> Django使用mysql

1. 手动创建一个数据库`create database djsite`
2. 配置Django连接数据库，可以使用多个数据库（读写分离，主从服务器）
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'djsite',
            'HOST': '127.0.0.1',
            'PROT': 3306,
            'USER': 'root',
            'PASSWORD': ''
        }
    }
    ```
3. 使用第三方的包连接数据库：`pymysql`, `MySQLDb`(支持py2)，在`djsite`项目的`__init__.py`中告知`Django`使用`pymysql`
    ```
    import pymysql

    pymysql.install_as_MySQLdb()
    ```
4. 创建一张表，在`app/models.py`的文件中创建类
    ```
    from django.db import models

    # Create your models here.

    class User(models.Model):
        id = models.AutoField(primary_key=True) # id 主键
        email = models.CharField(max_length=32) # varchar(32)
        pwd = models.CharField(max_length=32) # varchar(32)
        
    ```
5. 使用ORM
    把`models.py`中变更的记录下来：`python manage.py makemigrations`
    变更的记录创建成数据库语句执行：`python manage.py migrate`

6. 视图中使用
    ```
    User.objects.filter(emial=, pwd=) # 查询数据库中的字段
    ```

> 模版语言

展示：
```
{{name}}
```

`for`循环：
```
{%for item in press_list%}
    <tr>
        <td>{{forloop.counter}}</td>
        <td>{{item.id}}</td>
        <td>{{item.name}}</td>
        <td><a href="/del_press/?id={{item.id}}">删除</a></td>
    </tr>
{%endfor%}
```

> 配置settings.py

数据库相关配置:
```
ENGIGE # 引擎相关  mysql sqllite3
NAME # 数据库名字
HOST # IP
PORT # 端口 3306
USER # 用户名
PASSWORD # 密码, ''
```
静态文件相关:
```
STATIC_URL = 'static' # 别名
STATICFILE_DIRS = [ # 静态文件地址
    os.path.join(BASE_DIR, 'static')
]
```
APP:
```
INSTALL_APP = [
    'app01.apps.App01Config' # 告知django新建了一个名叫app01的应用
    # appName.appFile.appClass
]
```
> ORM关系

```
class -> 数据表
object -> 行
attr -> 字段
```


## 图书管理系统

表的设计
```
出版社
    id, name
作者
    id, name
书
    id, title, 出版社_id(一对多，一本书只能选择一个出版社),
作者和书(多对多的关系，多一张关系表)
    id, 书_id, 作者_id
```

> CURD

模型：
```
class Press(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

```
`views.py`中`CURD`操作:
```
def press_list(request):
    press_list = Press.objects.all().order_by('id')

    return render(request, 'press_list.html', {'press_list': press_list})

def add_list(request):
    if request.method == 'POST':
        press_name = request.POST.get('name')
        Press.objects.create(name=press_name)
        return redirect('/press_list/')

    return render(request, 'add_list.html')

def del_list(request):
    del_id = request.GET.get('id')
    Press.objects.filter(id=del_id).delete()

    return redirect('/press_list/')

def edit_press(request):
    edit_id = request.POST.get('id')
    edit_press = Press.objects.get(id=edit_id)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        edit_press.name = new_name
        edit_press.save() # 注意保存
        return redirect('/press_list/')
        
    return render(request, 'edit_list.html', {'edit_item', edit_press})

```

ORM语句：
```
className.objects.all()
className.filter()
className.objects.get()
className.objects.create(name='')
className.objects.filter(id=id).delete()

# 更改
obj = className.objects.get(id=id)
obj.name = newName
obj.save() # 注意保存
```
-----
```
# 书籍表结构：
#    id, title, 关系字段(外键)

create table_book(
    id int primary_key auto_increment,
    title varchar(30) not null
    press_id int not null,
    constraint fk_press foreign key(press_id) references press(id) on delete cascade update cascade
)
```
ORM使用外键：
```
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    press = models.ForeignKey(to='Press', on_delete=models.CASCADE) # 外键， 关联Press表
```
外键查询：
```
book_obj.press # 书籍关联的出版社对象
book_obj.press_id # 数据库中实际存在的字段值
```
外键修改：
```
book_obj = Book.objects.create(title='', press=)
book_obj = Book.objects.create(title='', press_id=)
```

ORM已经存在的表，再次更改字段，没有默认值，有必须填写，Django会提示手动输入默认值。
```
null=True
default=默认值

price = Press.IntegerField(null=True)
price = Press.IntegerField(default=100)
```
-----
```
# 作者表，多对多结构：
# SQL语句：
create table author(id int primary_key auto_increment; name varchar(32) not null);
create table authorToBook(
    id int primary_key auto_increment,
    author_id int not null,
    book_id int not null,
    constraint fk_author foreign key(author_id) references author(id) on delete on update cascade,
    constraint fk_book foreign key(book_id) references book(id) on delete on update cascade
);
```

> 对多对的关系查询的使用

模型：
```
# ORM创建二张表:
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

class AuthorToBook(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE)
    book = models.ForeignKey(to='Book', on_delete=models.CASCADE)

# Django中包含多对多的关系字段`ManyToManyField`：
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    books = models.ManyToManyField(to='Book') # Django包含多对多字段
```

视图：
```
def author_list(request):
    author_data = Author.objects.all()

    # for item in author_data:
    #     print(item.books.all()) # 连表查询，使用all()查询出数据来
    return render(request, 'author_list.html', {'author_data': author_data})
```
界面：
```
<table>
        <tr>
            <th>序号</th>
            <th>作者id</th>
            <th>作者名字</th>
            <th>作者作品</th>
        </tr>
        {% for author in author_data %}
        <tr>
            <td>{{forloop.counter}}</td>
            <td>{{author.id}}</td>
            <td>{{author.name}}</td>
            <td>
            {% for book in data.books.all %}
                {% if forloop.last %}
                    《{{book.title}}》
                {% else %}
                    《{{book.title}}》,
                {% endif %}
            {% empty %}
                暂无作品
            {% enfor %}
            </td>
        </tr>
        {% endfor %}
    </table>
```

查询多对多的关系字段：
```
author_obj.books.all()
```
修改：
```
author_obj.set(['book1', 'book2'])
author_obj.add('book1', 'book2', 'book3')
```
清除:
```
author_obj.clear() # 清除对应关系
```

> ORM操作

查:
```
from app01.models import User, Press, Book, Author

Press.object.all() # 查询所有出版社对象(对象列表queryset)
Press.object.filter(条件) # 查询所有满足条件的对象
Press.object.get(条件) # 查询有且只有一个对象

# 属性
press_obj.id
press_obj.name

# 外键属性
book_obj.id
book_obj.press # 关联对象
book_obj.press.id

# 多对多属性
author_obj.books # 管理对象
author_obj.books.all() # 作者关联的所有书籍对象
```
增:
```
from app01.models import User, Press, Book, Author

new_press_obj = Press.object.create(name='')

# 外键的增加
Book.object.create(title='', prece='', press_id=press_obj.id)
Book.object.create(title='', prece='', press=press_obj)

# 多对多关系的增加
new_author_obj = Author.object.create(name='')
new_author_obj.books.set([press_id, press_id])
new_author_obj.books.set([book1, book2])
new_author_obj.books.add(book1, book2)
```
删:
```
book_obj.delete(条件) # 删除满足条件单个对象
Press.object.filter(条件).delete() # 删除满足条件的多个对象
```
改:
```
press_obj.name = ''
press_obj.save() # 注意修改保存

Press.object.filter(条件).update() # 修改满足条件的多个对象

# 外键的修改
book_obj.press = press_obj
book_obj.save()
book_obj.press_id = press_obj.id

# 多对多字段的修改
author_obj.name = ''
author_obj.save()

author_obj.books.set([press_id, press_id])
```

> 文件上传

```
f_dict = request.FILES.get('name') # 文件字典
    print(f_dict)
    with open(f_dict, 'wb') as f:
        for chunk in f_dict.chunk():
            f.write(chunk)
```


## 模版语言

变量相关:`{{}}`
逻辑相关:`{%  %}`

点`.`在模版语言中，有特殊的含义，顺序为：
1. 字典查询
2. 属性或方法查询
3. 数字索引查询

```
{{name}}
{{dict1.name}}
{{list1.0}}
```
模版语言中方法不用加`()`执行，Django自动调用，只能调用不带参数的方法。

> filter


```
# {{变量名|方法|参数}}
{{name|fun}}
{{ value|add:"2" }} # 支持链式操作
{{ value|date:"D d M Y" }} {{ value|time:"H:i" }}
```
- 过滤器后加个冒号，再紧跟参数，中间不能有空格。
- 支持一个参数。

`if`语句支持`过滤器`, `and`, `or`, `==`, `<`, `>`, `in`, `!=`, `is`, `is not`, `not in`, `<=`, `>=`

> 自定义filter

1. 在`app`中新建一个**`templatetags`**包（名字固定，不能变，只能是这个），和`views.py`、`models.py`等文件处于同一级别目录下。这是一个包！不要忘记创建`__init__.py`文件以使得该目录可以**作为Python的包**。
2. 在创建的包中，创建`.py`文件作为过滤器文件
    ```
    from django import template

    # 生成注册实例
    register = template.Library()

    @register.filter # 告知模版语言，自定义的filter
    def counter(val):
        '''
            counter
            :params {val} 管道符参数
            :return {}
        '''
        return val + 'counter'
    ```
3. 在`.html`视图文件中导入，并使用。
    ```
    # 导入filter模块
    {%  load counter  %}
    # 使用该过滤器
    {{ret|counter}}
    ```
4. 需要重启django项目。


> csrf

`CSRF`一般是`POST`请求：
```
{% csrf_token %}
```
- `<form>...</form>`标签；
- 使用`POST`的方法时，必须添加`{% csrf_token %}`标签，用于处理**csrf安全机制**；
- `{{ form }}`代表Django为你生成其它所有的form标签元素，提交按钮需要手动添加；

> 母板与继承

```
# 子页面中继承父页面
{% extends 'list/base.html' %}

# 父级页面`base.html`
{% block contenter %}
{% endblock %}

# 子页面
{% block contenter %}
{% endblock %}
```

> 组件

```
# 引入组件
{% include 'nav.html' %}
```

> 静态文件

```
{% load static %}

<link href="{% static % 'bootstrap-3.3.7/css/bootstrap.css'}" />

{% load static %}
{% get_static_prefix %} # 去settings.py中获取STATIC_URL的value值
```

> 自定义inclusion_tags

1. 在app下创建一个templatetags的python包
2. 在包下写py文件，`mytags`
3. 编辑文件
    ```
    from django import template
    register = template.Library()
    ```
4. 定义函数，可以接收参数，需要返回字典
    ```
    @register.include_tag(filename) # 组件名字
    def pagination(total):
        return {'total': total}
    ```
5. 在模版文件中使用字典参数，进行渲染
6. 使用
    ```
    {% load mytags %}
    { pagination 10 }
    ```
    
## Django中的视图

一个视图函数（类）称之为视图，它接受Web请求并且返回Web响应。
响应可以是一张网页的HTML内容，一个重定向，一个404错误，一个XML文档，或者一张图片。
无论视图本身包含什么逻辑，都要返回响应。为了将代码规范，约定俗成将视图放置在项目(project)或应用程序(app)目录中命名为`view.py`文件中。

> FBV(Function Based View)

```
def login(request):
    # return HttpResponse('ok')
    # print(request.POST, 'post')
    # print(request.Method, 'method')
    # print(request.GET, 'get')
    return render(request, 'login.html', {'ret': 'test'})
```

> CBV(class Based View)

```
from django.views import View

class AddPress(View):
    def get(self, request):
        return render(request, 'add_press.html')

    def post(self, request):
        press_name = request.POST.get('name')
        Press.objects.create(name=press_name)
        return rediract('/press_list/')
```

在`url.py`中使用
```
url(r'/add_press/', views.AddPress.as_view())
```

流程：
1. `views.AddPress.as_view()`获取源码的`view`函数
2. 当请求到来的时候执行`view`函数
    实例化自己定义的类赋值给`self`
        self = cls(**initkwargs)
    self.request = request
    执行父类中的`self.dispatch(request, *args, **kwargs)`
3. `self.dispatch(request, *args, **kwargs)`
    判断请求方式是否被允许
        handler = 允许的请求下通过**反射**获取自己定义的类中的`get`, `post`方法
    不允许的情况下
        handler = 不允许的情况, 父类中的http_method_not_allowed方法
    执行`handler`方法
    返回`HttpResponse`对象
4. 把返回`HttpResponse`对象返回给`Django`


> requset和response对对象：

`requset`对象：
```
['COOKIES', 'FILES', 'GET', 'META', 'POST', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_host', 'get_port', 'get_raw_uri', 'get_signed_cookie', 'is_ajax', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user', 'xreadlines']
```
`requset`常用的对象:
```
requset.method
requset.GET
requset.POST
requset.FILES
requset.COOKIES
requset.path_info
requset.body
requset.scheme # 协议
requset.encoding # 编码
requset.META # 元数据

requset.get_host() # ip:host
requset.is_ajax() # 是否是ajax请求
```

`response`对象：
```
from django.shortcuts import redner, HttpResponse, redirect

HttpResponse('字符串')
redner(requset, 'xxx.html', {ret: ret})
redirect('跳转地址') # Location

# 返回json数据，序列化
from django.http import JsonResponse
def json_data(request):
    ret = {'name': 'su', 'age': 30}
    # return HttpResponse(json.dumps(ret)) # Content-Type: text/html charset=utf-8
    return HttpResponse(json.dumps(ret), content_type: 'application/json')
    return JsonResponse(ret) # Content-Type: application/json
```
   
## 路由

`URL`是Web服务的入口，用户通过浏览器发送过来的任何请求，都是发送到一个制定的URL地址，然后被响应。

`urlpatterns`中的元素按照书写顺序从上往下逐一匹配正则表达式，一旦匹配成功则不再继续。

> 分组

```
url(r'^test/(\d{4})/\d{2}$', views.test) # test函数接收到正则匹配分组的参数
```
命名分组：
```
url(r'^test/(?P<year>\d{4})/\d{2}$', views.test) # test函数接收到正则匹配分组的year参数，也可以通过`args`或`**kwargs`来获取参数
```

> 视图默认参数

```
# URLconf
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^blog/$', views.page),
    url(r'^blog/page(?P<num>[0-9]+)/$', views.page),
]

# View (in blog/views.py)
def page(request, num="1"): # 当没有传递使用num=1
    pass
```

> 路由转发

通常，在每个`app`里，各自创建一个`urls.py`路由模块， 然后从根路由出发，将`app`所属的`url`请求，全部转发相应的`urls.py`模块中。

项目目录的`url.py`下:
```
from django.conf.urls import include, url

urlpatterns = [
    url(r'^community/', include('app.aggregator.urls')),
    url(r'^contact/', include('app.contact.urls')),
]
```
`app/aggregator/urls.py`下：
```
from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^test/', views.test)
]
```

地址栏访问方式：`127.0.0.1:8000/app/test`, test是`app`下定义的路由

> 命名URL和URL反向解析

命名：
```
url(r'press_list/', views.press_list, name='press_list') # 命名
url(r'^home/(\d{4})/(\d{2})/$', views.home, name=home) # 分组
url(r'^home/(?P<year>\d{4})/(?P<month>\d{2})/$', views.home, name=home) # 命名分组
```

反向：
```
# 视图中应用
from django.shortcuts import redirect, reverse

def press_list():
    # reverse('press_list') -> /press_list/
    redirect(reverse('press_list'))

    # url(r'^home/(\d{4})/(\d{2})/$')
    redirect(reverse('home', args=('2018', '12'))) # 分组，需要传递参数 'app/home/2018/12'

    # url(r'^home/(?P<year>\d{4})/(?P<month>\d{2})/$', views.home, name=home)
    redirect(reverse('home', kwargs={'year': 2018, 'month': 12})) # 命名分组
```
-----
```
# 模版中应用
{% url 'press_list' %}  # 命名
{% url 'home' '2018' '11' %}  # 分组
{% url 'home' year='2018' month='10' %}  # 命名分组
```

> 命名空间 namespace

```
# urls
url(r'^app01/', include('app01.urls', namespace='app01'))
url(r'^app02/', include('app02.urls', namespace='app02'))
```
-----
```
# 视图中使用
def home(request):
    reverse('app01:home')
    return HttpResponse('ok')
```

```
def delete(request, table, del_id):
    table_class = getattr(models, table.capitalize()) # getattr() 字符串映射到对象
    table_class.objects.get(id=del_id).delete()

    return redirect(reverse(table)) # reverse 反向解析
```

## ORM

> 字段类型

| 类型 | 说明 |
|: --- :|: --- :|
| AutoField | 自增整数类型字段。Django会自动添加字段: `id = models.AutoField(primary_key=True),从1开始计数。主键 |
| BooleanField | 布尔值类型。默认值是`None`。在HTML表单中表现为`CheckboxInput`标签，如果要接受`null`只，使用`NullBooleanFiled` |
| CharField | 字符串类型。 必须接受字段`max_length`,表示字符串长度不能超过该值，默认的标签`Input text`,最常用的filed。|
| DateField | `class DateField(auto_now=False, auto_now_add=False, **options)`日期类型。一个Python中的`datetime.date`的实例。在HTML中表现为`TextInput`标签。Django会帮你自动添加一个JS的日历表和一个“Today”快捷方式，以及附加的日期合法性验证。两个重要参数：**（参数互斥，不能共存）** `auto_now`: 每当对象被保存时将字段设为当前日期，常用于保存最后修改时间。`auto_now_add`：每当对象被创建时，设为当前日期，常用于保存创建日期(注意，是不可修改的)。设置上面两个参数就相当于给field添加了`editable=False`和`blank=True`属性。如果想具有修改属性，请用`default`参数。例：`pub_time = models.DateField(auto_now_add=True)`，自动添加发布时间。|
| EmailField | 邮箱类型，默认max_length最大长度254位。|
| FileField | `class FileField(upload_to=None, max_length=100, **options)`上传文件类型 |
| ImageField | 图像类型 |
| FilePathField | 文件路径信息。以字符串的形式存在，默认最大长度100，可以通过max_length参数设置。|
| IntegerField | 整数类型，最常用的字段之一。取值范围-2147483648到2147483647。在HTML中表现为`NumberInput`标签。 |
| GenericIPAddressField | `class GenericIPAddressField(protocol='both', unpack_ipv4=False, **options)[source]`IPV4或者IPV6地址，字符串形式 |
| TextField | 大量文本内容，在HTML中表现为Textarea标签 |
| URLField | 一个用于保存URL地址的字符串类型，默认最大长度200。 |
| UUIDField | 用于保存通用唯一识别码（Universally Unique Identifier）的字段。使用Python的UUID类 |

`UUIDField`: 需要设置`default`参数
```
import uuid
from django.db import models

def MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # other filed
```

> Meta配置

```
class UserInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)

    # 表进行相关配置
    class Mate:
        db_table = 'table_name' # 数据库中生成的表名，默认：appname + 下划线 + 类名
        verbose_name = '个人信息' # admin中显示的表名称
        index_together = [ # 联合索引
            ('pub_date', 'deadline') # 应为两个存在的字段
        ]
        unique_together = (('driver', 'restaurant'),) # 联合唯一索引
```

> 查询数据的13个方法

[django ORM操作](https://www.cnblogs.com/maple-shaw/articles/9403501.html)

```
import os

if __name__ == '__main__':
    os.environ.setdefault(‘DJANGO_SETTINGS_MODULE’, ‘project_name.settings’) # 设定配置文件
    import django
    django.setup()

    from appname import models # 导入app中的模块

    # all() 所有对象列表
    # p = models.Person.objects.all()

    # get() 获取多个对象列表
    # p = models.Person.objects.get(id=id) # 查询不到报错

    
    # filter() 满足条件的对象列表
    # p = models.Person.objects.filter(id=1)

    # exclude() 不满足条件的对象列表
    # p = models.Person.objects.exclude()

    # values() # 取具体的数据的对象列表。 字典形式key: val
    # 没有指定参数，是所有的表的字段，可以制定某些字段。
    # p = models.Person.objects.all().values()
    # p = models.Person.objects.all().values('id', 'name')

    # values_list() # 取具体的数据的对象列表。元祖形式 val
    # 没有指定参数，是所有的表的字段，可以制定某些字段。
    # p = models.Person.objects.all().values_list()

    # order_by() # 排序
    # p = models.Person.objects.all().order_by('id')
    # p = models.Person.objects.all().order_by('-id') # 降序
    # p = models.Person.objects.all().order_by('age', 'id') # 多个字段排序

    # reverse() # 反序
    # p = models.Person.objects.all().order_by().reverse() # 需要进行排序后再反转

    # distinct() # 去重

    # count() # 统计
    # p = models.Person.objects.all().count()

    # first(), last()
    # p = models.Person.objects.all().first()
    # p = models.Person.objects.filter().first()

    # exists() # 是否存在数据
    # p = models.Person.objects.all().exists()
    print(p)
```


> 单表查询

```
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djsite.settings")
    import django
    django.setup()

    from app01 import models

    ret = models.Person.objects.filter(id__gt=1) # 大于
    ret = models.Person.objects.filter(id__lt=4) # 小于
    ret = models.Person.objects.filter(id__gte=1) # 大于等于
    ret = models.Person.objects.filter(id__lte=1) # 小于等于
    ret = models.Person.objects.filter(id__in=[1, 3]) # 小于等于

    ret = models.Person.objects.filter(id__in=[1, 3]) # id=1, id=3
    ret = models.Person.objects.filter(id__lt=1, id__gt=3) # 1 < x < 3
    ret = models.Person.objects.filter(id__range=[1, 3])

    ret = models.Person.objects.filter(name__contains='e') # name包含e，模糊查询
    ret = models.Person.objects.filter(name__icontains='e') # name包含e，忽略大小写，模糊查询

    ret = models.Person.objects.filter(name__startswith='e') # 开头包含e
    ret = models.Person.objects.filter(name__istartswith='e') # 开头包含e，忽略大小写

    ret = models.Person.objects.filter(name__endswith='e') # 结尾包含e
    ret = models.Person.objects.filter(name__iendswith='e') # 结尾包含e，忽略大小写

    ret = models.Person.objects.filter(birth_year=2018) # 2018年份
    ret = models.Person.objects.filter(birth_month=12) # 12月份
    ret = models.Person.objects.filter(birth_day=12) # 天数

    print(ret, 'ret')

```

> 外键查询

django终端打印SQL语句：

```python
# 配置在`settings.py`中
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}
```
-----

```
#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djsite.settings')

    import django

    django.setup()

    from app import models

    book_obj = models.Book.objects.get(id=2)

    obj1 = models.Book.objects.filters(publisher__name='xxxx') # INNER JOIN 联表查询
    obj2 = models.Book.objects.all().values('title', 'publisher__name') # 表名__字段名
 
```

[多对多的查询](http://www.liujiangblog.com/course/django/98)


