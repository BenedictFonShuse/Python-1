"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from homework.lesson_5.file_util import FileUtil

util = FileUtil()

file_name = "task_5.txt"

print("Введите числа через пробел")

util.write_to_file(file_name, input(), 'w')

list_string = util.read_file(file_name)


def parse_and_sum_text(list_string: str) -> float:
    for string in list_string:
        split = string.split(" ")
        temp_float = 0.0
        for number in split:
            try:
                temp_float += float(number)
            except TypeError:
                continue
        return temp_float


print(parse_and_sum_text(list_string))
