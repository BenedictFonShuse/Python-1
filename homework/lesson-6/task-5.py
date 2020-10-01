"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title: str) -> None:
        self.title = title

    def draw(self):
        print(str(f"{self.title} рисует"))


class Pen(Stationery):
    def __init__(self) -> None:
        super().__init__("Ручка")


class Pencil(Stationery):
    def __init__(self) -> None:
        super().__init__("Карандаш")


class Handle(Stationery):
    def __init__(self) -> None:
        super().__init__("Маркер")


pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
