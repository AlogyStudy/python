## define class

`class`的三个组成部分：

- 类的名称：**类名**
- 类的属性: **一组数据**
- 类的方法：**允许对进行操作的方法(行为)**

> 定义

```
class Student (object):
    pass
```
`class`后面定义类名(类名通常是大写开头的单词)
`(object)`,表示该类是从哪个类继承下来的


> 实例化

创建实例是通过`类名+()`实现
```
stu = Student()
```
-----

```
class Stu (): # 定义class
    age = 10 # 属性
    def show (self): # 方法
        print(self.age) # 类中获取属性
        print(self, 'self')
        print(stu.name) # 获取类外添加属性

stu = Stu() # 实例化

stu.name = 'sf' # 添加属性
stu.show() # 调用方法
```

## self

`self`当前实例化的对象
在定义函数的时候，第一个参数需要`self`

```
class Stu ():
    def show_name (self):
        print(self.name)
        
stu = Stu()
stu.name = 'sf'

stu.show_name()
```

- `self`在定义时需要定义，但是在调用时会自动传入。
- `self`的名字并不是规定写死的，但是最好还是按照约定是`self`。
- `self`总是指调用时的类的实例。

## init

`__init__`: 构造函数(魔法方法)

```
class Stu ():
	# 初始化对象
	def __init__ (self, new_name, new_age):
        self.name = new_name
        self.age = new_age
    def show (self):    
		print('name: %s, age: %d' % (self.name, self.age))

stu = Stu('sf', 23)
stu.show()
```

创建对象的过程：
1. 创建一个对象
2. `Python`解释器会自动的调用`__init__`方法
3. 返回创建的对象的引用，给实例

`__str__`: 实例化执行该方法，返回值。

当需要`print`一个类的时候，需要先在类中定义`__str__`方法，返回值，就是`print()`输出的值

```
class Stu ():
    def __init__ (self, new_name):
        self.name = new_name
    def __str__ (self):    
        return self.name
```


