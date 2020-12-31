import random

r = random.randint(1,100)
while True:
	num = input('Please enter a number:')
	num = int(num) #change the datatype
	if num == r:
		print('You win!')
		break
	elif num < r:
		print('Small!')
	else:
		print('Big!')
