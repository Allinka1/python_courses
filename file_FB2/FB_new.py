import sys

filename = sys.argv[1]
f = open(filename, 'r')
for line in f:
    list_of_numbers = line.split()

    fizz_first_number = int(list_of_numbers[0])
    buzz_second_number = int(list_of_numbers[1])
    third_number = int(list_of_numbers[2])

    result = []

    for item in range(1, third_number + 1):
        if item % fizz_first_number == 0 and item % buzz_second_number == 0:
            result.append('FB')
        elif item % fizz_first_number == 0:
            result.append('F')
        elif item % buzz_second_number == 0:
            result.append('B')
        else:
            result.append(item)
    print(result)

    second_filename = sys.argv[2] 
    new_file = open(second_filename, 'a')
    new_file.write(str(result) + '\n')
    new_file.close()

f.close()