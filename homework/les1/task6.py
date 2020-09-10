"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""

while True:
    print("Введите начальный результат")
    first_result = input()
    if first_result.isdigit():
        first_result = int(first_result)
        break
    print("Введено отличное от числа значение")

while True:
    print("Введите начальный результат")
    goal_value = input()
    if goal_value.isdigit():
        goal_value = float(goal_value)
        break
    print("Введено отличное от числа значение")

while True:
    print("Введите ваш прогресс в процентах")
    progress = input()
    if progress.isdigit():
        progress = int(progress)
        break
    print("Введено отличное от числа значение")

progress = 1.0 + progress / 100


def get_target_day(first_value, target_value, coefficient, counter):
    first_value = first_value * coefficient
    counter += 1
    if first_value >= target_value:
        return counter
    else:
        counter = get_target_day(first_value, target_value, coefficient, counter)
    return counter


day_number = get_target_day(first_result, goal_value, progress, 0)

print(day_number)
