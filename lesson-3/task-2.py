"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
 город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
 Реализовать вывод данных о пользователе одной строкой.
"""
from datetime import date
from typing import List

import self


class User:
    first_name: str
    last_name: str
    birthday: date
    home_town: str
    email: str
    telephone: str

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name) :
        self.last_name = last_name

    def set_birthday(self, birthday):
        self.set_date(birthday)

    def set_home_town(self, home_town):
        self.home_town = home_town

    def set_email(self, email):
        self.email = email

    def set_telephone(self, telephone):
        self.telephone = telephone

    def get_user_data_template(self):
        return {
            self.set_first_name: ("Введиет имя", str),
            self.set_last_name: ("Введите фамилию", str),
            self.set_birthday: ("Введите дату рождения через пробелы (год, месяц, день)", str),
            self.set_home_town: ("Ввежите город проживания", str),
            self.set_email: ("Введите email", str),
            self.set_telephone: ("Ввдите телефон", str)
        }

    def set_date(self, date_string: str, delimiter: str = " ") -> None:
        int_array: List[int] = []
        for string in date_string.split(delimiter):
            int_array.append(int(string))
        self.birthday = date(int_array[0], int_array[1], int_array[2])

    def init_user(self):
        for key, value in self.get_user_data_template().items():
            key(value[1](input(value[0] + "\n")))
        return self

    def print(self):
        print(str(f"Имя: {self.first_name}\nФамилия: {self.last_name}\nДата рождения: {self.birthday}\nГород проживания: {self.home_town}\nEmail: {self.email}\nТелефон* {self.telephone}"))


user = User().init_user()

user.print()

