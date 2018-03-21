## 网络

> 网络通信

网络: 一种辅助双方或者多方能够连接在一起的工具

网络的目的：就是为了联通多方然后进行通信，即把数据从一方传递给另外一方。


使用网络能够把多方链接在一起，然后可以进行数据传递
网络编程： 让在不同的电脑上的软件能够进行数据传递，即**进程之间的通信**

> TCP/IP协议

TCP/IP协议(协议族)

为了把全世界的所有不同类型的计算机都连接起来，就必须规定一套全球通用的协议。
互联网协议簇(`Internet Protocol Suite`)就是通用协议标准。

因为互联网协议包含了上百种协议标准，但是最重要的两个协议是`TCP`和`IP`协议，所以把互联网协议简称为：`TCP/IP协议`


四层分类：`链路层` -> `网络层` -> `传输层` -> `应用层`
七层分类：`物理层` -> `数据链路层` -> `网络层` -> `传输层` -> `会话层` -> `表示层` -> `应用层`

![clipboard.png](/img/bV5luN)

网际层也称为：网络层
网络接口层也称为：链路层

常用的：`TCP`(模型：电话), `UDP`(模型：写信), `ARP`, `IP`

> 端口

端口:
- 操作系统为了**区分数据给哪个进程**，增加了一个标识**端口**。
- 进出进程的通道

`Pid`与`端口`: 同一台操作系统中，`pid`一定不同，而且可知，但是多台操作系统中，`Pid`不一定能够唯一, 不能够知道其它操作系统的进程的`pid`；而端口在多台操作系统中是唯一的。

端口作用：为了区分多个操作系统下具体是哪个进程。


端口号： 端口是通过端口号来标记的，端口号只有整数，范围是从**0到65535**(在`Linux`系统中，端口可以有**65536（2的16次方）**个。)

端口分类：
- 知名端口
知名端口是众所周知的端口号，范围从0到1023: `80`端口分配给`HTTP`服务。`21`端口分配给`FTP`服务。`22`端口分配给`SSH`服务
- 动态端口
动态端口的范围是从1024到65535。
它一般不固定分配某种服务，而是动态分配。
动态分配是指当一个系统进程或应用程序进程需要网络通信时，它向主机申请一个端口，主机从可用的端口号中分配一个供它使用。
当这个进程关闭时，同时也就释放了所占用的端口号。

查看端口: `netstat -an`

> IP地址

地址: 用来标记地点的

`IP`地址的作用: 用来在网络中标记一台电脑的一串数字，比如`192.168.1.1`，在本地局域网上是唯一的。

`IP`地址的分类：`A类`， `B类`， `C类`， `D类`， `E类`。

每一个`IP`地址包括两部分：**网络地址**和**主机地址**


![clipboard.png](/img/bV5nsH)


**A类IP地址**
第一个字节不变（网络号不变），其它字节可以变化（主机号可变）。
一个A类`IP`地址：1字节的网络地址 + 3字节主机地址组成, 网络地址的最高位必须是“0”

地址范围：`1.0.0.1` - `126.255.255.254`
二进制表示为：`00000001 00000000 00000000 00000001` - `01111110 11111111 11111111 11111110`
A类的可用网络有126个，每个网络能容纳1677214个主机

**B类IP地址**
第一个字节和第二个字节不变（网络号不变），其它字节可以变化（主机号可变）。
一个B类`IP`地址：2个字节的网络地址 + 2个字节的主机地址组成，网络地址的最高位必须是“10”

地址范围：`128.1.0.1` - `191.255.255.254`
二进制表示为：`10000000 00000001 00000000 00000001` - `10111111 11111111 11111111 11111110`
可用的B类网络有16384个，每个网络能容纳65534主机

**C类IP地址**
第一个字节和第二个字节不变,第三个字节（网络号不变），其它字节可以变化（主机号可变）
一个C类`IP`地址：3个字节的网络地址 + 1个字节的主机地址组成，网络地址最高为必须是“110”

地址范围：`192.0.1.1` - `233.255.255.254`
二进制表示为：`11000000 00000000 00000001 00000001` - `11011111 11111111 11111110 11111110`
C类网络可达2097152个，每个网络能容纳254(2^8 - 2[0,255不能使用])个主机

**D类地址**
D类地址用于多点广播

D类`IP`地址第一个字节以`1110`开始，它是一个专门保留的地址。
它并不指向特定的网络，目前这一类地址被用在多点广播（Multicast）中
多点广播地址用来一次寻址一组计算机

地址范围：`224.0.0.1` - `239.255.255.254`

**E类IP地址**
以`1111`开始，为将来使用保留
E类地址保留，仅作实验和开发用


**私有IP**

国际规定有一部分`IP`地址是在局域网中使用，属于私网`IP`，不在公网中使用

```
10.0.0.0 - 10.255.255.255
172.16.0.0 - 172.31.255.255
192.168.0.0 - 192.168.255.255
```

