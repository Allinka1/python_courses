def zip_func(*my_list):
	zip_list = []
	new_zip_list = []
	len_list = len(my_list)
	min_list = min(my_list, key=len)
	len_min_list = len(min_list)
	for element in my_list:
		i = 0
		while i < len_min_list:
			zip_list.append(element[i])
			i += 1

	i = 0
	for element in zip_list:
		while i < len_min_list:
			new_zip_list.append(tuple(zip_list[i::len(min_list)]))
			i += 1
	return new_zip_list			

print(zip_func([1,5,0,1,2,3], [4,5,6,7,9], [9,1,3,4,6,7,8,], [1,2,2,5,9,1,4]))

