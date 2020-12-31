import random
r = random.randint(1,10)
times = 0
while True:
	number = input('Please enter a number you guess:')
	number = int(number)
	times = times + 1
	if number == r:
		print('You win! You total use ', times, 'times!')
		break
	elif number < r:
		print('You wrong! Smaller than the answer! This is your ', times, 'times! Please enter it again:')
	else:
		print('You wrong! Bigger than the answer! This is your ', times, 'times! Please enter it again:')