"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
from enum import Enum
from random import randint


class Direction(Enum):
    LEFT = "лево"
    RIGHT = "право"
    BACK = "назад"
    DEFAULT = "прямо"


class Car:
    def __init__(self, speed: int, color: str, name: str, is_police: bool) -> None:
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Врум-врум")

    def stop(self):
        print("Торможу и останавливаюсь")

    def turn(self, direction: Direction):
        print(str(f"Поворачиваю {direction.value}"))

    def get_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed: int, color: str, name: str) -> None:
        super().__init__(speed, color, name, False)

    def get_speed(self):
        if self.speed > 60:
            print("Превышение скорости!")
        super().get_speed()


class SportCar(Car):
    def __init__(self, speed: int, color: str, name: str) -> None:
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed: int, color: str, name: str) -> None:
        super().__init__(speed, color, name, False)

    def get_speed(self):
        if self.speed > 40:
            print("Превышение скорости!")
        super().get_speed()


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str) -> None:
        super().__init__(speed, color, name, True)


town_car = TownCar(randint(50, 100), "Самый лучший цвет", "Самое лучшее имя")
town_car.go()
town_car.turn(Direction.LEFT)
town_car.stop()
town_car.get_speed()
sport_car = SportCar(randint(80, 200), "Самый лучший цвет", "Самое лучшее имя")
sport_car.go()
sport_car.turn(Direction.RIGHT)
sport_car.stop()
sport_car.get_speed()
work_car = WorkCar(randint(50, 100), "Самый лучший цвет", "Самое лучшее имя")
work_car.go()
work_car.turn(Direction.BACK)
work_car.stop()
work_car.get_speed()
police_car = PoliceCar(randint(100, 220), "Самый лучший цвет", "Самое лучшее имя")
police_car.go()
police_car.turn(Direction.DEFAULT)
police_car.stop()
police_car.get_speed()
