"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
from homework.lesson_5.file_util import FileUtil


def add_to_file(file_name: str, add_string: str):
    with open(file_name, "a", encoding="UTF-8") as file:
        file.write(str(f"{add_string}\n"))


while True:
    input_line = input()
    if input_line == "":
        break
    else:
        FileUtil().generate_file("task_1.txt", [input_line], "a")
