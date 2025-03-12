from random import randrange

def user_number():
	number = input('Give me a number between 0 and 10:')
	return number

def ran_num():
	rand_num = randrange(10)
	return rand_num

def high_or_low(number,rand_num):
	if number >  rand_num:
		print('Too high')
		print('The random number was: ' + str( rand_num))
		print('Your guess was: ' + str(number))
	
	elif number < rand_num:
		print('Too low')
		print('The random number was: ' + str( rand_num))
		print('Your guess was: ' + str(number))

	else: 
		print('The numbers are equal')

x = int(user_number())

high_or_low(x,ran_num())