Note:
相同网段:`192.168.1`前面3个字节相同就称之相同网段,即网络号不变就是相同网段

`IP`地址范围：`127.0.0.1` - `127.255.255.255`用于回路测试

`192.168.1.0` => `192.168.1.00000000`: 网络号
`192.168.1.255` => `192.168.1.11111111`: 广播号

## socket

`socket套接字`作用：多台电脑间进程的通信

```
socket.socket(AddressFamily, Type)
```
`Address Family`: 可以选择`AF_INET`（用于Internet进程间通信）或者`AF_UNIX`（用于同一台机器进程间通信），一般使用`AF_INET`
`Type`:套接字类型，可以是`SOCK_STREAM`（流式套接字，主要用于TCP协议）;也可以是`SOCK_DGRAM`(数据报套接字，主要用于UDP协议)

`TCP`通信：
```
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
`UDP`通信：
```
import socket
s = socket.socket(socket.AF_INIT, socket.SOCK_DGRAM)
```

`TCP`通信好处：不会丢失数据，数据可靠。
`TCP`通信坏处：速度慢。

> UDP

`UDP`用户数据报协议，是一个无连接的简单的面向数据报的运输层协议。`UDP`不提供可靠性，它只把应用程序传递`IP`曾的数据报发出去，但是并不能保证数据达到目的地。
由于`UDP`在传输数据报前不用在客户和服务端之间建立一个连接，且没有超时重发等机制，故而传输速度很快。

`UDP`是一种面向无连接的协议，每个数据报都是一个独立的信息，包括完整的源地址或目的地址，它在网络上以任何可能的路径传往目的地，因此是否能达到目的地，到达目的地的地址以及内容的正确性都是不能保证的。


`UDP`特点：

- `UDP`是面向无连接的通讯协议，`UDP`数据报括目的端口号和源端口号信息，由于通讯不需要连接，所以可以实现广播发送。
- `UDP`传输数据时有大小限制，每个被传输的数据报必须限定在64KB之内。
- `UDP`是一个不可靠的协议，发送方所发送的数据报并不一定以相同的次序到达接收方。

`UDP`一般用于**多点通信**和**实时的数据业务**:

- 语音广播
- 视频
- QQ
- TFTP(简单文件传送）
- SNMP（简单网络管理协议）
- RIP（路由信息协议，如报告股票市场，航空信息）
- DNS(域名解释）

> `UDP`发送数据

1. 创建客户端套接字
2. 发送/接收数据
3. 关闭套接字

```
from socket import *


udpSocekt = socket(AF_INET, SOCK_DGRAM)

udpSocket.send(b'msg', '192.168.1.201', 8081)

udpSocket.close()
```

> `UDP`发送、接收数据

```
# coding=utf-8

from socket import *


udpSocket = socket(AF_INET, SOCK_DGRAM)
sendAddr = ('192.168.1.201', 8080)
sendData = input("请输入要发送的数据:")
udpSocket.sendto(sendData, sendAddr)

recvData = udpSocket.recvfrom(1024) # 1024表示本次接收的最大字节数

print(recvData)

# 关闭套接字
udpSocket.close()
```

> 端口问题

运行程序端口号会变化：
每重新运行一次网络程序，端口不一样的原因：数字标识这个网络程序，当重新运行时，如果没有确定到底用哪个，系统默认会随机分配。
这个网络程序在运行的过程中，这个就唯一标识这个程序，所以如果其它电脑上的网络程序如果想要向此程序发送数据，那么就需要向这个数字(即端口)标识的程序发送。

在同一个OS中，端口不允许相同，即如果某个端口已经被使用了，那么在这个端口进程释放该端口之前，其它进程不能使用该端口。


> 绑定信息

一般情况下，一天电脑上运行的网络程序有很多，而各自用端口号很多情况下，为了不育其它的网络程序占用同一个端口好，往往在编程中，`udp`的端口号一般不绑定。

`bind`作用：固定端口和`IP`

socket接收信息:
```
# coding=utf-8

from socket import *


udpSocket = socket(AF_INET, SOCK_DGRAM)
bindAddr = ('', 9001) # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
udpSocket.bind(bindAddr) # 绑定ip和端口号

recvData = udpSocket.recvfrom(1024) # 1024表示本次接收的最大字节数

udpSocket.close()
```

一个`udp`网络程序，可以不绑定，此时操作系统会随机进行分配一个端口，如果重新运行次程序端口可能会发生变化
一个`udp`网络程序，也可以绑定信息（ip地址，端口号），如果绑定成功，那么操作系统用这个端口号来进行区别收到的网络数据是否是此进程的

发送方不需要绑定信息，服务方（接收方）需要绑定信息。
接收和发送，可以同时进行。

网络通信中的工作方式：
- 单工：只能往一个方向发送数据。例如（收音机）
- 半双工：一方在传输，另一方无法进行其它操作，同一时刻，只能执行一方。例如（对讲机）
- 全双工: 二个方向可以同时传输数据。例如（电话）

网络套接字（UDP和TCP）是**全双工**,例如（下载的同时，可以同时上传）


> Python3编码问题

在`socket.sendto()`时`Python3`默认需要字节一样的对象。不能使用`str`类型传递。

发送数据时的解决方法：
```
sendData = 'msg'
# udpSocket.sendto(sendData.encode('utf-8'), (ip, prot))
udpSocket.sendto(sendData.encode('gb2312'), (ip, prot))
```
接收数据时的解决方法：
```
recvData =udpSocket.recvfrom(1024)

