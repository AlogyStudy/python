## 数据结构和算法基础


什么是数据结构和算法：`兵法`，计算的方法。
算法是独立存在的一种解决问题的方法和思想。


算法的特征：
- 输入：算法具有0个或多个输入
- 输出：算法至少有1个或多个输出
- 有穷性：算法在有限的步骤之后会自动结束而不会无限循环，并且每一个步骤可以在可接受的时间内完成
- 确定性：算法中的每一步都有确定的含义，不会出现二义性
- 可行性：算法的每一步都是可行的，也就是说每一步都能执行有限的次数完成


> 时间复杂度和大O表示法


算法的优劣： 实现算法程序的**执行时间**可以反应出算法的效率

时间复杂度：步骤的执行速度(基本执行数量总和) + 程序运行环境（包括硬件和操作系统）

假设存在函数`g`，使得**算法A**处理规模为`n`的问题示例所用时间为`T(n)=O(g(n))`，则称`O(g(n))`为算法A的渐近时间复杂度，简称时间复杂度，记为`T(n)`
`T`: `time`
三个1000次`for`循环: 
`T = 1000 * 1000 * 1000 * 2` -> `T(n) = n ^ 3 * 2` -> `g(n) = n ^ 3`, `T(n) = k * g(n)` -> `T(n) = O(g(n))`


“大O记法”：对于单调的整数函数`f`，如果存在一个整数函数`g`和`实常数c>0`，使得对于充分大的`n`总有`f(n) <= c*g(n)`，就说函数`g`是`f`的一个**渐近函数（忽略常数）**，记为`f(n)=O(g(n))`。
也就是说，在趋向无穷的极限意义下，函数`f`的增长速度受到函数`g`的约束，亦即函数`f`与函数`g`的特征相似。


> 最坏时间复杂度

- 算法完成工作最少需要多少基本操作，即**最优时间复杂度**
- 算法完成工作最多需要多少基本操作，即**最坏时间复杂度**
- 算法完成工作平均需要多少基本操作，即**平均时间复杂度**

最优时间复杂度，其价值不大。
最坏时间复杂度，提供了一种保证，（只要关注，最坏时间复杂度）
平均时间复杂度，是对算法的一个全面评价。

> 时间复杂度的几条基本计算规则

- 基本步骤，即只有常数项，认为其时间复杂度为**O(1)**
- 顺序结构，时间复杂度按**加法**进行计算
- 循环结构，时间复杂度按**乘法**进行计算
- 分支结构，时间复杂度**取最大值**（`if` 或者 `else` 哪个步数最多）
- 判断一个算法的效率时，往往只需要关注**操作数量的最高次项**，其它次要项和常数项可以忽略
- 在没有特殊说明时，所分析的算法的时间复杂度都是指**最坏时间复杂度**

计算方式：
```
# for a in range(0, n):
#     for b in range(0, n):
#         c = 1000 - a - b
#         if a ** 2 + b ** 2 == c **2:
#             print('a, b, c为：%d'%(a, b, c))


# T(1000) = 1000 * 1000 * (1 + 1)
# T(n) = n * n * (1 + max(1, 0))
#  = n ^ 2 * 2
#  = O(n ^ 2)
```


> 常见时间复杂度与大小关系

|执行次数函数|阶|非正式术语|
|: ---:|: ---- :|: --- :|
|12	|O(1)|	常数阶|
|2n+3|	O(n)|	线性阶|
|3n2+2n+1|	O(n2)|	平方阶|
|5log2n+20	|O(logn)	|对数阶|
|2n+3nlog2n+19|	O(nlogn)|	nlogn阶|
|6n3+2n2+3n+4|	O(n3)	|立方阶|
|2n	| O(2n)|	指数阶|

Note: 经常将`log2n`（以2为底的对数）简写成`logn`

![clipboard.png](/img/bV71Ql)

所消耗的时间从小到大:
`O(1) < O(logn) < O(n) < O(nlogn) < O(n2) < O(n3) < O(2n) < O(n!) < O(n^n)`

Note：函数是步骤和执行结构的综合

> Python内置类型性能

`timeit`模块作用：测试一小段`Python`代码代码的执行速度

`class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>)`
`Timer`是测量小段代码执行速度的类。
`stmt`参数是要测试的代码语句（`statment`）；
`setup`参数是运行代码时需要的设置；
`timer`参数是一个定时器函数，与平台有关。

