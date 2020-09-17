"""
 Программа запрашивает у пользователя строку чисел, разделенных пробелом.
 При нажатии Enter должна выводиться сумма чисел.
 Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
 Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
 Но если вместо числа вводится специальный символ, выполнение программы завершается.
 Если специальный символ введен после нескольких чисел,
 то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""
from typing import Tuple


def sum(printed_val: str, sum_value: int) -> Tuple:
    split = printed_val.split(" ")
    for item in split:
        if item.isdigit():
            item = int(item)
        else:
            if len(item) > 1 and item[0] == "-" and item[1:].isdigit():
                item = int(item[1:]) * -1
            else:
                return sum_value, True
        sum_value += item
    return sum_value, False


def main():
    sum_value = 0
    while True:
        print("Введите числа с пробелом, для выхода введите любой символ")
        tuple = sum(input(), sum_value)
        sum_value = tuple[0]
        print(sum_value)
        if tuple[1]:
            break


if __name__ == '__main__':
    main()
