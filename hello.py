# Filename : hello.py
import sys
	
print 'hello world'


i = 5
print i
i = i + 1
print i
s = '''This is a multi-line string.
This is the second line.'''
print s

length = 5
breadth = 2
area = length * breadth
print 'Area is', area
print 'Perimeter is', 2 * (length + breadth)

number = 23
running = True
while running:
	guess = int(raw_input('Enter an integer : '))
	if guess == number:
		print 'Congratulations, you guessed it.'
		running = False # this causes the while loop to stop
	elif guess < number:
		print 'No, it is a little higher than that'
	else:
		print 'No, it is a little lower than that'
else:
	print 'The while loop is over.'
# Do anything else you want to do here
print 'Done'

for i in range(1, 5):
	print i
else:
	print 'The for loop is over'
	
def sayHello():
	print 'Hello World!' # block belonging to the function
sayHello() # call the function
	
def say(message, times = 1):
	'''Prints the maximum of two numbers.
	The two values must be integers.'''
	print message * times
say('World', 5)
print say.__doc__	
	

print 'The command line arguments are:'
for i in sys.argv:
	print i
print '\n\nThe PYTHONPATH is', sys.path, '\n'
	
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print 'I have', len(shoplist),'items to purchase.'
print 'These items are:', # Notice the comma at end of the line
for item in shoplist:
	print item,
print '\nI also have to buy rice.'
shoplist.append('rice')
print 'My shopping list is now', shoplist
print 'I will sort my list now'
shoplist.sort()
print 'Sorted shopping list is', shoplist
print 'The first item I will buy is', shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'I bought the', olditem
print 'My shopping list is now', shoplist	
print 'hello1'
print 'experimental'