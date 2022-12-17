# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать
# в файл многочлен степени k(до 6 степени).*
#
#         *Пример:*
#
#         - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import itertools

k = int(input("Введите натуральную степень k = "))


def get_multiplier(k):
    multiplier = [randint(-10, 10) for i in range (k + 1)]
    while multiplier[0] == 0:
        multiplier[0] = randint(-10, 10)
    return multiplier

def get_polynomial(k, multiplier):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(multiplier, var, range(k, 1, -1), fillvalue ='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')


multiplier = get_multiplier(k)
polynom1 = get_polynomial(k, multiplier)
print(polynom1)

with open('4.4_Polynomial.txt', 'w') as data:
    data.write(polynom1)


k = int(input("Введите натуральную степень k = "))

multiplier = get_multiplier(k)
polynom2 = get_polynomial(k, multiplier)
print(polynom2)

with open('4.4_Polynomial2.txt', 'w') as data:
    data.write(polynom2)