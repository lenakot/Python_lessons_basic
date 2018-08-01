import itertools
import math

__author__ = 'Котова Елена'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# Вычисляет n-ое число Фибоначчи.
def fib(n):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)


def fibonacci(n, m):
    result = []
    for i in range(n, m+1):
        result.append(fib(i))
    return result

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

# Сортировка пузырьком.
def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i+1]:
                origin_list[i], origin_list[i+1] = origin_list[i+1], origin_list[i]
        n += 1

origin_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(origin_list)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, lis):
    lis2 = []
    for x in lis:
        if func(x):
            lis2.append(x)
    return lis2

print(my_filter(lambda x: x % 3 == 0, [0, 1, 9, 15, 16, -3, 5]))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

a_x = float(input('Введите координату Х точки А '))
a_y = float(input('Введите координату У точки А '))
a = [a_x, a_y]

b_x = float(input('Введите координату Х точки B '))
b_y = float(input('Введите координату У точки B '))
b = [b_x, b_y]

c_x = float(input('Введите координату Х точки C '))
c_y = float(input('Введите координату У точки C '))
c = [c_x, c_y]

d_x = float(input('Введите координату Х точки D '))
d_y = float(input('Введите координату У точки D '))
d = [d_x, d_y]

def distance(a, b):
    return math.sqrt(((b[0]-a[0]) ** 2) + ((b[1]-a[1]) ** 2))

# Проверяет точки по порядку. A --> B --> C --> D.
def parallel_1(a, b, c, d):
    a_b = distance(a, b)
    d_c = distance(d, c)
    a_d = distance(a, d)
    b_c = distance(b, c)
    if a_b == d_c and a_d == b_c:
        return True
    else:
        return False

# Проверяет точки в любом порядке.
def parallel(a, b, c, d):
    points = [a, b, c, d]
    for a, b, c, d in itertools.permutations(points):
        if parallel_1(a, b, c, d):
            return True
    return False

print(parallel(a, b, c, d))