content, destInfo = recvData

print('content is %s'%content.decode('gb2312')) # decode() 默认是utf-8
```

> UDP网络通信过程


![clipboard.png](/img/bV5xib)

> echo服务器

echo(回显)服务器: 发送一条数据，返回一条数据。

```
# coding=utf-8

from socket import *


udpSocket = socket(AF_INET, SOCK_DGRAM)

bindAddr = ('', 9001)
udpSocket.bind(bindAddr)

num = 1
while True:
recvData = udpSocket.recvfrom(1024)
udpSocket.sendto(recvData[0], recvData[1]) # 将接收到的数据再发送给对方
print('已经将接收到的第%d个数据返回给对方,内容为:%s'%(num, recvData[0]))
num += 1

udpSocket.close()
```

> udp广播

`TCP`没有广播，即广播只能在`UDP`中使用，`TCP`使用不了。

信息发送到设备上(交换机)，该设备再处理信息到各个目的地。

网络通信中的几种通讯模式:
- 单播： 点对点传输。例如：QQ聊天信息中的个人聊天
- 多播(组播)： 一对多。例如：QQ聊天中群的一个人对群员发送信息
- 广播：一对所有。应用场景例如：QQ上下线

在`UDP`中使用广播，前提需要允许当前套接字发送广播。
```
# 发送广播数据的套接字进行修改设置，否则不能发送广播数据
udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1) # 设置套接字配置
```
固定广播`IP`：`192.168.1.255`或者是`<broadcast>`(尽量使用该方式)

```
#coding=utf-8


import socket, sys

dest = ('<broadcast>', 7788)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 对这个需要发送广播数据的套接字进行修改设置，否则不能发送广播数据
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)

# 以广播的形式发送数据到本网络的所有电脑中
s.sendto("Hi", dest)

print "等待对方回复（按ctrl+c退出）"

while True:
(buf, address) = s.recvfrom(2048)
print "Received from %s: %s" % (address, buf)
```


## tftp文件下载器

`wireshark`流经电脑中的数据，都可以检测到。

`cs架构`：`client`, `server`
`bs架构`：`browser`, `server`

> TFTP协议

TFTP（Trivial File Transfer Protocol,简单文件传输协议）

是`TCP/IP`协议族中的一个用来在客户端与服务器之间进行**简单文件传输**的协议


特点：
- 简单
- 占用资源小
- 适合传递小文件
- 适合在局域网进行传递
- 端口号为`69`
- 基于`UDP`实现

`TFTP`下载过程：

`TFTP`服务器默认监听`69`号端口
当客户端发送"下载"请求（即读请求）时，需要向服务器的`69`端口发送，服务器若批准此请求，则使用一个新的，临时的，端口进行数据传输。

![clipboard.png](/img/bV5zVT)

`TFTP`数据包的格式：

![clipboard.png](/img/bV5Fl6)


确认包`ACK`都需要往随机端口发送数据.
上传和下载往`69`端口发送数据.

`TFTP`操作码：

| 操作码 | 功能 |
|: --- :|: --- :|
|1  |读请求，即下载|
|2    |写请求，即上传|
|3    |表示数据包，即DATA|
|4    |确认码，即ACK|
|5    |错误|

`pack`和`unpack`的使用:

如何知道服务器发送完毕？
标记数据发送完毕：规定当客户端接收到到数据小于`516`字节（2字节操作码 + 2个字节到序号 + 512字节数据）时，意味着服务器发送完毕。

保证一个数字占用2个字节？
使用`struct.pack()`组包
使用`struct.unpack()`解包

组包：
```
sendData = struct.pack("!H8sb5sb",1,"test.jpg",0,"octet",0) # !表示网络数据， H占2个字节，8S占8个字节，b占一个字节。
```
解包：
```
udpSocket = socket(AF_INET, SOCK_DGRAM)
recvData = udpSocket.recvfrom(1024)
cmdTuple = struct.unpack('!HH', recvData[:4]) # 返回值 元组, 第一个元素操作码，第二个元素块编号
```

大端：在CPU中高位存储低位，CPU中低位存储高位
小端：在CPU中低位存储低位，CPU中高位存储高位
例如：`ox11`(高位) `ox22`(低位)
大端存储为：`ox2211`, 小端存储为: `ox1122`

```
from socket import *
import struct

udpSocket = socket(AF_INET, SOCKDGRAM)

# 发送请求数据
senData = struct.pack('!H8sb5sb', 1, 'test.jpg', 0, 'octet',0)
sendAddr = ('192.168.1.201', 8080)
socket.sendTo(senData, senAddr)

