
__author__ = 'Котова Елена'

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Teacher:
    def __init__(self, surname, course):
        self.surname = surname
        self.course = course

class ClassRoom:
    def __init__(self, number, teachers):
        self.number = number
        self.teachers = teachers

class Student:
    def __init__(self, name, surname, mother, father, class_room):
        self.name = name
        self.surname = surname
        self.mother = mother
        self.father = father
        self.class_room = class_room

teachers = {
    'Грибов': Teacher('Грибов', 'Математика'),
    'Иванов': Teacher('Иванов', 'Рус.Язык'),
    'Петров': Teacher('Петров', 'История'),
    'Пучкин': Teacher('Пучкин', 'Биология'),
    'Сергеева': Teacher('Сергеева', 'Литература'),
}

classes = {
    '1А': ClassRoom('1А', ['Петров', 'Иванов', 'Сергеева']),
    '1Б': ClassRoom('1Б', ['Сергеева', 'Пучкин']),
    '2Б': ClassRoom('2Б', ['Петров', 'Пучкин']),
    '3В': ClassRoom('3В', ['Иванов', 'Грибов']),
}

students = {
   'Петр Алексеев': Student('Петр', 'Алексеев', 'Алексеева Татьяна', 'Алексеев Вадим', '1А'),
   'Анна Алексеева': Student('Анна', 'Алексеева', 'Алексеева Татьяна', 'Алексеев Вадим', '1Б'),
   'Василий Иванов': Student('Василий', 'Иванов', 'Плотникова Наталья', 'Иванов Иван', '2Б'),
   'Матвей Бурин': Student('Матвей', 'Бурин', 'Бурина Евгения', 'Дурнин Пётр', '3В'),
}

# 1. Получить полный список всех классов школы
for el in classes:
    print(el)

# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
class_room = '2Б'
for el in students.values():
    if el.class_room == class_room:
        print(el.name, el.surname)

# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)

fullname = 'Анна Алексеева'
if fullname in students:
    class_room = students[fullname].class_room
    if class_room in classes:
        for surname in classes[class_room].teachers:
            if surname in teachers:
                print(teachers[surname].course)

# 4. Узнать ФИО родителей указанного ученика
fullname = 'Анна Алексеева'
if fullname in students:
    print('Мать: ', students[fullname].mother)
    print('Отец: ', students[fullname].father)

# 5. Получить список всех Учителей, преподающих в указанном классе
class_room = '2Б'
if class_room in classes:
    print(classes[class_room].teachers)
