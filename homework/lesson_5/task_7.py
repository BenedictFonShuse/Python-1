"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
from typing import List, Dict
from random import randint
import json

from homework.lesson_5.file_util import FileUtil
from homework.lesson_5.form_of_incorporation_enum import FormOfIncorporation as form


class Firm:
    name: str
    form_of_incorporation: form
    income: int
    expenses: int

    def __str__(self) -> str:
        return str(f"{self.name} {self.form_of_incorporation.name} {self.income} {self.expenses}")


list_of_form_of_incorporation = [form.GUP, form.FKP, form.MUUP, form.DUP, form.DP, form.PK, form.ART, form.SHK, form.PT,
                                 form.TV, form.OOO, form.ODO, form.OAO, form.ZAO, form.FL]


def firm_generator(size: int) -> List[str]:
    temp_list = []
    for i in range(size):
        firm = Firm()
        firm.name = str(f"firm{i}")
        firm.income = randint(10000, 50000)
        firm.expenses = randint(0, 50000)
        firm.form_of_incorporation = list_of_form_of_incorporation[randint(0, len(list_of_form_of_incorporation) - 1)]
        temp_list.append(firm.__str__())
    return temp_list


def text_to_dict(list_string: List[str]) -> Dict[str, int]:
    temp_dict = {}
    for string in list_string:
        string_split = string.split(" ")
        try:
            income = int(string_split[2])
            expenses = int(string_split[3])
            temp_dict[string_split[0]] = income - expenses
        except TypeError:
            continue
    return temp_dict


def dict_to_list(firm_dict: Dict[str, int]) -> List[Dict[str, int]]:
    temp_list = []
    temp_value = 0
    temp_list.append(firm_dict)
    for key, value in firm_dict.items():
        temp_value += value
    temp_list.append({"average_profit": (temp_value / len(firm_dict))})
    return temp_list


util = FileUtil()

file_name = "task_7.txt"
util.generate_file(file_name, firm_generator(10), "w")


list_string = util.read_file(file_name)
firm_dict = text_to_dict(list_string)
to_list = dict_to_list(firm_dict)
print(to_list)

j_data = json.dumps(to_list)

util.generate_file("task_7.json", [j_data], "w")
