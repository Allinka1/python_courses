import sys

filename = sys.argv[1]
f = open(filename, 'r')
for line in f:
    list_of_numbers = line.split(';')
    new_list = list_of_numbers[0].split()
    new_list_2 = list_of_numbers[1].split()


    result_average = (sum(list(map(int, new_list)))//len(new_list))
    result_rest = (sum(list(map(int, new_list)))%len(new_list))  
    

    new_list_2_int = list(map(int, new_list_2))

    if result_average == new_list_2_int[0] and result_rest == new_list_2_int[1]:
    	print('True')
    else:
    	print('False')


f.close()