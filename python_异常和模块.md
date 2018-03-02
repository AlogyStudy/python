## 异常处理

单个异常处理：
```
try:
    print(num)

except NameError:
    print('没有定义变量')

except FileNotFoundError:
    print('找不到文件路径')

print(1)
```

多个异常处理：
```
try:
    print(num)
    # 11/0
    # open('xxx.txt')
except (NameError, FileNotFoundError, ZeroDivisionError): # 多个异常统一处理
    print('异常')

print(1)
```

所有异常处理：
```
try:
    print(num)
except Exception: # 所有异常处理
    print('所有异常处理')

print(1)
```

查看原来异常输出:
```
try:
    print(num)
except Exception as err:
    print(err)
print(1)    
```

没有异常执行
```
try:
    a = 1

execpt Exception as err:
    print(err)

else:
    print('没有异常执行')

finally:
    print('不管是否出现异常, 都执行')

print(1)     
```
-----

```
import time
try:
	f = open('test.txt')
	try:
		while True
			content = f.readline()
			if len(content) == 0:
				break
			time.sleep(2)
			print(content)
	except Exception:
		# pass
        print('文件产生异常')
	finally:
		f.close()
		print('关闭文件')
except Exception:
	print('没有这个文件')
```

`try`与`except`需要同时存在
当函数嵌套的时候，如果函数出现异常，会返回异常，然后捕获到异常

## 抛出自定义异常

`raise`: 抛出一个自定义异常

`raise`语句如果不带参数，就会把当前错误原样抛出。

```
def main ():
    try:
        s = input('请输入-->')
        if len(s) < 3:
            raise ShortInputException(len(s), 3)
        else:
            print(s)
    except ShortInputException as result:
        print('ShortInputException: 输入的长度是 %d, 长度至少需要是 %d' % (result.length, result.atleast))
    else:
        print('没有异常发生.')

class ShortInputException(Exception):
    '''自定义异常类'''
    def __init__(self, length, atleast):
        # super().__init()
        self.length = length
        self.atleast = atleast

main()
```

## 模块

如何获取当前模块的文件名: `__file__`

> 引入模块

`import sys`导入模块中的全部功能
`from argv import sys`, `from argv import sys,executable`导入模块中的单独功能
`from sys import *`
`from sys as s` 别名

`__name__`: 用于表示当前模块的名字，同时还能反映一个包的结构
1. 导入输出的是当前模块名
2. 模块被直接运行时模块名为：`__main__`

```
if __name__ == '__main__': # 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
    # code
```


> 常用内建模块

|标准库|	说明|
|--- | ---|
|builtins|	内建函数默认加载|
|os|	操作系统接口 [系统级别的操作(文件和目录)]|
|sys|	Python自身的运行环境 [对解释器相关的操作]|
|functools|	常用的工具|
|json & pickle|	编码和解码 JSON 对象|
|logging|	记录日志，调试|
|multiprocessing|	多进程|
|threading	|多线程|
|copy|	拷贝|
|time|	时间|
|datetime|	日期和时间|
|calendar|	日历|
|hashlib|	加密算法|
|random|	生成随机数|
|re|	字符串正则匹配|
|socket|	标准的 BSD Sockets API|
|shutil|	文件和目录管理 [高级的 文件、文件夹、压缩包 处理模块(递归，文件复制等)]|
|glob|	基于文件通配符搜索|
|shelve| 一个简单的`k,v`将内存数据通过文件持久化的模块，可以持久化任何`pickle`可支持的`python`数据格式|

**hashlib**

```
import hashlib
m = hashlib.md5()   # 创建hash对象，md5:(message-Digest Algorithm 5)消息摘要算法,得出一个128位的密文
print m             # <md5 HASH object>
m.update('alogy')  # 更新哈希对象以字符串参数
print m.hexdigest() # 返回十六进制数字字符串
```

例子：用于注册、登录

```
import hashlib
import datetime
KEY_VALUE = 'alogy'
now = datetime.datetime.now()
m = hashlib.md5()
str = '%s%s' % (KEY_VALUE,now.strftime("%Y%m%d"))
m.update(str.encode('utf-8'))
value = m.hexdigest()
print(value) # c69c59b58209a94f40e6a7a425f9a977
```

> functools

