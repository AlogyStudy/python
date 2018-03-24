import os

ret = os.fork()
print(ret, 'ret')
if ret > 0:
	print("parent - %d"%os.getpid())
else:
	print('children - %d - %d'%(os.getpid(), os.getppid()))


