# number = int(input('Please enter a number: '))
# if (number % 2):
# 	print('This is NOT an even number!!!')
# else:
# 	print('This is an even number!!!')



# number = int(input('Please enter a number: '))
# if (number % 2 != 0) and not (number % 3) and not (number % 5):
# 	print('This is a number we are searching for :)')
# else:
# 	print('The number is wrong :(')


number = int(input('Please enter a number: '))
for element in range(1, number + 1):
	if number % element == 0:
	   print(element)
