"""
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно.

В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n**.

Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n*****.
"""
from abc import ABC


class Cell(ABC):
    __slots__ = ("value",)

    def make_order(self, num: int):
        pass


class CellImpl(Cell):
    def __init__(self, value: int) -> None:
        self.value = value

    def __add__(self, other: Cell) -> Cell:
        return CellImpl(self.value + other.value)

    def __sub__(self, other: Cell) -> Cell:
        value = self.value - other.value
        if value > 0:
            return CellImpl(value)

    def __mul__(self, other: Cell) -> Cell:
        return CellImpl(self.value * other.value)

    def __truediv__(self, other: Cell) -> Cell:
        if other.value == 0:
            print("Вторая клетка не имеет ячеек")
        value = round(self.value / other.value)
        return CellImpl(value)

    def make_order(self, num: int):
        out_str = ""
        for i in range(self.value // num):
            out_str += "*" * num + "\n"
        out_str += "*" * (self.value % num)
        return out_str

    def __str__(self) -> str:
        return str(self.value)


if __name__ == '__main__':
    cell_impl1 = CellImpl(15)
    cell_impl2 = CellImpl(2)
    cell = cell_impl1 + cell_impl2
    print(cell)
    print(cell.make_order(5))
    print("-"*15)
    cell = cell_impl1 - cell_impl2
    print(cell.make_order(5))
    print(cell)
    print("-"*15)
    cell = cell_impl1 * cell_impl2
    print(cell.make_order(5))
    print(cell)
    print("-"*15)
    cell = cell_impl1 / cell_impl2
    print(cell.make_order(5))
    print(cell)