```
#coding=utf-8

from timeit import Timer


def test1():
    li = []
    for i in range(10000):
        li.append(i)

def test2():
    li = []
    for i in range(10000):
        li += [i]

def test3():
    li = [i for i in range(10000)]

def test4():
    li = list(range(10000))

timer1 = Timer('test1()', 'from __main__ import test1')
print('append: ',timer1.timeit(1000)) # 测算次数, 返回值测算时间

timer2 = Timer('test2()', 'from __main__ import test2')
print('+: ',timer1.timeit(1000))

timer3 = Timer('test3()', 'from __main__ import test3')
print('[]: ',timer1.timeit(1000))

timer4 = Timer('test4()', 'from __main__ import test4')
print('list: ',timer1.timeit(1000))
```

`list`内置操作的时间复杂度:

![clipboard.png](/img/bV72bw)

`n`: 列表长度
`k`: 范围

主要：
```
index[] -> O(1)
append -> O(1)
pop(i) -> O(n)
insert(i, item) -> O(n)
contains(in) -> O(n)
```

`dict`内置操作的时间复杂度:

![clipboard.png](/img/bV72cJ)


> 数据结构引入

算法关注在解决问题的步骤和思想上面。

什么是数据结构：数据的组织结构方式,（一组数据如何存储），基本数据类型（`int`， `float`，`char`）的封装


算法与数据结构的区别：
数据结构只是静态的描述了数据元素之间的关系。
高效的程序需要在数据结构的基础上设计和选择算法。

**程序 = 数据结构 + 算法**

总结：算法是为了解决实际问题而设计的，数据结构是算法需要处理的问题载体

最常用的数据运算有五种:

- 插入
- 删除
- 修改
- 查找
- 排序


## 顺序表

> 内存

32位机器：一个`int`, 占四个字节。

**变量**表示起始地址位置

内存的基本信息：
- 单位：字节， `1byte == 8bit`
- 连续的存储空间
- 一个字节表示一个地址单元

> 类型本质

任何变量，函数原则上都是一块块大小各异的内存，而类型则是和系统对这块内存含义的**约定（固定内存块大小的别名）**

决定在内存中占多少个单元

> 基本顺序表与元素外围顺序表

顺序表的基本布局：

![clipboard.png](/img/bV77TX)


数据元素本身连续存储，每个元素所占的存储单元大小固定相同，元素的下标是其逻辑地址，而元素存储的物理地址（实际内存地址）可以通过存储区的起始地址Loc (e0)加上逻辑地址（第i个元素）与存储单元大小（c）的乘积计算而得

所以，访问指定元素时无需从头遍历，通过计算便可获得对应地址，其时间复杂度为O(1)

下标：地址单元的偏移量，才会规定为从0开始。

-----

顺序表的元素外置基本布局：

元素外置在内存中存储地址，地址字节是相同的（可以使用顺序表），而非变化的字节。

![clipboard.png](/img/bV77VI)


> 顺序表的一体式结构与分离式结构

顺序表 = 数据区(`元素集合`) + 表头信息(`容量 + 元素个数`)

容量: 在最初始的时候，就要预估当前规模，一次性向操作系统申请内存地址 （**最大存储多少**）
元素个数：**当前存储多少**

![clipboard.png](/img/bV8b7Q)


顺序表的基本实现方式（表头和数据区如何组合在一起）：
- 一体式结构：
    优点: 一次性申请， 整体性强，易于管理。
    缺点：元素存储区就固定。当数据存储不下的时候，需要整体替换重新向操作系统申请
- 分离式结构：
    优点：元素存储区不固定。 
    缺点：分二次申请，不易管理 

最大区别：分离式其实位置（表头）的地址不变，而一体式，需要整体替换（表头和数据区）都需要重新申请。

![clipboard.png](/img/bV8b9T)

> 顺序表数据区替换与扩充

重新扩充的两种策略：
- 每次扩充增加固定数目的存储位置，如每次扩充增加10个元素位置，这种策略可称为线性增长。
    特点：节省空间，但是扩充操作频繁，操作次数多。
- 每次扩充容量加倍，如每次扩充增加一倍存储空间。
    特点：减少了扩充操作的执行次数，但可能会浪费空间资源。以空间换时间，推荐的方式。

> 顺序表的操作

添加元素:

![clipboard.png](/img/bV8dT6)

尾端加入元素，时间复杂度为`O(1)`
保序的元素加入，时间复杂度为`O(n)`

删除元素:


![clipboard.png](/img/bV8dX7)

删除表尾元素，时间复杂度为`O(1)`
保序的元素删除，时间复杂度为`O(n)`


