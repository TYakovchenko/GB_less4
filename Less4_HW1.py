#еализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

#Первый способ не получился, в конце выдает, что-то про модуль, не успеваю понять
#print("Способ 1:")
#import arh

#time, bonus, salary, res = arh

#calculation = res
#print(f"Your pay is equal", calculation)

print("Способ 2:")

def salary1():
    try:
        time2 = float(input('Выработка в часах '))
        salary2 = int(input('Ставка '))
        bonus2 = int(input('Премия '))
        res2 = time2 * salary2 + bonus2
        print(f'зарплата сотрудника  {res2}')
    except ValueError:
        return print('неверно')


salary1()