## 迭代器

迭代是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象，迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束，迭代器只往前不会往后退。

> 可迭代对象

以直接作用域`for`循环的数据类型：

- 集合数据类型：`list`, `tuple`, `dict`, `set`, `str`
- generator，包括**生成器**和**`yield`的`generator function`**

> 判断是否可以迭代

使用方法`isinstance()`判断一个对象是否具有`Iterable`对象

```
from collections import Iterable

isinstance('abc', Iterable) # true
```

> 迭代器

可以被`next()`函数调用并不断返回下一个值的对象称之为迭代器: `Iterator`

`生成器`, `tuple`
```
from collections import Iterator

isinstance((x for x in range(10)), Iterator) # True
isinstance([], Iterator) # False 列表不是迭代对象
```

`iter()`函数
生成器都是`Iterator`对象， 但是`list`, `dict`, `str`虽然是`Iterable`,却不是`Iterator`

可以把其他类型转成生成器, 使用`iter()`函数


## 闭包

函数是引用

闭包:
```
def test(number):
def test_in(number_in):
print(number_in)
return number + number_in
return test_in

test(10)(20)
```

## 装饰器

对函数或方法起装饰作用

写代码要遵循`开放封闭`原则。
它规定已经实现的功能代码不允许被修改，但可以被扩展。

封闭: 已实现的功能代码块
开放: 对扩展开发

装饰器原理：
```
def a(func):
def inner():
func()
return inner()

def f1():
print('f1')

f1 = a(f1) # 函数名作为变量名，重新赋值使用
f1()
```

装饰器语法糖：
```
def a(func):
def inner():
func()
return inner()

@a
def f1():
print('f1')

f1()
```

> 二个装饰器

```
def makeBold(fn):
def warpped():
print('1')
return '<b>' + fn() + '</b>'
return warpped

def makeItalic(fn):
def warpped():
print('2')
return '<i>' + fn() + '</i>'
return warpped

@makeBold
@makeItalic
def test1():
print('3')
return 'hello world'

ret = test1()
print(ret)

# 输出结果:
# 1
# 2
# 3
# <b><i>hello world</i></b>
```

> 装饰器执行的时间

```
def w1(func):
print('1')
def inner():
print('2')
func()
return inner

def w2(func):
print('4')
def inner():
print('5')
func()
return inner

@w2
@w1
def f1():
print(3)

# 执行f1
f1()
# 1 2 3 # 只有w1 装饰
# 1 4 5 2 3 # w1,w2共同装饰

# 不执行f1
# 1 4
```

> 装饰器对有参数、无参数函数进行装饰


```
def func(funName):
print('1')
def func_in(argA, argB): # 形参
print('2')
funName(argA, argB) # 调用传递参数
return func_in


@func
def test(a, b):
print('a=%d,b=%d'%(a,b))

test(10, 20)
```
以`*args`来解决多参数问题
```
def func(funName):
print('1')
def func_in(*args, **kwargs): # 形参
print('2')
funName(*args, **kwargs) # 调用传递参数
return func_in


@func
def test(a, b):
print('a=%d,b=%d'%(a,b))

test(10, 20)
```

> 装饰器对带有返回值的函数进行装饰

```
def func(funName):
print('1')
def func_in():
print('2')
return funName() # 返回值
return func_in


@func
def test():
return 'test'

ret = test()
print(ret)
```

> 通用装饰器

```
def func(funName):
def func_in(*args, **kwargs):
return funName(*args, **kwargs) # 返回值
return func_in


@func
def test():
return 'test'

ret = test()
print(ret)
```


> 带有参数装饰器

```
from time import ctime, sleep

def timefun_arg(pre="hello"):
def timefun(func):
def warppedfunc():
print('%s called at %s %s'%(func.__name__, ctime(), pre))
return func()
return warppedfunc
return timefun


@timefun_arg('it') # 执行，主动调用。需要多一层闭包函数
def foo():
print('foo')

@timefun_arg('python')
def too():
print('too')

foo()
sleep(2)
too()
```

