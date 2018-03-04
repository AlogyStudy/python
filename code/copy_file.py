#coding=utf-8
from multiprocessing import Pool, Manager
import os

def copy_task (name, old_file, new_file, queue):
	print(old_file + '/' + name)
	fr = open(old_file + '/' + name)
	fw = open(new_file + '/' + name, 'w')

	con = fr.read()
	fw.write(con)	

	fr.close()
	fw.close()
	
	queue.put(name)	

def main ():
	old_file = input('文件夹名字:')
	new_file = old_file + '_附件'
	os.mkdir(new_file)
	file_names = os.listdir(old_file)

	pool = Pool(5)
	queue = Manager().Queue()
	
	for file in file_names:
		pool.apply_async(copy_task, args=(file,  old_file, new_file, queue))
	
	num = 0
	all_num = len(file_names)
	while num < all_num:
		queue.get()
		num += 1
		copy_rate = num / all_num
		print('\rcopy进度是:%.2f%%'%(copy_rate * 100), end='')
				
	print('\n完成copy')

if __name__ == '__main__':
	main()