# 确认

# 接收数据
recvData = udpSocket.recvfrom(1024)
cmdTuple = struct.unpack('!HH', recvData[:4])
print(cmdTuple)
```

客户端：
```
#coding=utf-8
from socket import *

# 创建socket
tcpClientSocket = socket(AF_INET, SOCK_STREAM)

# 链接服务器
serAddr = ('192.168.1.102', 7788)
tcpClientSocket.connect(serAddr)

while True:
# 提示用户输入数据
sendData = input("send：")

if len(sendData) > 0:
tcpClientSocket.send(sendData)
else:
break

# 接收对方发送过来的数据，最大接收1024个字节
recvData = tcpClientSocket.recv(1024)
print 'recv:',recvData

# 关闭套接字
tcpClientSocket.close()
```
服务端：
```
#coding=utf-8
from socket import *

# 创建socket
tcpSerSocket = socket(AF_INET, SOCK_STREAM)

# 绑定本地信息
address = ('', 7788)
tcpSerSocket.bind(address)

# 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
tcpSerSocket.listen(5)

while True:
# 如果有新的客户端来链接服务器，那么就产生一个信心的套接字专门为这个客户端服务器
# newSocket用来为这个客户端服务
# tcpSerSocket就可以省下来专门等待其他新客户端的链接
newSocket, clientAddr = tcpSerSocket.accept()

while True:
# 接收对方发送过来的数据，最大接收1024个字节
recvData = newSocket.recv(1024)

# 如果接收的数据的长度为0，则意味着客户端关闭了链接
if len(recvData) > 0:
print('recv:', recvData)
else:
break

# 发送一些数据到客户端
sendData = input('send:')
newSocket.send(sendData)

# 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
newSocket.close()

# 关闭监听套接字，只要这个套接字关闭了，就意味着整个程序不能再接收任何新的客户端的连接
tcpSerSocket.close()
```


## TCP

`UDP用户数据包协议`模型中，在通信开始之前，不需要建立相关的链接，值需要发送数据即可，类似生活中的`写信`
`TCP传输控制协议`通信模型中，在通信开始之前，一定要先建立相关的链接，才能发送数据，类似生活中的`打电话`


`TCP协议`特点：
- 稳定
- 慢 (相对于`udp`而言，要慢一些，但是几乎提现微乎其微)
- `web`服务器

`UDP`模型：

![clipboard.png](/img/bV5M5f)

`TCP`模型：

![clipboard.png](/img/bV5Nju)

`socket`创建出来的默认是**主动套接字**（套接字默认是给别人发送信息，而不是等待信息），`listen()`由主动变为被动。（转为被动套接字后，才可以收别人发送的数据）

`TCP`服务端步骤：
1. 买手机: `socket()`
2. 绑定手机卡: `bind()`
3. 设置手机响铃模式: `listen()`
4. 等待别人打电话接听: `accept()`
5. 交流说话：`recv()/send()`接收发送数据

`TCP`客户端步骤：
1. 买手机：`socket()`
2. 拨打电话: `connect()`
3. 交流说话：`recv()/send()`接收发送数据

`newScoket, clientAddr = tcpSocket.accept()`: 返回值是新的套接字(新的客户端)和新客户端的地址与`ip`

`newScoket`作用，去处理当前的请求业务，而主套接字`tcpSocket`，作为继续监听套接字。

`TCP`服务端：
```
#coding=utf-8
from socket import *


tcpSerSocket = socket(AF_INET, SOCK_STREAM)

# 绑定本地信息
address = ('', 7788)
tcpSerSocket.bind(address)

# 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接
tcpSerSocket.listen(5)

# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务器，newSocket用来为这个客户端服务，tcpSerSocket就可以省下来专门等待其他新客户端的链接
newSocket, clientAddr = tcpSerSocket.accept()

# 接收对方发送过来的数据，最大接收1024个字节
recvData = newSocket.recv(1024)
print '接收到的数据为:',recvData

# 发送一些数据到客户端
newSocket.send("thank you !")

# 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
newSocket.close()

# 关闭监听套接字，只要这个套接字关闭了，就意味着整个程序不能再接收任何新的客户端的连接
tcpSerSocket.close()
```

`TCP`客户端：
```
#coding=utf-8
from socket import *

tcpClientSocket = socket(AF_INET, SOCK_STREAM)

# 链接服务器
serAddr = ('192.168.1.102', 7788)
tcpClientSocket.connect(serAddr) # 链接服务器需要耗费时间

sendData = input("请输入要发送的数据：")

tcpClientSocket.send(sendData)

# 接收对方发送过来的数据，最大接收1024个字节
recvData = tcpClientSocket.recv(1024)
print('接收到的数据为: ', recvData)

