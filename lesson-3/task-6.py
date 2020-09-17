"""
Реализовать функцию int_func(),
принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
"""


def int_func(string: str) -> str:
    return string.title()


def parse_string(pars_string: str) -> str:
    new_string = ""
    split = pars_string.split(" ")
    for item in split:
        new_string += int_func(item) + " "
    return new_string


string = parse_string(input())
print(string)
