"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
from typing import Type, Dict
from homework.lesson_5.file_util import FileUtil


class FileInfo:
    number_of_strings: int
    number_of_words: Dict[int, int]


def get_file_info(file_name: str) -> Type[FileInfo]:
    file_info = FileInfo
    iter_index = 0
    temp_dict = {}
    with open(file_name, "r", encoding="UTF-8") as file:
        for line in file.readlines():
            split_line = line.split(" ")
            temp_dict[iter_index] = len(split_line)
            iter_index += 1
    file_info.number_of_words = temp_dict
    file_info.number_of_strings = iter_index
    return file_info


list_strings = ["asdfasdf", "", "asfds sdfsadf asdfas", "asdfasdf sadfasdf"]

name = "task_2.txt"
file = FileUtil().generate_file(name, list_strings, "w")

info = get_file_info(name)
print(info.number_of_strings, info.number_of_words)
