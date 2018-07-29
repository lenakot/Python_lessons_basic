import math
import random

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

a = [2, -5, 8, 9, -25, 25, 4]
b = []
for x in a:
    if x >= 0:
        x = math.sqrt(x)
        if x == int(x):
            b.append(int(x))
print(b)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

n = int(input('Введите количество элементов '))
a = []
for x in range(n):
    a.append(random.randint(-100, 100))
print(a)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

a = [1, 2, 4, 5, 6, 2, 5, 2]
# 4.a.
b = list(set(a))
print(b)

# 4.б.
b = []
for i in range(len(a)):
    if not (a[i] in a[:i] + a[i+1:]):
        b.append(a[i])
print(b)
