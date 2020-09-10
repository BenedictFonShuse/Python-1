"""
 Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
 Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""


while True:
    print("Введите размерность")
    array_size = input()
    if array_size.isdigit():
        break
    print("Введено отличное от числа значение")

while True:
    print("Введите число")
    passed_int = input()
    if passed_int.isdigit():
        break
    print("Введено отличное от числа значение")


arr1 = []

for i in range(int(array_size)):
    arr2 = []
    for j in range(i+1):
        arr2.append(int(passed_int))
    arr1.append(arr2)

middle_value = 0

for i in range(len(arr1)):
    first_value = 0
    for j in range(i+1):
        first_value += arr1[i][j]
    middle_value += first_value * 10 ** (len(arr1) - 1 - i)

print(middle_value)
