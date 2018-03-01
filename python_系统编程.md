多任务：同一个时间段中，执行多个函数/运行多个程序.

操作系统可以同时运行多个任务:
操作系统轮流让各个任务交替执行，任务1执行0.01秒，切换到任务2，任务2执行0.01秒，再切换到任务3，执行0.01秒……这样反复执行下去。表面上看，每个任务都是交替执行的，但是，由于CPU的执行速度实在是太快了，感觉就像所有任务都在同时执行一样。(时间片轮转)

任务 执行算法：
- 时间片轮转
- 优先级调度
- 调度算法（什么样的情况下按照什么样的规则，让哪个任务执行）

真正的并行执行多任务只能在多核CPU上实现，但是，由于任务数量远远多于CPU的核心数量，所以，操作系统也会自动把很多任务轮流调度到每个核心上执行。

- 进程
- 线程
- 协程

并发：看上去一齐执行（任务数>内核数）
并行：真正一齐执行（内核数>任务数）

程序：编写完毕的代码，在没有运行的时候（一个可执行的代码，可以理解称没有生命）
进程：正在运行的代码（除了包含代码外，还需要运行环境，占用的内存，键盘，显示器等，可以理解称具有生命）

## 进程

> 创建子进程

`os.fork()`创建新的进程，为子进程

```
import os
import time

ret = os.fork() # 返回二个特殊值， 其中一个等于0（子进程），一个不固定的大于0的值（父进程，pid）。都是int类型。

if ret == 0:
while True:
print('1')
time.sleep(1)
else:
while True:
print('2')
time.sleep(1)
```

不一定父进程先执行，或子进程先执行，哪个进程先执行，是依靠操作系统调度算法。

Note: `os.fork()`，只在`Unix/Linux/Mac`上运行，`windows`不可以。

> getpid、getppid

```
import os

ret = os.fork()
print(ret)
if ret > 0:
print('父进程 - %d'%os.getpid())
else:
print('子进程 - %d - %d'%(os.getpid(), os.getppid()))

"""
1535
父进程 - 1534
0
子进程 - 1535 - 1534
"""
```

`os.getpid()`: 子进程的pid的值
`os.getppid()`: 父进程的pid的值

父进程中`fork`的返回值，就是刚刚创建出来的子进程的`pid`

> 父子进程的先后顺序

主进程执行完结束后，子进程没有结束。照样主进程结束掉，而子进程一样执行完程序。

```
import os
import time

ret = os.fork()

if ret == 0:
print('子进程')
time.sleep(5)
print('子进程over')
else:
print('父进程')
time.sleep(3)

print('over')
```
执行结果：
```
父进程
子进程
over
linxingzhangdeMacBook-Air:python linxingzhang$ 子进程over
over
光标定位到当前位置
```

> 全局变量在多个进程中不共享

```
import os
import time

g_num = 100

ret = os.fork()

if ret == 0:
g_num += 1
print('process-c - %d'%g_num)
else:
time.sleep(3)
print('process-p - %d'%g_num)
```
执行结果：
```
process-c - 101
process-p - 100
```
在进程中，全局变量，局部变量，在各自进程的命名空间中，互不干预。
进程和进程之间，数据无法共享。

同一台电脑进程之间通信：管道，消息队列...
不同一台电脑进程之间通信：网络


> 多个fork

第一种：多个`fork`情况，并列`fork`。
```
import os

# 父进程
ret = os.fork()

if ret == 0:
# 子进程
print('1')
else:
# 父进程
print('2')

# 父子进程
ret = os.fork()

if ret == 0:
# 孙子进程
# 2儿子进程
print('11')
else:
# 儿子进程
# 父进程
print('22')
```
执行结果：
```
2
22
1
11
11
22
```

第二种`fork`情况，包含`fork`
```
import os

# 父进程
ret = os.fork()

if ret == 0:
# 子进程
print('1')
else:
# 父进程
print('2')

ret = os.fork()

if ret == 0:
# 2儿子进程
print('11')
else:
# 父进程
print('22')
```
执行结果：
```
2
22
1
11
```

父子进程的执行顺序：
父进程、子进程执行顺序没有规律，完全取决于操作系统的**调度算法**

> Process创建子进程


`multiprocessing`模块是跨平台版本的多进程模块。

```
# coding=utf-8
from multiprocessing import Process
import time

def test():
while True:
print('--test')
time.sleep(2)
ret = Process(target=test)

ret.start() # 子进程执行代码

while True:
print('--mian')
time.sleep(1)
```

```
# coding=utf-8
from multiprocessing import Process
import os

# 子进程执行的代码
def run_proc(name):
print('子进程运行中，name= %s ,pid=%d...' % (name,  .getpid()))

if __name__ == '__main__':
print('父进程 %d.' % os.getpid())
p = Process(target=run_proc, args=('test',))
print('子进程将要执行')
p.start() # 子进程开始
p.join() # 等待进程标记结束后才继续往下走 # 堵塞
print('子进程已结束')

```
执行结果
```
父进程 12826
子进程将要执行
子进程运行中，name= test, pid=12827...
子进程已结束
```

创建子进程时，只需要传入一个执行函数和函数的参数，创建一个`Process`实例，用`start()`方法启动
`join()`方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。


主进程会等待所有的Process子进程先结束，然后再结束主进程。

创建新的进程还能够使用类的方式，可以自定义一个类，继承Process类，每次实例化这个类的时候，就等同于实例化一个进程对象

创建新的进程的另一种方式：`使用自定义类`，继承`Process`类，每次实例化当前自定义类的时候，等同与实例话一个进程对象。

