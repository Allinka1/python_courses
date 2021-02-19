
# Задание 1:
# import math
# number = int(input('Please enter a number: '))
# floors = 9
# entrance = 4 
# number_of_apartments_per_floor = 4

# def my_func(number):

# 	appartments_per_entrsnce = number_of_apartments_per_floor * floors
# 	result_entrace = math.ceil(number / appartments_per_entrsnce)
# 	print('Entrance: ' + str(result_entrace))
# 	result_floor = (result_entrace * appartments_per_entrsnce - number) // number_of_apartments_per_floor
# 	print('Floor: ' + str(floors - result_floor))

# my_func(number)

# Задание 2
num = int(input("Please enter an odd positive number: "))
if num < 0 or (num % 2) == 0:
    print('Error!!!')
    exit()

spaces = num - 1
i = 1
while i <= num:
	if not (i % 2) == 0:
		print((' ' * spaces) + (i * "*" ))
		spaces = spaces - 1
	i = i + 1


spaces = spaces + 2
x = num - 1
while x > 0:
	if not (x % 2) == 0:
		print((' ' * spaces) + x * "*")
		spaces = spaces + 1
	x = x - 1
