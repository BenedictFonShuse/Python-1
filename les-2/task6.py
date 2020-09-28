"""
 Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
 Каждый кортеж хранит информацию об отдельном товаре.
 В кортеже должно быть два элемента — номер товара и словарь с параметрами
 (характеристиками товара: название, цена, количество, единица измерения).
 Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""
from typing import Dict, List, Any

goods_template = {
    "название": "Введите название",
    "цена": "Введите цену",
    "количество": "Введите количество",
    "eд": "Введите единицу измерения"
}
goods_list = []

for number in range(3):
    goods = {}

    for key, value in goods_template.items():
        goods[key] = input(value + "\n")

    goods_set = (number, goods)
    goods_list.append(goods_set)


def create_analytics_data(list_of_dict_set):
    analytics_data: Dict[Any, List[Any]] = {}
    for dict_set in list_of_dict_set:
        for dict_key in dict_set[1]:
            analytics_data[dict_key] = []

    for dict_set in list_of_dict_set:
        for dict_key, dict_value in dict_set[1].items():
            analytics_data[dict_key].append(dict_value)
    return analytics_data


print(create_analytics_data(goods_list))
