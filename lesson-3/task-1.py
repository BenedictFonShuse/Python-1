"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
from numbers import Number
from typing import Union


def own_compartition(numerator: Number, divisor: Number) -> Union[Number, None]:
    """
    Метод деления.
    :param numerator: делимое
    :param divisor: делитель
    :return: результат деления
    """
    if divisor == 0:
        print("Деление на 0 не определено")
        return None
    return numerator / divisor

