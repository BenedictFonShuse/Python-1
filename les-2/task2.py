"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""


def turn_close_values(list_values):
    if not isinstance(list_values, list):
        print(f"Объект не list: {list_values} - {type(list_values)}")
        return None
    for number in range(len(list_values)):
        if number % 2 == 0:
            if (2 + number) < len(list_values):
                changed_var = list_values[number]
                list_values[number] = list_values[number + 1]
                list_values[number + 1] = changed_var

    return list_values


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(turn_close_values(test_list))