```
from multiprocessing import Process
import time

class New_Process (Process):
# 重写run方法
def run():
while True:
print('11')
time.sleep(1)

p = New_Process()
p.start() # 没有传递target参数，会调用run方法

while True:
print('main')
time.sleep(1)
```
-----
```
from multiprocessing import Process
import time
import os

# 继承Process
class Process_Class (Process):
# 因为Process类本身也有__init__方法，这个子类相当于重写了Process的__init__方法，导致，并没有完全的初始化一个Process类，所以不能子类不能使用继承的方法和属性。
# 解决：将继承类的本身传递给Process.__init__方法，完成这些初始化操作。
def __init__(self, interval):
Process.__init__(self)
self.interval = interval

# 重写Process类的run()方法
def run(self):
print("子进程(%s) 开始执行，父进程为（%s）"%(os.getpid(),os.getppid()))
t_start = time.time()
time.sleep(self.interval)
t_stop = time.time()
print("(%s)执行结束，耗时%0.2f秒"%(os.getpid(),t_stop-t_start))

if __name__ == '__main__':
t_start = time.time()
print("当前程序进程(%s)"%os.getpid())
p1 = Process_Class(2) # 实例化
# 对一个不包含target属性的Process类执行start()方法，就会运行这个类中的run()方法，所以这里会执行p1.run()
p1.start()
p1.join()
t_stop = time.time()
print("(%s)执行结束，耗时%0.2f"%(os.getpid(),t_stop-t_start))
```

> Process语法结构

```
Process([group [, target [, name [, args [, kwargs]]]]])
```

- `target`: 这个进程实例所调用对象
- `args`: 调用对象的位置参数元组
- `kwargs`: 调用对象的关键字参数字典
- `name`: 当前进程实例的别名

Process类常用方法:

`is_alive()`: 判断进程实例是否还在执行
`join([timeout])`: 是否等待进程实例执行结果，或等待多少秒
`start()`: 创建子进程
`run()`: 如果没有给定`target`参数，对这个对象调用`start()`方法时，就执行对象中的`run()`方法
`terminate()`: 不管任务是否完成，立即终止

Process类常用属性：

- `name`: 当前进程的实例别名，默认为`Process-N`, N从1开始递增的整数。
- `pid`: 当前进程的实例`PID`值

```

# coding=utf-8
from multiprocessing import Process
import time
import os

# 两个子进程将会调用的两个方法
def  worker_1(interval):
print("worker_1,父进程(%s),当前进程(%s)"%(os.getppid(),os.getpid()))
t_start = time.time()
time.sleep(interval) # 程序将会被挂起interval秒
t_end = time.time()
print("worker_1,执行时间为'%0.2f'秒"%(t_end - t_start))

def  worker_2(interval):
print("worker_2,父进程(%s),当前进程(%s)"%(os.getppid(),os.getpid()))
t_start = time.time()
time.sleep(interval)
t_end = time.time()
print("worker_2,执行时间为'%0.2f'秒"%(t_end - t_start))

# 输出当前程序的ID
print("进程ID：%s"%os.getpid())

# 创建两个进程对象，target指向这个进程对象要执行的对象名称，
# args后面的元组中，是要传递给worker_1方法的参数，
# 因为worker_1方法就一个interval参数，这里传递一个整数2给它，
# 如果不指定name参数，默认的进程对象名称为Process-N，N为一个递增的整数
p1 = Process(target=worker_1,args=(2,))
p2 = Process(target=worker_2,name="alogy",args=(1,))

# 使用"进程对象名称.start()"来创建并执行一个子进程，
# 这两个进程对象在start后，就会分别去执行worker_1和worker_2方法中的内容
p1.start()
p2.start()

# 同时父进程仍然往下执行，如果p2进程还在执行，将会返回True
print("p2.is_alive=%s"%p2.is_alive())

# 输出p1和p2进程的别名和pid
print("p1.name=%s"%p1.name)
print("p1.pid=%s"%p1.pid)
print("p2.name=%s"%p2.name)
print("p2.pid=%s"%p2.pid)

# join括号中不携带参数，表示父进程在这个位置要等待p1进程执行完成后，
# 再继续执行下面的语句，一般用于进程间的数据同步，如果不写这一句，
# 下面的is_alive判断将会是True，在shell（cmd）里面调用这个程序时
# 因为p2需要2秒以上才可能执行完成，父进程等待1秒很可能不能让p1完全执行完成，
# 所以下面的print会输出True，即p1仍然在执行
p1.join()
print("p1.is_alive=%s"%p1.is_alive())
```
执行结果：
```
进程ID：19866
p2.is_alive=True
p1.name=Process-1
p1.pid=19867
p2.name=alogy
p2.pid=19868
worker_1,父进程(19866),当前进程(19867)
worker_2,父进程(19866),当前进程(19868)
worker_2,执行时间为'1.00'秒
worker_1,执行时间为'2.00'秒
p1.is_alive=False
```

> 进程池

池`Pool`作用：缓冲
进程池优点：增加使用率

创建新的进程的另一种方式：`进程池Pool`

创建一定数量的进程，然后需要使用的时候拿去使用，使用完毕后归还。

```
from multiprocessing import Pool
import random
import time

def worker(num):
for i in range(random.randint(1, 3)):
print('pid = %d, num=%d'%(os.getpid(), num) )
time.sleep(1)

p = Pool(3)

for in range(10):
p.apply_async(worker,(i )) # 向进程池中添加任务
# 如果添加的任务数超过了进程池中的进程个数的话，那么会导致添加不进入到进程池中。
# 添加到进程池中的任务，如果还没有被执行的话，那么会等待进程池中的进程完成一个任务之后，会自动去使用已经结束的进程，完成没有被执行的任务。

p.close() # 关闭进程池，关闭后p实例不再接收新的请求
p.join() # 等待p实例中的所有子进程执行完毕，主进程才会退出， 必须放在close语句之后。
```