# 关闭套接字
tcpClientSocket.close()
```

Note:
`TCP`客户端已经链接好了服务器，在以后的数据发送中，不需要填写对方的`ip`和`port`
`UDP`在发送数据的时候，因为没有之前的链接，在每次发送的数据的时候，需要每次填写接收方的`ip`和`port`


模拟QQ聊天：

客户端：

```
from scoket import *


cSocket = socket(AF_INET, SOCK_STREM)

addr = ('192.168.1.201', 8180)
cSocket.connect(addr)

while True:
sendData = input('data: ')

if len(sendData) > 0:
cSocket.send(sendData)
else:
break

# 接收对方发送的数据，最大值1024个字节
recvData = cSocket.recv(1024)

print('return data: %s'%recvData)

cSocket.close()
```

服务端：
```
#coding=utf-8
from socket import *

sSocket = socket(AF_INET, SOCK_STREM)

adder = ('', 8180)
sSocket.bind(adder)
sSocket.listen(5)

while True:
newSocket, clientAddr = sSocket.accept()

while True:
recvData = newSocket.recv(1024)

# 如果接收到客户端发送的数据为0，表示客户端已经下线
if len(recvData) > 0:
print('recv: ', recvData)
else:
break # 退出
newSocket.close() # 关闭新的Socket


sSocket.close()
```
客户端一般绑定`IP`, 服务器一般不写`IP`。

## 网络通信过程

名词：
```
Routers: 路由器
Switches：交换机
Hubs：集线器
Wireless Devices： 无线设备
Connections：连接器
End Devices：终端设备
```

辅助软件: `Cisco Packet Tracer`

> 通过集线器组网

- `hub（集线器）`作用： 能够**完成多个电脑的链接**
- 每个数据包的发送都是以**广播的形式**进行的，容易堵塞网络(任何数据，每次都是以广播形式发送)

不允许一条网线之间有三台或以上的电脑一起链接，会导致数据混乱。需要使用`hub（集线器）`，交换机等设备解决。

网络掩码:
`C`类默认掩码：`255.255.255.0`
`B`类默认掩码：`255.255.0.0`
`A`类默认掩码：`255.0.0.0`
网络掩码必须和`IP`一齐出现，才有作用。

网络掩码作用：网络掩码按位与`IP`地址 => 网络号

网络号相同处于同一个网段，才可以通信。

> 通过交换机组网

网络交换机介绍:
网络交换机(又称“网络交换器”)，是一个扩大网络的器材，能为子网络提供更多的连接端口，以便连接更多的计算机，具有性能比高，高度灵活，相对简单，易于实现等特点。
以太网技术已

交换机的作用：
- 转发过滤：当一个数据帧的目的地址在`MAC`地址表中有映射时，它被转发到连接目的节点的端口而不是所有端口(如该数据帧为广播帧则转发至所有端口)
- 学习功能：以太网交换机了解每一端口相连设备的`MAC`地址，并将地址同相应的端口映射起来存放在交换机缓存中的`MAC`地址表中成为当今最重要的一种局域网组网技术，网络交换机也就成为了最普及的交换机。

Note：

- 如果PC不知目标IP所对应的的MAC，那么可以看出，pc会先发送arp广播，得到对方的MAC然后，在进行数据的传送
- 当switch第一次收到arp广播数据，会把arp广播数据包转发给所有端口（除来源端口）；如果以后还有pc询问此IP的MAC，那么只是向目标的端口进行转发数据

> 交换机和集线器区别

交换机和集线器相同点：
- 完成多台电脑的链接

交换机和集线器不同点：
- 交换机第一次以广播形式确认具体当前是哪台电脑（学习功能），后面都是点对点的发送数据包（转发过滤功能）。（学习之后都是以单播形式传输数据包）
- 集线器不管是第一次还是以后多次，还是对方电脑返回数据包，都是以广播形式发送。（容易造成网络拥堵）


> arp和icmp

网卡有一组序列号：
实际地址/硬件地址/`MAC`地址: 6组数据，每一组数据都是十六进制表示。一共有六个字节。
六个字节分为，前三组（厂商地址），后三组（该厂商生产的网卡序列号）。

![clipboard.png](/img/bV53wM)


`ping 192.168.1.1`使用的是`ICMP`协议
获取`MAC`地址号使用的是`ARP`协议

`ping`之前并不知道对方的`MAC`地址，需要先使用`ARP`协议，然后使用`ICMP`协议。


![clipboard.png](/img/bV53xR)

`OSI Model` 对应七层分类。

七层分类：`物理层` -> `数据链路层` -> `网络层` -> `传输层` -> `会话层` -> `表示层` -> `应用层`


`ICMP`协议作用：`ping `命令使用
`ARP`协议作用：获取`MAC`地址（广播），根据`IP`寻找`MAC`地址
`RARP`协议作用: 根据`MAC`地址寻找`IP`

广播的`MAC`地址: `FFFF.FFFF.FFFF`, `TYPE`：`0x806`

![clipboard.png](/img/bV53DE)

`arp -a`命令：每台`pc`都会有一个`arp`缓存表，用来记录`IP`所对应的的`MAC`。`
`arp -d`命令：删除`arp`缓存表


