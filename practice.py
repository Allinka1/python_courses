import numpy as np
from datetime import datetime, date, time

class Employee:

    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary

    def work(self):
        return('I come to the office')

    def check_salary(self):
        today = date.today()
        first_day_of_month = date(today.year, today.month, 1)
        days = np.busday_count(first_day_of_month, today)
        money = self.salary * days + self.salary
        print(money)

    def compare_salary(self, another_employee):
        if self.salary > another_employee.salary:
            sign = '>'
        elif self.salary < another_employee.salary:
            sign = '<'
        else:
            sign = '='


        return(f'Salary of {self.name} {sign} salary of {another_employee.name}')



class Programmer(Employee):

    def __init__(self, name, email, salary, tech_stack):
        super().__init__(name, email, salary)
        self.tech_stack = tech_stack


    def work(self):
        return(f'{super().work()} and start to coding')

    def __str__(self):
        return(f'Programmer: {self.name}')

    def compare_teches(self, another_employee):

        if len(self.tech_stack) > len(another_employee.tech_stack):
            sign = '>'
        elif len(self.tech_stack) < len(another_employee.tech_stack):
            sign = '<'
        else:
            sign = '='

        return(f'Tech stack of {self.name} {sign} tech stack of {another_employee.name}')

    def alfa_programmer(*args):
        alfa_tech_stack = set()
        for i in args:
            alfa_tech_stack = alfa_tech_stack.union(set(i.tech_stack))
            
        alfa_programmer = Programmer('Alfa', 'alfa@gmail.com', 1000, list(alfa_tech_stack))
        return alfa_programmer

class Recruiter(Employee):

    def work(self):
        return(f'{super().work()} and start to hiring')

    def __str__(self):
        return(f'Recruiter: {self.name}')



employee_1 = Programmer('Alinka', 'ddd@gmail.com', 100, ['Python', 'HTML', 'CSS', 'PostgreSQL'])
employee_2 = Programmer('Masha', 'rrr@gmail.com', 150,  ['Python', 'CSS', 'PostgreSQL'])
employee_3 = Programmer('Nikita', 'lll@gmail.com', 500,  ['Python', 'GitHub'])
employee_4 = Recruiter('Dasha', 'mmm@gmail.com', 100)

# print(date.today().day())
print(employee_3.check_salary())
# print(first.work())
# print(employee_1.__str__())
# print(employee_1.compare_teches(employee_2))
# print(employee_1.alfa_programmer(employee_2))
# alfa = Programmer.alfa_programmer(employee_1, employee_2, employee_3)
# print(alfa.tech_stack)