```
['WRAPPER_ASSIGNMENTS', 'WRAPPER_UPDATES', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cmp_to_key', 'partial', 'reduce', 'total_ordering', 'update_wrapper', 'wraps']
```

**partial()**

把一个函数的某些参数设置默认值，返回一个新函数，调用这个新函数会更简单。

```
import functools

def showarg(*args, **kw):
    print(args)
    print(kw)

p1 = functools.partial(showarg, 1, 2, 3)
p1()
p1(4,5,6)
p1(a='python', b='alogy')

p2 = functools.partial(showarg, a=3, b='linux')
p2()
p2(1, 2)
p2(a='python', b='alogy')
```

**wraps()**


使用装饰器时，被装饰后等函数其实已经是另外一个函数（函数名等函数属性会发生变化）

添加后由于函数名和函数的`doc`发生了改变，对测试结果有一些影响，例如:
```
def note(func):
    "note function"
    def wrapper():
        "wrapper function"
        print('note something')
        return func()
    return wrapper

@note
def test():
    "test function"
    print('I am test')

test()
print(test.__doc__)
```
运行结果
```
note something
I am test
wrapper function
```
所以，Python的functools包中提供了一个叫wraps的装饰器来消除这样的副作用。例如：

```
import functools
def note(func):
    "note function"
    @functools.wraps(func) # 保存外边函数名
    def wrapper():
        "wrapper function"
        print('note something')
        return func()
    return wrapper

@note
def test():
    "test function"
    print('I am test')

test()
print(test.__doc__)
```
运行结果
```
note something
I am test
test function
```

> 常用扩展库

|扩展库 |	说明 |
| --- | --- |
|requests|	使用的是 urllib3，继承了urllib2的所有特性|
|urllib|	基于http的高层库|
|scrapy|	爬虫|
|beautifulsoup4|	HTML/XML的解析器|
|celery|	分布式任务调度模块|
|redis|	缓存|
|Pillow(PIL)|	图像处理|
|xlsxwriter|	仅写excle功能,支持xlsx|
|xlwt|	仅写excle功能,支持xls ,2013或更早版office|
|xlrd|	仅读excle功能|
|elasticsearch|	全文搜索引擎|
|pymysql|	数据库连接库|
|mongoengine/pymongo|	mongodbpython接口|
|matplotlib|	画图|
|numpy/scipy|	科学计算|
|django/tornado/flask|	web框架|
|xmltodict|	xml 转 dict|
|SimpleHTTPServer|	简单地HTTP Server,不使用Web框架|
|gevent|	基于协程的Python网络库|
|fabric|	系统管理|
|pandas|	数据处理库|
|scikit-learn|	机器学习库|

例如：读写excel文件
    
1. 安装`esay_install`工具
    sudo apt-get install python-setuptools
2. 安装模块
    sudo easy_install xlrd
    sudo easy_install xlwt        

> 所有内置模块
```
import sys
sys.modules.keys()
```
-----
```
['builtins', 'sys', '_frozen_importlib', '_imp', '_warnings', '_thread', '_weakref', '_frozen_importlib_external', '_io', 'marshal', 'nt', 'winreg', 'zipimport', 'encodings', 'codecs', '_codecs', 'encodings.aliases', 'encodings.utf_8', '_signal', '__main__', 'encodings.latin_1', 'io', 'abc', '_weakrefset', 'site', 'os', 'errno', 'stat', '_stat', 'ntpath', 'genericpath', 'os.path', '_collections_abc', '_sitebuiltins', 'sysconfig', 'idlelib', 'idlelib.run', 'linecache', 'functools', '_functools', 'collections', 'operator', '_operator', 'keyword', 'heapq', '_heapq', 'itertools', 'reprlib', '_collections', 'types', 'collections.abc', 'weakref', 'tokenize', 're', 'enum', 'sre_compile', '_sre', 'sre_parse', 'sre_constants', '_loc
ale', 'copyreg', 'token', 'queue', 'threading', 'time', 'traceback', 'warnings', 'tkinter', '_tkinter', 'tkinter.constants', 'idlelib.autocomplete', 'string', '_string', 'idlelib.autocomplete_w', 'platform', 'subprocess', 'signal', 'msvcrt', '_winapi', 'idlelib.multicall', 'idlelib.config', 'configparser', '_bootlocale', 'encodings.gbk', '_codecs_cn', '_multibytecodec', 'idlelib.hyperparser', 'idlelib.pyparse', 'idlelib.calltips', 'inspect', 'ast', '_ast', 'dis', 'opcode', '_opcode', 'importlib', 'importlib._bootstrap', 'importlib._bootstrap_external', 'importlib.machinery', 'textwrap', 'idlelib.calltip_w', 'idlelib.debugger_r', 'idlelib.debugger', 'bdb', 'fnmatch', 'posixpath', 'idlelib.macosx', 'idlelib.scrolledlist', 'idlelib.windows', 'idlelib.debugobj_r', 'idlelib.rpc', 'pickle', 'struct', '_struct', '_compat_pickle', '_pickle', 'select', 'socket', '_socket', 'selectors', 'math', 'socketserver', 'idlelib.iomenu', 'shlex', 'tempfile', 'shutil', 'zlib', 'bz2', '_compression', '_bz2', 'lzma', '_lzma', 'random', 'hashlib', '_hashlib', '_blake2', '_sha3', 'bisect', '_bisect', '_random', 'locale', 'idlelib.stackviewer', 'idlelib.debugobj', 'idlelib.tree', 'idlelib.zoomheight', 'pydoc', 'importlib.util', 'importlib.abc', 'contextlib', 'pkgutil', 'urllib', 'urllib.parse']
```

