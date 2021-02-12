# Задание 1
# Написать 2 функции. 
# Первая функция будет принимать строку и приводить ее к нижнему регистру.
# Вторая функция будет принимать строку и проводить ее к верхнему регистру.

# def first(str1):
#   result = str1.upper() 
#   return result


# def second(str2):
#   result = str2.lower() 
#   return result

# # После чего с помощью map применить ваши функции к списку строк. 
# # Отдельно каждую функцию к отдельному списку строк!

# words_lower = ['say', 'hello', 'world', '!']
# words_upper = ['SAY', 'HELLO', 'WORLD', '!']
# any_first = list(map(first, words_lower))
# any_second = list(map(second, words_upper))

# print(any_first)
# print(any_second)

# Задание 2
# Написать функцию которая будет простое число возводить в квардрат.
# Необходимо возвести в квадрат все простые числа в списке используя функцию map

# def function(num):
#     num = int(num)
#     result_element = []


#     for element in range(1, num + 1):
#         if num % element == 0:
#             result_element.append(element)
#     if len(result_element) == 2:
#         return str(num) + ' squared: ' + str(num ** 2)
#     else:
#         return num

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13]
# numbers_num = list(map(function, numbers))
# print(numbers_num)


# Задание 3
# Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк. 
# Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!

# Как я поняла в первый раз:
# word = input()
# summ = 0
# def word_in_text(string):
#     global summ
#     if string == word:
#         summ = summ + 1

# filename = 'english_text.txt'
# file = open(filename).read().split()

# found = list(map(word_in_text, file))

# print(summ)


# Или через список:

# total_count = []
# total_count_if_word_in_text = []

# def word_in_text(word):
# 	global total_count
# 	word = word.lower()
# 	if word in total_count_if_word_in_text:
# 		pass
# 	else:
# 		total = file.count(word)
# 		total_count.append(word + ': ' + str(total))
# 		total_count_if_word_in_text.append(word)


# filename = 'english_text.txt'
# file = open(filename).read().split()

# found = list(map(word_in_text, file))

# print(total_count)

Или через словарь:

total_count = {}

def word_in_text(word):
	global total_count
	word = word.lower()
	total = file.count(word)
	total_count[word] = total


filename = 'english_text.txt'
file = open(filename).read().split()

found = list(map(word_in_text, file))

print(total_count)