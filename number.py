import random
r = random.randint(1,10)

while True:
	number = input('Please enter a number you guess:')
	number = int(number)
	if number == r:
		print('You win!')
		break
	else:
		print('You wrong! Please enter it again:')