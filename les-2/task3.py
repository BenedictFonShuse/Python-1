"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

seasons = {1: "Зима", 2: "Весна", 3: "Лето", 4: "Осень"}

list_of_month = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 1]


while True:
    print("Введите номер месяца от 1 до 12")
    input_int = input()
    if input_int.isdigit():
        input_int = int(input_int)
        if 0 < input_int <= 12:
            break
        else:
            print("Введено отличное от требуемого число")
    else:
        print("Введено отличное от числа значение")

print(seasons[list_of_month[input_int]])
