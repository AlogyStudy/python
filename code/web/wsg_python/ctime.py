
#coding=utf-8
import time


def application(env, start_response):
    status = '200 OK' # 当前状态
    headers = [ # 响应头
        ('Conent-type', 'text/plain')
    ]
    env.get('PATH_INFO')
    env.get('METHOD')
    start_response(status, headers) # 状态和响应头需要通过函数调用参数传递
    return time.ctime() # 响应体 # 只能返回响应体