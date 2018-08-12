import math

__author__ = 'Котова Елена'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


def distance(a, b):
    return math.sqrt(((b[0]-a[0]) ** 2) + ((b[1]-a[1]) ** 2))

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.ab = distance(self.a, self.b)
        self.bc = distance(self.b, self.c)
        self.ca = distance(self.c, self.a)

    def perimeter(self):
        return self.ab + self.bc + self.ca

    def height(self, side):
        ab = self.ab
        bc = self.bc
        ca = self.ca
        p = self.perimeter()/2
        return (2/side) * math.sqrt(p * (p - ab) * (p - bc) * (p - ca))

    # Высота из точки self.a
    def height_a(self):
        return self.height(self.bc)

    # Высота из точки self.b
    def height_b(self):
        return self.height(self.ca)

    # Высота из точки self.c
    def height_c(self):
        return self.height(self.ab)

    def area(self):
        return (self.ca/2) * self.height_b()


tri = Triangle((1, 1), (3, 4), (5, 1))
print('Периметр: ', tri.perimeter())
print('Высота: ', tri.height_b())
print('Площадь: ', tri.area())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class IsoscelesTrapezium:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.ab = distance(self.a, self.b)
        self.bc = distance(self.b, self.c)
        self.cd = distance(self.c, self.d)
        self.da = distance(self.d, self.a)

    # Проверяем: трапеция равнобедренная, если её диагонали равны. Если всё ок, то вернет True.
    def check(self):
        return distance(self.c, self.a) == distance(self.b, self.d)

    def perimeter(self):
        return self.ab + self.bc + self.cd + self.da

    def area(self):
        return ((self.da + self.bc)/4) * math.sqrt((4 *(self.ab ** 2)) - ((self.da - self.bc) ** 2))


trap = IsoscelesTrapezium((1, 1), (3, 5), (6, 5), (8, 1))
print('Длина стороны ab = ', trap.ab)
print('Длина стороны bc = ', trap.bc)
print('Длина стороны cd = ', trap.cd)
print('Длина стороны da = ', trap.da)
print('Является ли трапеция равнобедренной: ', trap.check())
print('Периметр: ', trap.perimeter())
print('Площадь: ', trap.area())