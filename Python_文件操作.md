## opening and closeing

```
'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines'
```

> ��

```
open('file', 'modes') # file: ֧�����·�������·��
open('a.txt', 'r')

# modes:
'r'       # ��ֻ�� (Ĭ��) (�ļ��������, ������׳�����)
'w'       # д�룬����ļ����ڣ����串�ǣ��ļ������ڣ��������ļ�
'x'       # ����һ�����ļ��������Ա��д
'a'       # ׷�ӣ�����ļ����ڣ����ݻᱻд�뵽�������ݵĺ�ߣ��ļ������ڣ��򴴽����ļ�
'b'       # ������ģʽ
't'       # �ı�ģʽ(Ĭ��)
'+'       # �򿪴����ļ��Խ��и���(��д)

# combination:
'rb'      # �Զ����Ƹ�ʽ��һ���ļ����ļ�ָ�뽫������ļ���ͷ (Ĭ��)
'wb'      # �����Ƹ�ʽ��д���ļ�������ļ����ڣ����串�ǣ��ļ������ڣ��������ļ�
'ab'
# ��Ƶ�ļ�, ͼƬ�ļ�, pdf�ļ�, ��Ƶ�ļ� ��Ҫ��modes�е�b
'r+'      # ��һ���ļ����ڶ�д
'w+'
'a+'
'rb+'     # �Զ����Ƹ�ʽ��һ���ļ����ڶ�д���ļ�ָ�뽫������ļ��Ŀ�ͷ
'wb+'
'ab+'
```

> �ر�

```
f = open()

f.close() # �ر�
```

## reading and writing

> ��

```
f = open()

f.read()
f.read(2) # ����: �ļ���ȡ���ַ���
```

> д

```
f = open()

f.write('write in char') # ������д����ַ���

'\n' # �س�����
'\t' # ����������һ�Ʊ��λ��
'\r' # �س�
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

## ���ļ�����ʽ

��ȡ���ļ���ʱ�򣬽�ֹʹ��`read()`, `readline()`, `readlines()`������ȡ.

> ��ȡС�������ݣ���ζ�ȡ

```
f1 = open()

while True:
    content = f1.read(1024)
    if not content:
        break
```

> with open()

```
# ����ļ��ǻ����е�
with open(...) as f:
    for line in f:
        process(line)
```

> fileinput����

```
import fileinput
for line in fileinput.input(['xxx.log']):
    print line
```

## ��λ��д

`seek()`��ָ��ƫ����
`tell()`: ָ������λ��

```
seek(offset, from)

offset # ƫ���� (ָ���ƶ�)
from # ����[0: �ļ���ͷ, 1: ��ǰλ��, 2: �ļ�ĩβ]
```
-----
```
f = open()

f.seek(2, 0)
f.readline()
f.close()
```

## �ļ��к��ļ�����

����`os`����ģ��, ���ϵͳ��ز���

> �ļ�������

```
import os

os.rename('old_name', 'new_name')
```

> ɾ���ļ�

```
import os
os.remove('file_name') # file_name ��ɾ�����ļ�
```

> �����ļ���

```
import os

os.mkdir('folder') # folder �ļ�������
```

> ��ȡ��ǰĿ¼

```
import os

os.getcdw() # ���ص�ǰ�ļ����ڵľ���·��
```

> ��ȡĿ¼�б�

```
import os

os.listdir('url') # url �б�·��
os.listdir('./')
```

> ɾ���ļ���

```
import os

os.rmdir('folder') # folder ��ɾ�����ļ���
```

> �ı�Ĭ��Ŀ¼

```
import os

os.chdir('../')

# open() �����ڵ�ǰĿ¼�£����Ըı�Ĭ��Ŀ¼��ʹ����������Ŀ¼��
```


## ����������


����1��
ע����������·������

```
import os

folder_name = input('input name:')

file_names = os.listdir(folder_name)

os.chdir(folder_name) # ��ת��ָ��Ŀ¼

for name in file_names:
    _name = name[:name.rfind('.')] + '-tt-' + name[name.rfind('.'):]
    os.rename(name, _name)
```

����2��

```
import os

folder_name = input('input name:')

file_names = os.listdir(folder_name)

for name in file_names:
    old_file_name = folder_name + '/' + name
    new_file_name = folder_name + '/' + 'haha'
    os.rename(old_file_name, new_file_name)
```
