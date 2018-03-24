# from multiprocessing import Pool
from multiprocessing import Pool

def worker (num):
	print(1111, 'num: %d'%num )

p = Pool(3)

for i in 5:
	p.apply_async(worker, i)

p.close()
p.join()

