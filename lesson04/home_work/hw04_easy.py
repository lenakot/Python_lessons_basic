import random
 
__author__ = 'Котова Елена'

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

lst_g = [random.randint(-10, 10) for _ in range(10)]
lst_new = [ i**2 for i in lst_g]
print('lst_g = ', lst_g)
print('lst_new = ', lst_new)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits_1 = ['apple', 'banana', 'potato', 'orange', 'mango']
fruits_2 = ['mango', 'kivy', 'pinapple', 'tomato', 'banana']
fruits_new = [i for i in fruits_1 if i in fruits_2]
print('fruits_new = ', fruits_new)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

lst_g = [random.randint(-10, 10) for _ in range(10)]
lst_new = [i for i in lst_g if i % 3 == 0 and i > 0 and i % 4 != 0]
print('lst_g = ', lst_g)
print('lst_new = ', lst_new)