> 路由器的作用以及组网

路由器，确定一条路径的设备。（假想成十字路口的路标）

功能：
- 链接不同的网络，不同网段之间通信。
- 判断网络地址
- 选择`IP`路径

路由器特点：
- 至少有两个网卡（一个网卡具有一个`IP`地址）
- 两个网卡都是在一个设备上


Note:
- 不在同一网段的pc，需要设置默认网关才能把数据传送过去 通常情况下，都会把路由器默认网关
- 当路由器收到一个其它网段的数据包时，会根据“路由表”来决定，把此数据包发送到哪个端口；路由表的设定有静态和动态方法
- 每经过一次路由器，那么`TTL值`就会减一

路由解析协议：`RIP`


> 网络通信过程的mac地址以及ip的不同

有了`IP`为何需要`MAC`地址：
获取默认网关的`MAC`地址（`rap协议`）


`MAC`地址以及`IP`的不同：
- `MAC`地址，在两个设备之间通信时，在实时变化。
- `IP`地址，在整个通讯过程中，都不变化。


`IP`：标记逻辑上的地址
`MAC`：标记实际转发设备的地址
`netmask网络掩码`: 和`IP`地址一起确定网络号
`默认网关`：发送的`IP`不在同一个网段内，那么会把这个数据转发给，默认网关。(每台电脑，服务器都会配置默认网关)


`route print`: 查看路由表

![clipboard.png](/img/bV56gc)

> pc + switch + router + server


- `DNS`服务器用来解析出`IP`（类似电话簿）
- `DFGATEWAY（默认网关）`用来对顶，当发送的数据包的目的ip不是当前网络时，此数据包包转发的目的`ip`
- 在路由器中路由表指定数据包的”下一跳”的地址


`server(服务器)`: 主机

**访问baidu的过程**:
所有访问都是第一次：
- 先知道默认网关的`MAC`地址:
1. 使用`ARP协议`获取默认网关`MAC`地址
2. 组织数据 发送给默认网关（`IP`还是`DNS`服务器的`IP`,但是`MAC`地址是默认网关的`MAC`地址）
3. 默认网关拥有把转发数据的能力，把数据转发给路由器
4. 路由器根据自己的路由协议，选择一个合适的较快的路径，转发给目的网关（`DNS`所在的网关）
5. 目的网关把数据转发给`DNS`服务器
6. `DNS`服务器查询解析出`www.baidu.com`对应`IP`的地址，并原路返回给请求这个域名的`client`

- 得到`www.baidu.com`对应的`IP`地址之后，会发送`TCP`3次握手，并进行连接。
- 使用`HTTP`发送请求数据给`Web`服务器
- `Web`服务器收到请求数据之后，通过查询自己的服务器得到相应的结果，原路返回给浏览器。
- 浏览器接收到数据之后，通过浏览器自己的渲染功能显示
- 浏览器关闭`TCP`链接,即4次挥手


域名还是`IP`访问: `IP`访问三次握手，然后发送真正请求数据；`域名`访问`DNS`服务器，再然后三次握手，最后发送真正请求数据。

`DHCP协议`：自动分配地址，当前网络的电脑中没有`ip`地址，自动分配。

**DNS服务器**：

作用：解析域名
使用协议：`UDP`

`pc`配置：
默认网关，`DNS`服务器，`IP`地址，网络掩码

![clipboard.png](/img/bV56L8)

![clipboard.png](/img/bV56Mp)

`router`配置：
不同网段`IP`地址(充当默认网关)，多台路由器`IP`

![clipboard.png](/img/bV56Nd)

![clipboard.png](/img/bV56Nk)

`server`配置：
`IP`地址，网络掩码，各种协议配置

![clipboard.png](/img/bV56NN)

![clipboard.png](/img/bV56NW)


> tcp三次握手，四次挥手


![clipboard.png](/img/bV6bPm)

`sequeue num`序列号, `ack num`确认包 等值的变化：

`SYN`: 标记的`TCP`整个包的作用，也就是请求。
`SYN + ACK`: 返回包的的格式
`ACK`: 第二次请求格式

![clipboard.png](/img/bV56VT)

![clipboard.png](/img/bV56V6)

![clipboard.png](/img/bV56Wn)

第二次请求格式，还一并携带的数据包，而后`client`会发送确认数据包,并且`client`会自动关闭套接字，告知服务器。

`PSH + ACK`: 第二次携带数据包格式
`FIN + ACK`: 浏览器套接字关闭发送的包（服务端和客户端各自调用套接字的close都会发送一个包告知对方）

![clipboard.png](/img/bV562q)

![clipboard.png](/img/bV5605)

三次握手作用：建立链接，保存信息。


> TCP十种状态

`netstat -n`: 显示协议统计信息和当前 TCP/IP 网络连接,。
`-n`参数： 以数字形式显示地址和端口号

