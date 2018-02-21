## opening and closeing

```
'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines'
```

> 打开

```
open('file', 'modes') # file: 支持相对路径或绝对路径
open('a.txt', 'r')

# modes:
'r'       # 打开只读 (默认) (文件必须存在, 否则会抛出错误)
'w'       # 写入，如果文件存在，将其覆盖，文件不存在，创建新文件
'x'       # 创建一个新文件并打开它以便编写
'a'       # 追加，如果文件存在，内容会被写入到已有内容的后边，文件不存在，则创建新文件
'b'       # 二进制模式
't'       # 文本模式(默认)
'+'       # 打开磁盘文件以进行更新(读写)

# combination:
'rb'      # 以二进制格式打开一个文件，文件指针将会放在文件开头 (默认)
'wb'      # 二进制格式打开写入文件，如果文件存在，将其覆盖，文件不存在，创建新文件
'ab'
# 视频文件, 图片文件, pdf文件, 音频文件 需要带modes中的b
'r+'      # 打开一个文件用于读写
'w+'
'a+'
'rb+'     # 以二进制格式打开一个文件用于读写，文件指针将会放在文件的开头
'wb+'
'ab+'
```

> 关闭

```
f = open()

f.close() # 关闭
```

## reading and writing

> 读

```
f = open()

f.read()
f.read(2) # 参数: 文件读取的字符数
```

> 写

```
f = open()

f.write('write in char') # 参数：写入的字符串

'\n' # 回车换行
'\t' # 横向跳到下一制表符位置
'\r' # 回车
```

## copy

```
f1 = open()

content = f1.read()
name = f1.name
f2 = open(name[:name.rfind('.')] + '.bak')
f2.write(content)

f1.close()
f2.close()
```

## 大文件处理方式

读取大文件的时候，禁止使用`read()`, `readline()`, `readlines()`方法读取.

> 读取小部分内容，多次读取

```
f1 = open()

while True:
    content = f1.read(1024)
    if not content:
        break
```

> with open()

```
# 如果文件是基于行的
with open(...) as f:
    for line in f:
        process(line)
```

> fileinput处理

```
import fileinput
for line in fileinput.input(['xxx.log']):
    print line
```

## 定位读写

`seek()`：指针偏移量
`tell()`: 指针所在位置

```
seek(offset, from)

offset # 偏移量 (指针移动)
from # 方向[0: 文件开头, 1: 当前位置, 2: 文件末尾]
```
-----
```
f = open()

f.seek(2, 0)
f.readline()
f.close()
```

## 文件夹和文件操作

依靠`os`内置模块, 完成系统相关操作

> 文件重命名

```
import os

os.rename('old_name', 'new_name')
```

> 删除文件

```
import os
os.remove('file_name') # file_name 待删除的文件
```

> 创建文件夹

```
import os

os.mkdir('folder') # folder 文件夹名字
```

> 获取当前目录

```
import os

os.getcdw() # 返回当前文件所在的绝对路径
```

> 获取目录列表

```
import os

os.listdir('url') # url 列表路径
os.listdir('./')
```

> 删除文件夹

```
import os

os.rmdir('folder') # folder 待删除的文件夹
```

> 改变默认目录

```
import os

os.chdir('../')

# open() 创建在当前目录下，可以改变默认目录，使创建到其它目录下
```


## 批量重命名


方法1：
注意重命名的路径问题

```
import os

folder_name = input('input name:')

file_names = os.listdir(folder_name)

os.chdir(folder_name) # 跳转至指定目录

for name in file_names:
    _name = name[:name.rfind('.')] + '-tt-' + name[name.rfind('.'):]
    os.rename(name, _name)
```

方法2：

```
import os

folder_name = input('input name:')

file_names = os.listdir(folder_name)

for name in file_names:
    old_file_name = folder_name + '/' + name
    new_file_name = folder_name + '/' + 'haha'
    os.rename(old_file_name, new_file_name)
```
