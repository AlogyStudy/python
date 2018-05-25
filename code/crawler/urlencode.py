#conding=utf-8

import urllib.parse

test = {
    'test': '我的'
}

# 通过urllib.urlencode()方法，将字典键值对按URL编码转换，从而能被web服务器接受。
enCodeTest = urllib.parse.urlencode(test)

# 冒号转化为等号
print(enCodeTest) # test=%E6%88%91%E7%9A%84

# 通过urllib.unquote()方法，把 URL编码字符串，转换回原先字符串。
print(urllib.parse.unquote(enCodeTest)) # test=我的