只要客户端调用`close`,服务器的`recv`的数据长度为0，
过一段时间客户端才会`close`，而服务器收到`TIME_WAIT`的包之后，就关闭`socket`。

![clipboard.png](/img/bV6cp1)

Note:

- 当一端收到一个`FIN`，内核让`read`返回0来通知应用层另一端已经终止了向本端的数据传送
- 发送`FIN`通常是应用层对`socket`进行关闭的结果

> tcp的2MSL问题

![clipboard.png](/img/bV6cxT)

`TTL`: 一个数据包在网络上经过的路由器的最大值，经过路由器的个数。
- 如果路由接收到的`TTL`值是0的话，不会转发当前数据包，会直接扔掉。
- 每经过一个路由减1(从此路过，留下1)

```
UNIX 及类 UNIX 操作系统 ICMP 回显应答的 TTL 字段值为 255
Compaq Tru64 5.0 ICMP 回显应答的 TTL 字段值为 64
微软 Windows NT/2K操作系统 ICMP 回显应答的 TTL 字段值为 128
微软 Windows 95 操作系统 ICMP 回显应答的 TTL 字段值为 32
```

`MSL`: 一个数据包在网络上存储的最长时间（1min-2min）。
`2MSL`：2倍的存活最长时间（2min-4min）。

当第一次关闭，客户端没有`ACK`的时候，过一段时间服务器会再次发送`FIN`，最终收到这个数据包之后，就关闭掉通信。
那边先`close`(不管是`client`还是`server`)就会等待`2MSL`时间。在这个时间中，这个套接字不会被释放，然后重启服务器的时候，导致**绑定失败**。

`2MSL`问题原因：当`TCP`的一端发起主动关闭，在发出最后一个`ACK`包后，即第3次握手完成后发送了第四次握手的`AC`K包后就进入了`TIME_WAIT`状态，必须在此状态上停留两倍的`MSL`时间，等待`2MSL`时间主要目的是怕最后一个`ACK`包对方没收到，那么对方在**超时后将重发第三次握手的`FIN`包**，主动关闭端接到重发的`FIN`包后可以再发一个`ACK`应答包。`TIME_WAI`T状态 时两端的端口不能使用，要等到2MSL时间结束才可继续使用。

导致结果：当连接处于2MSL等待阶段时任何**迟到的报文段都将被丢弃**。

解决方法：可以通过设置`SO_REUSEADDR`选项达到不必等待`2MSL`时间结束再使用此端口。


> 长连接、短连接

`TCP`在真正的读写操作之前，`server`与`client`之间必须建立一个连接，当读写操作完成后，双方不再需要这个连接时它们可以释放这个连接，连接的建立通过三次握手，释放则需要四次握手，所以说每个连接的建立都是需要资源消耗和时间消耗的。

长连接：
一次`TCP`三次握手，发送数据，一直发送数据，最后四次握手关闭。 例如：观看视频
短链接：
`TCP`三次握手，发送数据，四次握手关闭。重新`TCP`三次握手，发送数据，四次握手关闭。如此反复。例如：访问网页

TCP长/短连接的优点和缺点:
- 长连接可以省去较多的`TCP`建立和关闭的操作，减少浪费，节约时间。对于频繁请求资源的客户来说，较适用于长连接。
- 短连接对于服务器来说管理较为简单，存在的连接都是有用的连接，不需要额外的控制手段。但如果客户请求频繁，将在`TCP`的建立和关闭操作上浪费时间和带宽。
- `client`与`server`之间的连接如果一直不关闭的话，会存在一个问题，随着客户端连接越来越多，`server`早晚有扛不住的时候，这时候`server`端需要采取一些策略，如关闭一些长时间没有读写事件发生的连接，这样可以避免一些恶意连接导致`server`端服务受损；如果条件再允许就可以以客户端机器为颗粒度，限制每个客户端的最大长连接数，这样可以完全避免某个的客户端连累后端服务。


`TCP`长/短连接的应用场景：
- 长连接多用于操作频繁，点对点的通讯，而且连接数不能太多情况。每个`TCP`连接都需要三次握手，这需要时间，如果每个操作都是先连接，再操作的话那么处理速度会降低很多，所以每个操作完后都不断开，再次处理时直接发送数据包就OK了，不用建立`TCP`连接。例如：数据库的连接用长连接，如果用短连接频繁的通信会造成`socket`错误，而且频繁的`socket` 创建也是对资源的浪费。
- 而像`WEB`网站的`http`服务一般都用短链接，因为长连接对于服务端来说会耗费一定的资源，而像`WEB`网站这么频繁的成千上万甚至上亿客户端的连接用短连接会更省一些资源，如果用长连接，而且同时有成千上万的用户，如果每个用户都占用一个连接的话，那可想而知吧。所以并发量大，但每个用户无需频繁操作情况下需用短连好。


> listen的队列长度


`listen`参数问题: 首次一次达到该设置参数数值，后面关闭之后，已连接队列扔出一个，才能继续进行，再从半连接队列到已连接队列中。

