"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
from typing import List

from homework.lesson_5.file_util import FileUtil


class AcademicSubject:
    name: str
    academic_hours: int


util = FileUtil()

list_string = ["Информатика: 100(л) 50(пр) 20(лаб)", "Физика: 30(л) — 10(лаб)", "Физкультура: — 30(пр)"]

file_name = "task_6.txt"

util.generate_file(file_name, list_string, "w")

list_string = util.read_file(file_name)


def parse_txt_to_academic_subjects(list_string: List[str]) -> List[AcademicSubject]:
    academic_subject_list = []
    for string in list_string:
        subject = AcademicSubject()
        hour_sum = 0
        string_split = string.split(":")
        subject.name = string_split[0]
        string_subject_time = string_split[1].strip()
        temp_string = ""
        for char in string_subject_time:
            if char.isdigit():
                temp_string += char
            elif len(temp_string) == 0:
                continue
            else:
                hour_sum += int(temp_string)
                temp_string = ""
        subject.academic_hours = hour_sum
        academic_subject_list.append(subject)
    return academic_subject_list


subjects = parse_txt_to_academic_subjects(list_string)

for subject in subjects:
    print(str(f"{subject.name}: {subject.academic_hours} hours"))
