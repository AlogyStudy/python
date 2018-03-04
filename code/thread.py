from threading import Thread
import time


class My_Thread(Thread):
	def run (self):
		for i in range(3):
			time.sleep(1)
			print(self.name) # name 属性中保存的是当前线程的名字

if __name__ == '__main__':
	t = My_Thread()
	t.start()
