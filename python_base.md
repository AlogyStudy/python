## Run

> 源代码

`Python`源代码的文件以"py"为扩展名，由`Python`程序解释，不需要编译

命令：`python 文件`

> 字节代码

`Python`源文件经过编译后生成的扩展名为"pyc"的文件
编译方法：
```
import py_compile
py_compile.compile("url") # url编译的文件的路径
```

编译后的文件为：`xxx.cpython-36.pyc`

> 优化代码

经过优化的源文件，扩展名为".pyo"
命令：`pyhont -O -m py_comile 编译的文件`

编译后的文件为：`xxx.cpython-36.opt-1.pyc`

## Type

```
int, float, str, bool, NoneType

tuple, list, dict, set
```

## Lists

```
list = []
list[i:j]  # 返回列表的子集
list[-1]   # 访问的最后一个元素
list[:-1]  # 只返回最后一个元素

list[i] = val
list[i:j] = otherlist  # replace ith to jth element with otherlist
del list[i:j]

list.append(item)
list.extend(list)
list.insert(0, item)
list.pop()
list.remove(i)
list1 + list2     # 结合两个列表
set(list)         # 从列表中删除重复元素

list.reverse()
list.count(item)
sum(list)

list.sort()

zip(list1, list2)
sorted(list)
",".join(list)
```


## Dict

```
dict.keys()
dict.values()
"key" in dict
dict["key"]   # throws KeyError
dict.get("key")
dict.setdefault("key", 1)
```

## Iteration

```
for item in ["a", "b", "c"]:
for i in range(4):     # 0 到 3
for i in range(4, 8):  # 4 到 7
for key, val in dict.items():
```

## String

```
str[0:4]
len(str)

string.replace("-", " ")
",".join(list)
"hi {0}".format('j')
str.find(",")
str.index(",") 
str.count(",")
str.split(",")

str.lower()
str.upper()
str.title()

str.lstrip()
str.rstrip()
str.strip()

str.islower()

len() # 求序列长度
+ # 连接2个序列
* # 重复序列元素
in # 判断元素是否在序列中
max() # 返回最大值
min() # 返回最小值
```

## Casting

```
int(str)
float(str)
str(int)
str(float)
bool(1)
```

## Comprehensions

```
[fn(i) for i in list]            # .map
map(fn, list)                    # .map, 返回的迭代

filter(fn, list)                 # .filter, 返回的迭代
[fn(i) for i in list if i > 0]   # .filter.map
```

## Regex

```
import re

re.match(r'^[aeiou]', str)
re.sub(r'^[aeiou]', '?', str)
re.sub(r'(xyz)', r'\1', str)

expr = re.compile(r'^...$')
expr.match(...)
expr.sub(...)
```

## Function

> 定义函数

使用关键字:`def`。 依次写出`函数名`, `括号`, `参数`, `语句结束符 :`。然后，在缩进块中编写函数体，函数的返回值用`return`语句返回

```
def my_abs (x):
    if x >= 0:
        return x
    else:
        return -x    
```

> 空函数

定义一个什么也不做的空函数，使用`pass`语句

```
def nop ()
    pass
```

空函数的作用：提供占位符


> 参数

默认参数一定要用不可变对象(基本变量类型和`tuple`), 如果是可变对象，程序运行时会有逻辑错误。


定义可变参数和关键字参数的使用：
- `*args`是可变参数，`args`接收的是一个`tuple`
- `**kw`是关键字参数，`kw`接收的是一个`dict`

调用函数时如何传入可变参数和关键字参数：
- 可变参数既可以直接传入：`func(1, 2, 3)`，又可以先组装`list`或`tuple`，再通过`*args`传入：`func(*(1, 2, 3))`；
- 关键字参数既可以直接传入：`func(a=1, b=2)`，又可以先组装`dict`，再通过`**kw`传入：`func(**{'a': 1, 'b': 2})`。


使用`*args`和`**kw`是`Python`的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数作用：为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符`*`，否则定义的将是位置参数


> 返回值


函数执行完毕也没有`return`语句时，自动`return None`
函数可以**同时返回多个值**，但其实就是一个`tuple`


> 匿名函数

`lamdba 参数:函数体`

匿名函数自动具有返回值


## Characteristic

1. 区分大小写
2. 语句结尾使用`:`
3. `Tab`符


> if的各种假

Flase: `''`, `None`, `0`, `[]`, `{}`, `Flase`

> `==`与`is`

`is`是比较两个**引用**是否指向了**同一个对象**(引用比较)
`==`是比较两个对象是否相等

```
a = 2
b = 2

a is b # True, 为True的原因是[-5, 256]

c = 500
d = 500
c is d # False
```
`python`解释器为了优化速度，会把`[-5, 256]`之间的数据提前存放到小整数对象池中，程序中要使用到`[-5, 256]`之间范围的数据，就不会重新创建一份，都是指向对象池中的同一份数据，除了这个区间之外的数据，每次使用时解释器都会重新申请一块内存，用来存储数据。


> 深拷贝和浅拷贝


浅拷贝：对于一个对象的顶层拷贝(拷贝了引用，并没有拷贝内容)
深拷贝：重新申请内存存储复制的数据.

```
import copy
a = [1, 2, 3]

b = a # 浅拷贝
c = copy.deepcopy(a) # 深拷贝
```

区别`copy`和`deepcopy`:
`deepcopy`：所有的内容都重新申请内存，依次拷贝
`copy`: 外层重新申请内存


拷贝元组的特点：
都是相同引用地址(元组是不可变类型,拷贝之后还是相同地址)



