import sys

filename = sys.argv[1]
f = open(filename, 'r')
for line in f:
    list_of_numbers = line.split(';')
    # print(list_of_numbers)
    new_list = list_of_numbers[0].split()
    print(new_list)


# def my_func(number):
# 	global list_of_numbers
# 	result = []
# 	for number in list_of_numbers:
# 		if number == ";"
# 		break
# 	elif:
# 		number.append(result)

# result_2 = sum(result)//len(result)
# return result_2

    # second_filename = sys.argv[2] 
    # new_file = open(second_filename, 'a')
    # new_file.write(str(result) + '\n')
    # new_file.close()

f.close()