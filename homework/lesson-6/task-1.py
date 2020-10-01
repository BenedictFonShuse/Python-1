"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time
from enum import Enum


class TrafficLightColor(Enum):
    READ = 7
    YELLOW = 2
    GREEN = 11


class TrafficLight:
    __change_step = 0
    __color: TrafficLightColor
    __change_color_info = (TrafficLightColor.READ, TrafficLightColor.YELLOW, TrafficLightColor.GREEN)

    def change_color(self):
        self.color = self.change_color_info[self.change_step % len(self.change_color_info)]
        self.change_step += 1
        print(self.color.name)

    def running(self):
        begin = time.monotonic()
        while True:
            self.change_color()
            if print():
                break
            time.sleep(self.color.value)


light = TrafficLight()

light.running()
light.running()
light.running()
