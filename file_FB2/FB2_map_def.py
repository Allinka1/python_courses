import sys

filename = sys.argv[1]
f = open(filename, 'r')


def make_list_of_numbers(line):
    return line.split()

list_of_numbers = list(map(make_list_of_numbers, f))

f.close()


def push_into_result(item):
    result = []

    fizz_first_number = int(item[0])
    buzz_second_number = int(item[1])
    third_number = int(item[2])

    for element in range(1, third_number + 1):
        if not element % fizz_first_number and not element % buzz_second_number:
            result.append('FB')
        elif not element % fizz_first_number:
            result.append('F')
        elif not element % buzz_second_number:
            result.append('B')
        else:
            result.append(element)
    second_filename = sys.argv[2]
    new_file = open(second_filename, 'a')
    new_file.write(str(result) + '\n')
    new_file.close()

list(map(push_into_result, list_of_numbers))
