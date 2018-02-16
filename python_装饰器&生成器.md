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
