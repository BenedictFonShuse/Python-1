"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна.
Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:

    def __init__(self, length: float, width: float) -> None:
        self.__length = length
        self.__width = width

    def calculate_mass(self, layer_thickness: float, solidity: float) -> float:
        return self.__length * self.__width * layer_thickness * solidity

    def __str__(self) -> str:
        return str(f"Road: id - {id(self)} length - {self.__length} m, width - {self.__width} m")


road = Road(5000, 20)

print(road)

mass = road.calculate_mass(5, 25)

print(str(f"{mass} кг"))

