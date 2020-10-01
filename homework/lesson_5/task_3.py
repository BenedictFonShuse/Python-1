"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
import uuid
from random import randint
from typing import List, Dict

from homework.lesson_5.file_util import FileUtil


def employee_list_generator(amount: int) -> List[str]:
    employee_list = []
    for number in range(amount):
        employee_list.append(str(f"{str(uuid.uuid4())} {randint(10000, 100000)}"))
    return employee_list


util = FileUtil()
file_name = "task_3.txt"
file = util.generate_file(file_name, employee_list_generator(20), "w")

list_strings = util.read_file(file_name)


def parse_text_to_dict(list_employee_strings: List[str]) -> Dict[str, int]:
    temp_list = {}
    for string in list_employee_strings:
        split = string.split(" ")
        salary = split[1]
        if salary.isdigit():
            employee_id = split[0]
            temp_list[employee_id] = int(salary)
    return temp_list


def find_employee_by_salary(employee_dict: Dict[str, int], min_salary: int) -> List[str]:
    list_employee_id = []
    for key, value in employee_dict.items():
        if value > min_salary:
            list_employee_id.append(key)
    return list_employee_id


def find_average_salary(employee_dict: Dict[str, int]) -> float:
    temp_value = 0
    for value in employee_dict.values():
        temp_value += value
    return temp_value/len(employee_dict)


to_dict = parse_text_to_dict(list_strings)
print(to_dict)

employee = find_employee_by_salary(to_dict, 20000)
print(employee)

average_salary = find_average_salary(to_dict)
print(average_salary)