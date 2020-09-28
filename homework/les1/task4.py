"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

while True:
    print("Введите число")
    input_int = input()
    if input_int.isdigit():
        break
    print("Введено отличное от числа значение")

max_number = 0
for char in input_int:
    char = int(char)
    max_number = char if char > max_number else max_number

print(max_number)
