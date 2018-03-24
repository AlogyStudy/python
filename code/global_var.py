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