`Python`中的`list`和`tuple`两种类型采用了顺序表的实现技术.
`list`就是一种采用**分离式技术实现的动态顺序表**

`list`实现采用了如下的策略：在建立空表（或者很小的表）时，系统分配一块能容纳8个元素的存储区；在执行插入操作（`insert`或`append`）时，如果元素存储区满就换一块4倍大的存储区。但如果此时的表已经很大（目前的阀值为`50000`），则改变策略，采用加一倍的方法。引入这种改变策略的方式，是为了避免出现过多空闲的存储位置。

## 单链表

> 为什么需要链表

顺序表缺点：
- 需要预先知道数据大小来申请存储空间
- 进行扩充时需要进行数据的搬迁
- 灵活性低

手拉手的方式（线串）去存储，而非通过元素外置的方式去存储，元素外置需要预先知道数据大小。

线性表：
一维空间的一条线去组织数据，呈线性状态。
- 顺序表：将元素顺序地存放在一块连续的存储区里，元素间的顺序关系由它们的存储顺序自然表示。
- 链表：将元素存放在通过链接构造起来的一系列存储块中。

![clipboard.png](/img/bV8epZ)

原本的数据区，不单单仅仅存储数据，而会增加一个下一个的单元地址


> 单链表的ADT模型

![clipboard.png](/img/bV8evK)

头节点：开始存储的变量
尾节点：往后就是空指针

变量`p`指向链表的头节点（首节点）的位置，从`p`出发能找到表中的任意节点。


单链表的操作:
```
is_empty() 链表是否为空
length() 链表长度
travel() 遍历整个链表
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
search(item) 查找节点是否存在
```

Python中变量标识的本质: 存储地址，引用指向到一个实际数据

> 单链表的实现


```
# coding=utf-8
# single_link_list

class Node(object):
	'''节点'''
	def __init__(self, elem):
		self.elem = elem
		self.next = None

# node = Node(100) # 保存  elem, next

class SingleLinkList(object):
	'''单链表'''
	def __init__(self, node=None):
		self.__head = node # 头节点
	def is_empty(self):
		'''链表是否为空'''
		return self.__head == None

	def length(self):
		'''链表长度'''
		# 游标, 指针
		# cur游标，用来移动遍历节点
		cur = self.__head
		# count记录数量
		count = 0
		while cur != None: # cur.next == None
			count += 1
			cur = cur.next
		return count

	def travel(self):
		'''遍历整个链表'''
		cur = self.__head
		while cur != None:
			print(cur.elem, end=' ')
			cur = cur.next

	def add(self, item):
		'''链表头部添加元素，头插法'''
		node = Node(item)
		node.next = self.__head # 保证链表中的所有关系不打断
		self.__head = node

	def append(self, item):
		'''链表尾部添加元素，尾插法'''
		# item 数据元素
		node = Node(item)
		if self.is_empty():
			self.__head = node
		else:	 
			cur = self.__head
			while cur.next != None: # 从头往后走，然后最后挂载一个新的游标
				cur = cur.next
			cur.next = node

	def insert(self, pos, item):
		'''指定位置添加元素
			:param pos 从0开始
		'''
		if pos < 0:
			self.add(item)
		elif pos > self.length() - 1:
			self.append(item)
		else:
			# pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
			pre = self.__head # pre, prior
			count = 0
			while count < pos - 1:
				count += 1
				pre = pre.next
			# 当循环退出后，pre指向pos-1的位置
			node = Node(item)
			# 先将新节点node的next指向插入位置的节点
			node.next = pre.next
			# 将插入位置的前一个节点的next指向新节点
			pre.next = node
	def remove(self, item):
		'''删除节点'''
		# pre 与 cur 二个游标，需要隔开移动
		cur = self.__head
		pre = None
		while cur != None:
			if cur.elem == item:
				# 如果第一个就是删除的节点
				if cur == self.__head:
				# 判断子节点是否是头节点
					self.__head = cur.next # 将头指针指向头节点的后一个节点
				else:
					# 将删除位置前一个节点的next指向删除位置的后一个节点
					pre.next = cur.next
				break
			else:
				# 继续按链表后移节点
				pre = cur
				cur = cur.next
	def search(self, item):
		'''查找节点是否存在'''
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				return True
			else:
				cur = cur.next
		return False

if __name__ == '__main__':
	sll = SingleLinkList()
	print('is_empty', sll.is_empty())
	print('length', sll.length())
	sll.append(100)
	print('is_empty', sll.is_empty())
	print('length', sll.length())

	sll.append(22)
	sll.add(7)
	sll.append(20)
	sll.insert(2, 777)

	sll.travel()
	sll.remove(7)
	sll.travel()

```

