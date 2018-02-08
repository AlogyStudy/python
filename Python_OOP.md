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

魔法方法:
```
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```

`__init__`: 类构造方法(魔法方法)

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

`__new__`: 方法主要是当继承一些不可变的`class`时(比如int, str, tuple), 提供一个自定义这些类的实例化过程.

```
class Stu(object):
    def __new__(cls):
        return object.__new__(cls) # 自定义实例化过程
        # 自身没有能力创建实例,可以让父类创建
    def __init__(self):
        print('init')
stu = Stu()
```

> 创建单例对象

```
class Single(object):
    __instance = None
    def __new__(cls):
        if cls.__instance != None:
            return cls.__instance
        else:
            cls.__instance = object.__new__(cls)
            return cls.__instance

s1 = Single()
s2 = Single()
```

## 私有方法和私有属性

> 私有属性

按照约定俗成的规定`__`开头的属性表示**私有属性**, 不可以直接`类名.变量名`访问
在类中存储的形式为：`_Stu__age`, `_类名__变量名`

```
class Stu():
    def __init__(self, new_name):
        self.name = new_name
        self.__age = 0 # 定义了一个私有的属性，属性的名字是`__age`
```

在类中访问形式:`self.__变量名`


> 私有方法(private)

按照约定俗成的规定`__`开头的属性表示**私有方法**, 不可以直接`类名.方法名`访问
存储的形式为：`_Stu__get_age`, `_类名__方法名`

```
class Stu():
    def __test(self): # 定义私有方法
        pass
```

在类中调用私有方法:`self.__方法名()`


有些时候，会看到以一个下划线开头的实例变量名，比如`_name`，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。


> __del__

`__del__`:  当删除一个对象时，`python`解释器会默认调用一个魔术方法，`__del__()`

```
class Stu():
    def __del__ (self):
        print('remove obj')

stu = Stu()
del stu
```

在类的生命周期中，如果类销毁了，`python`会自动调用`__del__`方法。也就是说,不管是手动调用`del`还是由`python`自动回收都会触发`__del__`方法执行。


> 对象引用个数

模块`sys`中有一个`getrefcount`方法可以测试对象的引用个数
返回的结果，会比实际结果大`1`.

```
import sys

sys.getrefcount('变量/方法')
```

## 继承

```
class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal): # 继承
    def run(self):
        print('Dog is running')

class Cat(Animal):
    pass


dog = Dog()
cat = Cat()

dog.run()
cat.run()
```

当子类和父类都存在相同的`run()`方法时，子类的`run()`覆盖了父类的`run()`,在代码运行的时候，总是会调用子类的`run()` -- 多态

> 重写

重写父类的方法,继承之后,子类定义和父类方法名一样的方法

```
class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self): # 重写
        print('Dog is running')

class Cat(Animal):
    pass


dog = Dog()
cat = Cat()

dog.run()
cat.run()
```

> 调用父类方法

- 类名调用
- `super`关键字调用

```
class Animal():
    def run(self):
        print('Animal is running')
class Dog (Animal):
    def say(self):
        #  第一种，类名调用。
        # Animal.run(self) #方法必须传递参数`self`
        
        # 第二种，super关键字
        super().run()
        print('Gog is running')
 
dog = Dog()
dog.say()        
```


私有方法，私有属性在继承中的表现:

- 私有方法并不会被继承(子类外和子类内都不会让使用)
- 私有属性并不会被继承(子类外和子类内都不会让使用)


> 多继承


子类具有多个父类

```
class A(object): # object是所有最终类的终点
    def test(self):
        print('A')
class B:
    def test(self):
        print('B')

class C(A, B): # 多继承 (如果继承类中方法名或者属性名相同，生效的是参数先后顺序，`类名.__mro__`中的顺序)
    pass

print(C.__mro__) 
# (<class '__main__.A'>, <class '__main__.Base'>, <class '__main__.T'>, <class 'object'>) 
# C3算法

c = C() # 子类也会重写父类的方法
```

## 多态

定义时的类型和运行时的类型不一样。

执行的时候确定

```
class D(object):
    def _print(self):
        print('D')
class X(D):
    def _print(self):
        print('X')

def introduce(temp):
    temp._print()

d = D()
x = X()

introduce(d)
introduce(x)
```

`isinstance()`判断一个对象是否是某种类型

实例属性属于各个实例所有，互不干扰；
类属性属于类所有，所有实例共享一个属性；
不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。


> 类属性 & 实例属性

```
class A():
    num = 1 # 类属性
    def __init(self):
        print(self.num)

a = A()
a.name = 100 # 实例属性

print(A.num) # 获取类属性
```

> 实例方法 & 类方法 & 静态方法

```
class A():
    # 定义类方法
    @classmethod
    def add_num(cls): # 保存类的引用
        pass
    def get_num(self): # 实例方法
        pass
    @staticmethod
    def set_num(): # 静态方法 # 可以没有任何参数引用
        pass

a = A()
A.add_num() # 调用类方法
# a.add_num() # 实例调用类方法

A.set_num() # 调用静态方法
a.set_num() # 实例调用静态方法
```


