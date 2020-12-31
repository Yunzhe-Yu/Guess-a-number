import random

r = random.randint(1,100)
count = 0

while True:
	count += 1 # count = count + 1
	num = input('Please enter a number:')
	num = int(num) #change the datatype
	if num == r:
		print('You win!')
		print('This is your ', count, 'times!')
		break
	elif num < r:
		print('Small!')
	else:
		print('Big!')
	print('This is your ', count, 'times!')
