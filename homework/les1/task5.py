"""
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""


class Company:
    status = 0
    profitability = 0
    employees = 0
    profitability_by_employee = 0

    def __init__(self, profit, loss):
        self.profit = profit
        self.loss = loss

    def calculate_financial_status(self):
        self.status = self.profit - self.loss
        if self.status > 0:
            print("Прибыль составила %s" % self.status)
        else:
            print("Убыток составил %s" % abs(self.status))
        return self.status

    def calculate_profitability(self):
        if self.status < 0:
            print("У вас убыток")
            return self.status
        self.profitability = self.status / self.profit * 100
        print("Рентабельность выручки составила %s процентов" % self.profitability)
        return self.profitability

    def calculate_profitability_by_employee(self):
        if self.status < 0:
            print("У вас убыток")
            return self.status
        self.profitability_by_employee = self.status / self.employees
        print("Прибыль фирмы в расчете на одного сотрудника составила %s" % self.profitability_by_employee)
        return self.profitability_by_employee


while True:
    print("Введите прибыль")
    profit_value = input()
    if profit_value.isdigit():
        profit_value = int(profit_value)
        break
    print("Введено отличное от числа значение")

while True:
    print("Введите убыток")
    loss_value = input()
    if loss_value.isdigit():
        loss_value = int(loss_value)
        break
    print("Введено отличное от числа значение")

company = Company(profit_value, loss_value)
status = company.calculate_financial_status()
if status > 0:
    company.calculate_profitability()

    while True:
        print("Введите количество сотрудников")
        employees_count = input()
        if employees_count.isdigit():
            employees_count = int(employees_count)
            break
        print("Введено отличное от числа значение")

    company.employees = employees_count
    company.calculate_profitability_by_employee()
