number = input('Please enter a number: ')

lenth_number = len(number)

for item in number:
    result = item + ' * 1' + ('0' * (lenth_number - 1))
    lenth_number = lenth_number - 1
    print(result)
