"""
 Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
 У пользователя необходимо запрашивать новый элемент рейтинга.
 Если в рейтинге существуют элементы с одинаковыми значениями,
 то новый элемент с тем же значением должен разместиться после них.
"""

base_rating = [7, 5, 3, 3, 2]


def add_rating_value(rating, value):
    if rating[0] <= value:
        new_rating = [value]
        new_rating.extend(rating)
        return new_rating
    elif rating[len(rating) - 1] >= value:
        rating.append(value)
        return rating
    else:
        return private_add_rating_value(rating, value, len(rating) // 2)


def private_add_rating_value(rating, value, recursion_var):
    new_rating = []
    if rating[recursion_var] == value:
        new_rating.extend(rating[:recursion_var])
        new_rating.append(value)
        new_rating.extend(rating[recursion_var:])
        return new_rating
    elif rating[recursion_var] < value:
        recursion_var -= recursion_var // 2
        new_rating.extend(private_add_rating_value(rating, value, recursion_var))
    else:
        recursion_var += recursion_var // 2
        new_rating.extend(private_add_rating_value(rating, value, recursion_var))
    return new_rating


while True:
    print("Введите число")
    input_int = input()
    if input_int.isdigit():
        input_int = int(input_int)
        break
    print("Введено отличное от числа значение")

print(add_rating_value(base_rating, input_int))
