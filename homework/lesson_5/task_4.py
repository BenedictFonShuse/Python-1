"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
from typing import Dict, List

from homework.lesson_5.file_util import FileUtil

list_string = ["One — 1", "Two — 2", "Three — 3", "Four — 4"]

format_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

util = FileUtil()
file_name = "task_4.txt"
file = util.generate_file(file_name, list_string, "w")

list_string = util.read_file(file_name)


def format_text(list_strings: str, format_dict: Dict[str, str]) -> List[str]:
    for string in list_strings:
        split = string.split(" ")
        for word in split:
            try:
                var = format_dict[word]
                word = var
            except KeyError:
                continue
    return list_strings


util.generate_file("task_4_1.txt", format_text(list_string, format_dict), "w")
