import types
class Person(object):
	def __init__(self, newName, newAge):
		self.name = newName
		self.age = newAge
	def eat(self):
		print('eat-', self.name)

def run(self):
	print('run-', self.name)

p1 = Person('p1', 24)
p1.eat()

p1.run = types.MethodType(run, p1)
p1.run()

