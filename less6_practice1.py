# 1. Создать словарь оценок предполагаемых студентов 
# # (Ключ - ФИ студента, значение - список оценок студентов). 
# # Найти самого успешного и самого отстающего по среднему баллу.

students = {'Alina':[6, 5, 9], 'Maria':[5, 8, 10], 'Vika':[9, 8, 10], 'Anya':[6, 5, 3]}


list_valuse = (students.values())


def summ_values(item):

    result = sum(item)//len(item)
    return result
    
average_list = list(map(summ_values, list_valuse))


list_keys = (students.keys())

new_students = {}

i = 0

for key in list_keys:
	
	new_students[key] = average_list[i]
	i += 1

print(new_students)

print(max(new_students.items(), key=lambda kv: kv[1]))
print(min(new_students.items(), key=lambda kv: kv[1]))