内置全局变量：`vars()`
```
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
```

第三方模块：
[anaconda](https://www.anaconda.com/): 数十个常用的第三方模块

> 内建属性

python类的内建属性和方法
```
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```

| 常用专有属性| 说明 |	触发方式 |
|------ | -------|
|`__init__`	|构造初始化函数|	创建实例后,赋值时使用,在__new__后|
|`__new__`	|生成实例所需属性|	创建实例时|
|`__class__`	|实例所在的类|	实例.__class__|
|`__str__`	|实例字符串表示,可读性|	print(类实例),如没实现，使用repr结果|
|`__repr__`	|实例字符串表示,准确性|	类实例 回车 或者 print(repr(类实例))|
|`__del__`	|析构|	del删除实例|
|`__dict__`	|实例自定义属性|	vars(实例.__dict__)|
|`__doc__`	|类文档,子类不继承|	help(类或实例)|
|`__getattribute__`|	属性访问拦截器	|访问实例属性时|
|`__bases__`|	类的所有父类构成元素	|类名.__bases__|

`__getattribute__`例子：

```
class Person(object):
    def __init__(self, subject1):
        self.subject1 = subject1

    # 属性访问时拦截器，打log
    def __getattribute__(self, obj):
        if obj == 'subject1':
            print('log subject1')
        return 'redirect python'

    def show(self):
        print('this is Person')

p = Person("python")
print(p.subject1)
```

> 内建函数

`dir(__builtins__)`
```
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs', 'all', 'any', 'apply', 'basestring', 'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'execfile', 'exit', 'file', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'raw_input', 'reduce', 'reload', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']
```

**range()**

```
range(stop) # 整数列表
range(start, stop[, step]) # 整数列表
```
- strat: 计数从start开始，默认是从0开始。例如：`range(5)`等价于`range(0, 5)`
- stop: 到stop结束，但不包括stop。例如：`range(0, 5)`, 返回`[0, 1, 2, 3, 4]`没有5
- step: 每次跳跃的间距，默认为1。例如：`range(0, 5)`等价于`range(0, 5, 1)`

**map()**

`map`函数会根据提供的函数作为指定序列做映射
```
map(function, sequence[, sequence, ...]) -> list
```

- `function`: 一个函数
- `sequence`: 一个或多个序列，取决于`function`需要几个参数
- 返回值是一个`list`

```
# 函数需要一个参数
map(lambda x: x*x, [1, 2, 3]) # [1, 4, 9]

# 函数需要两个参数
map(lambda x, y: x+y, [1, 2, 3], [4, 5, 6]) # [5, 7, 9]


def f1( x, y ):  
    return (x, y)
l1 = [0, 1, 2, 3, 4, 5, 6]  
l2 = ['Sun', 'M', 'T', 'W', 'T', 'F', 'S']
l3 = map(f1, l1, l2) 
print(list(l3))
# [(0, 'Sun'), (1, 'M'), (2, 'T'), (3, 'W'), (4, 'T'), (5, 'F'), (6, 'S')]
```

**filter()**

`filter()`会对指定序列执行过滤操作
```
filter(function or None, sequence) -> list, tuple, or string
```

- `function`: 接受一个参数，返回布尔值True或False
- `sequence`: 序列可以是`str`,`tuple`, `list`
- 返回值`list`, `tuple`, `string`

```
filter(lambda x: x%2, [1, 2, 3, 4])
[1, 3]

filter(None, "a")
'a'
```

**reduce()**

`reduce`会对参数序列中对元素进行累积

```
reduce(function, sequence[, initial]) -> value
```

function:该函数有两个参数
sequence:序列可以是str，tuple，list
initial:固定初始值

- `function`: 该函数有二个参数
- `sequence`: 序列可以是`str`, `tuple`, `list`
- `initial`: 固定初始值
- 返回`value`

```
reduce(lambda x, y: x+y, [1,2,3,4]) # 10

reduce(lambda x, y: x+y, [1,2,3,4], 5) # 15

reduce(lambda x, y: x+y, ['aa', 'bb', 'cc'], 'dd') # 'ddaabbcc'
```

**sorted()**

```
sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list
```

- `iterable`: 迭代器
- `key`: 函数
- `reverse`: 正序，倒序
- 返回一个新的列表
```
sorted([1, 4, 2, 6, 3, 5]) # [1, 2, 3, 4, 5, 6]

sorted([1, 4, 2, 6, 3, 5], reverse = 1) # 倒序 # [6, 5, 4, 3, 2, 1]

sorted(['dd', 'aa', 'cc', 'bb']) # ['aa', 'bb', 'cc', 'dd']

lst = [3, -19, -1, 28, 7, 0, -2, -5, 7, 8, 0 -3, 9, 0, 11]
sorted(lst, key=lambda x: (x >= 0, -x if x >= 0 else x)) # [-19, -5, -3, -2, -1, 28, 11, 9, 8, 7, 7, 3, 0, 0] ​​​​
sorted(lst, key=lambda x: (x >= 0, -abs(x))) # [-19, -5, -3, -2, -1, 28, 11, 9, 8, 7, 7, 3, 0, 0] ​​​​
```

> 模块中的`__all__`的作用


`__all__`只影响`from <module> import *`这种导入方式

```
__all__ = ['test']

def test():
    print('test')
```

> `包`、`__init__.py`的作用


某个文件夹下具有`__init.py`的，称之为`包`

`__init__.py`作用：

- `package`的标识
- 定义`package`中的`__all__`，用来模糊导入


> 模块的发布和安装

新建一个`setup.py`写入：
```
from distutils.core import setup

setup(name='alogy', version='1.0', description='a', author='alogy', py_modules=['suba.aa']) # suba.aa 包名.模块名
```

发布：
```
> python setup.py build

> python setup.py sdist
```

安装：
```
> python setup.py install
```


> import搜索路径

```
import sys
sys.path # sys.path的先后顺序
```


> 重新导入模块

模块被导入后，`import module`不能重新导入模块，需要重新导入

```
from imp import *
reload('module') # module模块名
```

## 调试

`pdb`是基于命令行的调试工具

> 运行时启动

```
python -m pdb xxx.py
```

`l`: `list` 查看运行的代码
`n`: `next` 往下行执行
`c`: `continue` 继续执行代码直到结束
`b 7`，`b 行数`: `break` 添加断点(通过`c`执行)
`b`: 查看所有断点
`clear 断点序号`: 清除指定断点
`s`: `step` 进入当前作用域中
`p 变量名`: 查看指定变量名的值
`a`: 查看所有当前作用域的变量名和变量值
`q`: `quit` 退出调试
`r`: `return` 快速执行到函数最后一行

> 交互式调试

```
import pdb
pdb.run('testfun(args)') # 此时会打开pdb调试，注意：先使用s跳转到testfun函数中，然后可以使用
```

> 程序里埋点

当程序执行到`pbd.set_trace()`位置时停下来调试
```
import pdb

pdb.set_trace()
```

## 其它

> 给程序传递参数

```
import sys

print(sys.argv) # 接收运行时接受的参数
```



