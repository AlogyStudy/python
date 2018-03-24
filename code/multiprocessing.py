# coding=utf-8
# from multiprocessing import Process

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
