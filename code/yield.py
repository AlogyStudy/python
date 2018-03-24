def test1():
	while True:
		print('test1')
		yield None

def test2():
	while True:
		print('test2')
		yield None

t1 = test1()
t2 = test2()

while True:
	t1.next()
	t2.next()
