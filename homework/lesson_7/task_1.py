"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""
from typing import List


class Matrix:
    __slots__ = ("matrix_value",)

    def __init__(self, matrix_value: List[List]) -> None:
        self.matrix_value = matrix_value

    def __str__(self) -> str:
        out_str = ""
        for matrix_list in self.matrix_value:
            out_str += "| "
            for item in matrix_list:
                out_str += str(f"{item:>03} ", )
            out_str += "|\n"
        return out_str

    def __add__(self, other):
        new_list_of_list = []
        for i in range(len(other.matrix_value)):
            temp_list = []
            for j in range(len(other.matrix_value[i])):
                temp_list.append(self.matrix_value[i][j] + other.matrix_value[i][j])
            new_list_of_list.append(temp_list)
        return Matrix(new_list_of_list)


if __name__ == '__main__':
    matrix1 = Matrix([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
    matrix2 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    matrix3 = matrix1 + matrix2
    print(matrix3)
