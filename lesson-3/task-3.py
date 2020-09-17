"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1: int, arg2: int, arg3: int) -> int:
    if arg1 > arg2:
        if arg2 > arg3:
            return arg1 + arg2
        return arg1 + arg3
    else:
        if arg1 > arg3:
            return arg1 + arg2
        else:
            return arg2 + arg3


print(my_func(1, 2, 3))

