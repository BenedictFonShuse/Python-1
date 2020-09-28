class Seconds:
    value = 0


class Minute:
    value = 0


class Hour:
    value = 0


class Alarm:
    seconds = Seconds
    minute = Minute
    hour = Hour

    dict = {0: Hour, 1: Minute, 2: Seconds}

    def time_parser(self, seconds, recursion_number):
        if recursion_number == 2:
            self.dict[recursion_number].value = seconds
            return self
        support_number = 60 ** (2 - recursion_number)
        if seconds >= support_number:
            seconds_number = seconds // support_number
            self.dict[recursion_number].value = seconds_number
            seconds -= seconds_number * support_number
            recursion_number += 1
            self.time_parser(seconds, recursion_number)
        else:
            recursion_number += 1
            self.time_parser(seconds, recursion_number)


while True:
    print("Введите время в секундах")
    input_seconds = input()
    if input_seconds.isdigit():
        break
    print("Введено отличное от числа значение")

new_alarm = Alarm()

new_alarm.time_parser(int(input_seconds), 0)

print(str(new_alarm.hour.value) + ":" + str(new_alarm.minute.value) + ":" + str(new_alarm.seconds.value))
