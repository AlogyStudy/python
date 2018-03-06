from threading import Thread, Lock
import time


g_num = 0

def test1 ():
	global g_num
	mutex.acquire()
	for i in range(1000000):
		g_num += 1
	mutex.release()
	print('--test--g_num=%d'%g_num)

def test2 ():
	global g_num
	# 轮询
	mutex.acquire()
	for i in range(1000000):
		g_num += 1
	mutex.release()
	print('--test2--g_num=%d'%g_num)

mutex = Lock() # 互斥锁，默认是没有上锁到
# 一方成功上锁，那么另一方会堵塞(一直等待)到这个锁被解开为止

p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test2)
p2.start()


