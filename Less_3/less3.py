# 1.Каждый пишет сумму списка при помощи for и while

sum = 0
a = [1, 2, 3 ,4 ,5]
for i in a:
 	sum += i
print(sum)


sum = 0
index = 0
l = [1, 2, 3, 4, 5]

list_last_index = len(l)
while index < list_last_index:
    sum += l[index]
    index += 1
print(sum)

# 2.Написать программу, которая выводит сама себя

import sys
filename = sys.argv[1]
f = open(filename, 'r')
for line in f:
	print(line)
f.close()

# 3.Написать программу, которая выводит саму себя задом наперед

filename = sys.argv[1]
f = open(filename, 'r')
for line in f:
	print(line[::-1])
f.close()

# или:

filename = sys.argv[0]
f = open(filename, 'r')
for line in f:
	print(line)
f.close()
