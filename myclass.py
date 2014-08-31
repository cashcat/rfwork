class Person:
	def __init__(self, name):
		self.name = name
	def sayHi(self):
		print 'Hello, my name is', self.name
p = Person('Swaroop')
p.sayHi()
print p

import cPickle as p
#import pickle as p
shoplistfile = 'shoplist.data'
# the name of the file where we will store the object
shoplist = ['apple', 'mango', 'carrot']
# Write to the file
f = file(shoplistfile, 'w')
p.dump(shoplist, f) # dump the object to a file
f.close()
del shoplist # remove the shoplist
# Read back from the storage
f = file(shoplistfile)
storedlist = p.load(f)
print storedlist

listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print listtwo

def make_repeater(n):
        return lambda s: s*n
twice = make_repeater(3)
print twice('word')
print twice(5)