## 作用域

> globals

查看命名空间中所有全局变量：
`globals()`以字典方式返回

```
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
```

> locals

查看命名空间中局部变量
`locals()`以字典方式返回：
```
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
```

> LEGB规则


Python使用LEGB的顺序来查找一个符号对应的对象

```
locals -> enclosing function -> globals -> builtins
```

`locals`: 当前所在的命名空间(如函数，模块)，函数的参数也属于命名空间内的变量
`enclosing`: 外部嵌套函数的命名空间
`globals`: 全局变量，函数定义所在模块的命名空间
`builtins`: 内建模块的命名空间


查看内建模块的变量：`dir(__builtins__)`
```
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```


## 动态绑定

动态绑定属性：
```
class Person(object):
def __init__(self):
pass

p1 = Person
p1.name = 'pp' # 动态添加属性

print(p1.name)
```


动态绑定方法：
```
import types
class Person(object):
def __init__(self, newName, newAge):
self.name = newName
self.age = newAge
def eat(self):
print('eat-', self.name)

def run(self):
print('run-', self.name)

p1 = Person('p1', 24)
p1.eat()

# 通过types库中的MethodType方法来修改指向函数中的this指针
p1.run = types.MethodType(run, p1) # 动态添加方法

p1.run()
```

绑定静态方法和静态属性：
```
class Person(object):
def __init__(self):
pass



@staticmethod
def test():
print('static method')

Person.test = test # 绑定静态方法
Person.name = 'alogy' # 绑定静态属性

Person.test()
```
绑定类属性：
```
class Person(object):
def __init__(self):
pass


@classmethod
def printNum(cls):
print('class method')

Person.printNum = printNum

Person.printNum()
```

> __slots__

动态语言：可以在运行过程中，修改代码
静态语言：编译时已经确定好代码，运行过程中不能修改

`__slots__`作用：限制实例的属性

```
class Person(object):
__slots__ = ('name', 'age')

p = Person()
p.name = 'alogy'
p.age = 24

```

Note:
`__slots__`定义的属性仅对当前类实例起作用，对继承的子类是不起作用


## 生成器

目标：列表中有大量数据，还不想占用大量内存空间。

生成器特点：保存了一套生成数值的算法。(什么时候需要使用到了，才去生成。)


> 生成器定义方法

方法1:`()`
```
a = (x for x in range(10))
print(a)
```

方法2: `yield`
```
def createNum():
print('--start')
a,b = 0,1
for i in range(5):
print('--11')
yield b
print('--22')
a,b = b,a+b
print('--33')
print('--end')

t = createNum()

for num in t:
print(num)
```
输出结果：
```
--start
--11
1
--22
--33
--11
1
--22
--33
--11
2
--22
--33
--11
3
--22
--33
--11
5
--22
--33
--end
```

`send`方法: 与`yield`的结果配合使用，使得`yield`执行的时候，外部可以传递参数到生成器中。
能够执行`next()`且还可以传递参数

```
def test():
i = 0
while i < 5:
temp = yield i
print(temp)
i += 1

t = test()
print(t.next())
# 0
print(t.next())
# None
# 1
print(t.send('args'))
# args
# 2
```

Note:
`send()`第一次直接调用报错，是参数不知道给那个函数。
报错为：
```
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: can't send non-None value to a just-started generator
```

解决方法：
1. 通过`next()`先调用一次，然后再使用`send()`
2. 第一次调用`send(None)`传递空值进去，后续几次传递该传递的值

> 完成多任务

```
def test1():
while True:
print('test1')
yield None

def test2():
while True:
print('test2')
yield None

t1 = test1()
t2 = test2()

while True:
t1.next()
t2.next()
```

一齐执行`test1()`,`test2()`,`test3()`,三个`while True`同时执行
三个多任务或者三个以上同时执行称之为：`协程`

