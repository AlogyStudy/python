import threading


local = threading.local()

def process_student():
	std = local.student
	print('Hello, %s (in %s)'%(std, threading.current_thread().name))

def process_thread(name):
	local.student = name
	process_student()

t1 = threading.Thread(target=process_thread, args=('xixixi',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('hahaha',), name='Thread-B')

t1.start()
t2.start()
t1.join()
t1.join()
