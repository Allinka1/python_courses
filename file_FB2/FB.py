fizz_first_number = int(input('Enter first number: '))
buzz_second_number = int(input('Enter second number: '))
third_number = int(input('Enter third number: '))


for item in range(1, third_number + 1):
    if not item % fizz_first_number and not item % buzz_second_number:
        print('FB')
    elif not item % fizz_first_number:
        print('F')
    elif not item % buzz_second_number:
        print('B')
    else:
        print(item)
