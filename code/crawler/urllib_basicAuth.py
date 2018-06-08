#conding=utf-8

import urllib.request


user = ''
passwd = ''
proxyserver = ''

# 构建一个密码管理对象，用来保存需要处理的用户名和密码
passwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# 添加账户信息，第一个参数realm是与远程服务器相关的域信息，一般都是写None，后面三个参数分别是 代理服务器、用户名、密码
passwdmgr.add_password(None, proxyserver, user, passwd)

# 构建一个代理基础用户名/密码验证的ProxyBasicAuthHandler处理器对象，参数是创建的密码管理对象
proxy_auth_handler = urllib.request.ProxyDigestAuthHandler(passwdmgr)

# 通过 build_opener()方法使用这些代理Handler对象，创建自定义opener对象，参数包括构建的 proxy_handler 和 proxyauth_handler
opener = urllib.request.build_opener(proxy_auth_handler)

request = urllib.request.Request('http://www.baidu.com/')
response = opener.open(request)

print(response.read().decode())