import random

print('This is a guess number game! You can setting the range of answer')
low = input('You can enter the lowest number in your range:')
low = int(low)
big = input('You can enter the biggest number in your range:')
big = int(big)
r = random.randint(low,big)
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