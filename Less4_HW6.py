#6. Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.

#Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
#Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle

def my_func1(num_1, num_end):
    for el in count(num_end):
        if el > num_end:
            break
        else:
            print("Вы ввели: ",el)

def my_func2(my_list, repit):
    i = 0
    iter = cycle(my_list)
    while i < repit:
        print("Результат",next(iter))
        i += 1

start_num = int(input("Первое число: "))
last_num = int(input("Последнее число: "))
my_func1(num_1=start_num, num_end=last_num)
my_func2(my_list=[1, 2], repit=int(input("введите итератор: ")))