```
tcpSerSocket.listen(connNum)
# connNum表示，半链接和已链接次数的总长度
# 在Linux中不管写多少，都是系统会自己计算该值
# Mac电脑系统上，用户写多少就是多少。
```
![clipboard.png](/img/bV6dJD)


服务端：
```

#coding=utf-8
from socket import *
from time import sleep

# 创建socket
tcpSerSocket = socket(AF_INET, SOCK_STREAM)

# 绑定本地信息
address = ('', 7788)
tcpSerSocket.bind(address)

connNum = int(raw_input("请输入要最大的链接数:"))

# 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
tcpSerSocket.listen(connNum)

# 在这个期间，如果有20个客户端调用了connect链接服务器，那么这个服务器的Linux底层，会自动维护2个队列（半链接和已链接）
# 其中，半链接和已链接的总数为linsten中的值，如果这个值是5,那么，意味着此时最多只有5个客户端能够链接成功，而剩下15则会堵塞在connect函数
for i in range(10):
print(i)
sleep(1)

while True:

# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务器
newSocket, clientAddr = tcpSerSocket.accept() # 如果服务器调用了accept，那么Linux底层中的那个半链接和已链接中的总数就减少了一个，因此，此时的15个因为connect堵塞的客户端又会在进行连接 来争抢1个刚空出来的空位。
print clientAddr
sleep(1)
```
客户端：
```
#coding=utf-8
from socket import *

connNum = raw_input("请输入要链接服务器的次数:")
for i in range(int(connNum)):
s = socket(AF_INET, SOCK_STREAM)
s.connect(("192.168.1.102", 7788))
print(i)
```

Note:

- `listen`中的`black`表示已经建立链接和半链接的总数
- 如果当前已建立链接数和半链接数以达到设定值，那么新客户端就不会`connect`成功，而是等待服务器

> 手动配置ip

设置IP和掩码:
```
ifconfig eth0 192.168.5.40 netmask 255.255.255.0
```
设置网关:
```
route add default gw 192.168.5.1
```

> 常见网络攻击


**tcp半链接攻击**

`tcp`半链接攻击（`SYN Flood (SYN洪水)`）：是种典型的`DoS` (`Denial of Service，拒绝服务`) 攻击

导致结果：服务器`TCP`连接资源耗尽，停止响应正常的`TCP`连接请求。

三次链接的第一次就是半链接


**dns攻击**

`dns`使用的是`udp`协议，不稳定.

`dns`服务器被劫持:
需要攻击`dns`服务器，或者和`dns`服务器合作。
一个域名服务器对其区域内的用户解析请求负责，但是并没有一个机制去监督它有没有认真地负责。 有些被攻击`dns`服务器故意更改一些域名的解析结果，将用户引导向一个错误的目标地址。
用来阻止用户反问某些特定的网站，后者是将用户引导到广告页面，或者构造钓鱼网站，获取用户信息。

`dns`欺骗：
主动用一个假的`dns`应答来欺骗用户计算机，让其相信这个假的地址，并且抛弃真正的`dns`应答。

导致用户访问假的目的地址。


**查看域名解析的ip地址方法**

```
nslookup 域名

# 例如
nslookup baidu.com

```

![clipboard.png](/img/bV6fbl)


**arp攻击**

修改电脑的`mac`地址，使用中间人攻击。

![clipboard.png](/img/bV6fbI)

> NAT

`NAT`: 网络地址转换器

家庭上网:
电话线 -> 调制解调器（猫） -> 路由器 -> 电脑,手机

从`调制解调器`中出来的`IP`才可以访问到外网。


`LAN`口: 局域网
`WAN`口: 万维网

![clipboard.png](/img/bV6fmj)

路由器存在一张表，一个本地电脑和路由器对应到标识。

路由器功能：`代理`
本地电脑不能访问，路由器把不能访问的地址扔掉。


## 并发服务器

> 单进程服务器

简单单进程`TCP`服务器：

```
from socket import *

serSocket = socket(AF_INET, SOCK_STREAM)

# 重复使用绑定的信息
serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR  , 1)
# 作用：服务器先四次挥手到第一次，最终也等待2MSL时间。 服务器先结束，而且立即运行服务器，就不会出现

localAddr = ('', 7788)

serSocket.bind(localAddr)

serSocket.listen(5)

while True:
print('主进程，等待新客户端的到来')
newSocket, destAddr = serSocket.accept()
print('主进程，接下来负责数据处理[%s]'%str(destAddr))

try:
while True:
recvData = newSocket.recv(1024)
if len(recvData) > 0:
print('recv[%s]:%s'%(str(destAddr), recvData))
else:
print('[%s]客户端已经关闭'%str(destAddr))
break
finally:
newSocket.close() # 服务器主动关闭

serSocket.close()
```


> 关闭监听套接字、已连接套接字的不同


关闭监听套接字，意味着：不能再连接新的客户端连接。
已连接套接字关闭，意味着：当前套接字不能再使用`send`和`recv`来收发数据。




