import random

start = input('please enter a startpoint number:')
start = int(start)
end = input('please enter a endpoint number:')
end = int(end)
r = random.randint(start,end)
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
