# Создать структуру данных для студентов из имен и фамилий, можно случайных.
# Придумать структуру данных, чтобы указывать,в какой группе учится студент
# (Группы Python, FrontEnd, FullStack, Java).
# Студент может учиться в нескольких группах.
# Затем вывести:
# студентов, которые учатся в двух и более группах
# студентов, которые не учатся на фронтенде
# студентов, которые изучают Python или Java


dict_students = {
                 'Alina Dymova': {'Python', 'FrontEnd'},
                 'Sergey Ivanov': {'FrontEnd'},
                 'Anton Ivanchin': {'FullStack'},
                 'Victoria Klimenko': {'Python', 'FrontEnd'},
                 'Yulia Sergeeva': {'Java', 'FullStack'},
                 'Maria Klimenova': {'Python', 'FrontEnd', 'FullStack', 'Java'}
                }


def get_key_front(d, value):
    result = []
    for k, v in dict_students.items():
        if value not in v:
            result.append(k)
    return result

students_who_do_not_study_on_the_frontend = get_key_front(dict_students, 'FrontEnd')
print('not Front End: ' + str(students_who_do_not_study_on_the_frontend))


def get_key_2_or_more(d):
    result = []
    for k, v in dict_students.items():
        if len(v) > 1:
            result.append(k)
    return result


students_who_study_in_2_or_more_groups = get_key_2_or_more(dict_students)
print('Two or more groups: ' + str(students_who_study_in_2_or_more_groups))


def get_key_python_java(d):
    list_students = []
    for k, v in dict_students.items():
        if ('Python' in v) or ('Java' in v):
            list_students.append(k)
    return list_students


students_python_or_java = get_key_python_java(dict_students)
print('Python or Java: ' + str(students_python_or_java))