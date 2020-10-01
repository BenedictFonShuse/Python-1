"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class FullName:
    def __init__(self, first_name: str, last_name: str, middle_name: str = None) -> None:
        self.middle_name = middle_name
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        if self.middle_name is not None:
            to_string = str(f"{self.first_name} {self.middle_name} {self.last_name}")
        else:
            to_string = str(f"{self.first_name} {self.last_name}")
        return to_string


class Income:
    def __init__(self, wage: int, bonus: int = 0) -> None:
        self.wage = wage
        self.bonus = bonus

    def get_total_income(self):
        return self.wage + self.bonus


class Worker:
    def __init__(self, full_name: FullName, position: str, income: Income) -> None:
        self.full_name = full_name
        self.position = position
        self.income = income


class Position(Worker):
    def get_full_name_and_income(self):
        print(str(f"{self.full_name}: {self.income.get_total_income()}"))


position = Position(FullName("Петр", "Вилкин"), "Ведущий специалист", Income(100000, 20000))

position.get_full_name_and_income()