`insert`示意图:

![clipboard.png](/img/bV8tba)

`remove`示意图：

![clipboard.png](/img/bV8Jlb)


后继结点：当前节点的下一个节点


> 单链表与顺序表的对比


链表失去了顺序表随机读取的优点，同时链表由于增加了节点的指针域，空间开销比较大，但对存储空间的使用要相对灵活。

链表与顺序表的各种操作复杂度：

| 操作 	| 链表 	| 顺序表 |
| ----- | ----- | ----- |
| 访问元素 | O(n)	| O(1) |
| 在头部插入/删除 |	O(1)	| O(n) |
| 在尾部插入/删除 |	O(n)	| O(1) |
| 在中间插入/删除 |	O(n)	| O(n) |

链表不能一次性找到位置，都需要通过循环来找到该位置；而顺序表则直接找到位置。


## 双链表

![clipboard.png](/img/bV8KjW)

数据包含：`数据区` + `前驱结点` + `后继结点`

```
# coding=utf-8
# double_link_list

class Node(object):
	'''节点'''
	def __init__(self, elem):
		self.elem = elem
		self.next = None
		self.prev = None

class DoubleLinkList(object):
	"""双链表"""
	def __init__(self, node=None):
		self.__head = node
	def is_empty(self):
		return self.__head is None

	def length(self):
		count = 0
		cur = self.__head
		while cur != None:
			count += 1
			cur = cur.next
		return count
	def travel(self):
		cur = self.__head
		while cur != None:
			print(cur.elem, end=' ')
			cur = cur.next
		print('')
	def add(self, item):
		node = Node(item)
		node.next = self.__head
		self.__head = node
		node.next.prev = node

	def append(self, item):
		node = Node(item)
		cur = self.__head

		if self.is_empty():
			self.__head = node
		else:	
			while cur.next != None:
				cur = cur.next
			cur.next = node
			node.prev = cur 

	def insert(self, pos, item):
		if pos <= 0:
			self.add(item)
		elif pos > (self.length() - 1):
			self.append(item)
		else:
			cur = self.__head
			count = 0
			while count < pos:
				count += 1
				cur = cur.next
			# 当循环退出的时候，cur指针指向的就是pos的位置
			node = Node(item)
			# 将node的prev指向cur
			node.next = cur
			#  将node的next指向cur的下一个节点
			node.prev = cur.prev # 当前节点的上一个，指向到插入节点的前指针
			# 将cur的下一个节点的prev指向node
			cur.prev.next = node
			# 将cur的next指向node
			cur.prev = node

	def remove(self, item):
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				if cur == self.__head:
					self.__head = cur.next
					if cur.next: # 判断双链表是否之后一个节点
						cur.next.prve = None
				else:
					# 将cur的前一个节点的next指向cur的后一个节点
					cur.prev.next = cur.next
					if cur.next:
						# 将cur的后一个节点的prev指向cur的前一个节点
						cur.next.prev = cur.prev
				break
			else:
				cur = cur.next

	def search(self, item):
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				return True
			else:
				cur = cur.next
		return False

if __name__ == '__main__':
	dll = DoubleLinkList()

	print('is_empty', dll.is_empty())
	print('length', dll.length())
	dll.append(100)
	print('is_empty', dll.is_empty())
	print('length', dll.length())

	dll.append(22)
	dll.add(7)
	dll.append(20)
	dll.insert(2, 777)

	dll.travel()
	dll.remove(7)
	dll.travel()
```

## 单项循环链表

![clipboard.png](/img/bV8PKX)

```
# coding=utf-8
# single_cycle_link_list

class Node(object):
    '''节点'''
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.next = 

class SingleCycleLinkList(object):
    '''单链表'''
    def __init__(self, node=None):
        self.__head = node # 头节点
        if node:
            node.next = node

    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        if self.is_empty():
            return 0
        cur = self.__head
        # count记录数量
        count = 1
        while cur.next != self.__head: # cur.next == None
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        pass

    def add(self, item):
        '''链表头部添加元素，头插法'''
        pass

    def append(self, item):
        '''链表尾部添加元素，尾插法'''
        pass

    def insert(self, pos, item):
        '''指定位置添加元素
            :param pos 从0开始
        '''
        pass
    def remove(self, item):
        '''删除节点'''
        pass
    def search(self, item):
        '''查找节点是否存在'''
        pass

if __name__ == '__main__':
    scll = SingleCycleLinkList()

```