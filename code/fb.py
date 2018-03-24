def createNum():
	print('--start')
	a,b = 0,1
	for i in range(5):
		print('--11')
		yield b
		print('--22')
		a,b = b,a+b
		print('--33')
	print('--end')

t = createNum()

#for num in t:
#	print(num)

ret = t.next()
print(ret)

# next(a)
# a.__next__()
