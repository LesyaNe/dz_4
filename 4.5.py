# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.*
# Пример:
#
#             - 2*x² + 4*x + 5 = 0
#             - 5*x² + 2*x + 43 = 0
#             - Результат: 7*x^2 + 6*x + 48 = 0
# *Значения коэффициентов от -100 до 100
# *Сумма многочленов с разными степенями
# Пример:
# - 2*x² + 4*x + 5 = 0
# - 5*x^4 + 2*x^3 - 6*x^2 + 13*x + 43 = 0
# - Результат: 5*x^4 + 2*x^3 - 4*x^2 + 17*x + 48 = 0

import random


# запись в файл
def write_file(name, s):
    with open(name, 'w') as data:
        data.write(s)


# создание случайного числа от 0 до 100
def run_num():
    return random.randint(0, 101)


# создание коэффициентов многочлена
def create_mnogo(k):
    lst = [run_num() for i in range(k + 1)]
    return lst


# создание многочлена в виде строки
def create_str(sp):
    lst = sp[::-1]
    w = ''
    if len(lst) < 1:
        w = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                w += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst[i + 1] != 0 or lst[i + 2] != 0:
                    w += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                w += f'{lst[i]}x'
                if lst[i + 1] != 0 or lst[i + 2] != 0:
                    w += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                w += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                w += ' = 0'
    return w


# получение степени многочлена
def sq_mnogo(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i + 1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num


# получение коэффицента члена многочлена
def k_mnogo(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num


# разбор многочлена и получение его коэффициентов
def calc_mnogo(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_mnogo(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1  # степень
    ii = l - 1  # индекс
    while ii >= 0:
        if sq_mnogo(st[ii]) != -1 and sq_mnogo(st[ii]) == i:
            lst.append(k_mnogo(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1

    return lst


# создание двух файлов

k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
koef1 = create_mnogo(k1)
koef2 = create_mnogo(k2)
write_file("file1.txt", create_str(koef1))
write_file("file2.txt", create_str(koef2))

# нахождение суммы многочлена

with open('file1.txt', 'r') as data:
    st1 = data.readlines()
with open('file2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = calc_mnogo(st1)
lst2 = calc_mnogo(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll, mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll, mm):
        lst_new.append(lst2[i])
write_file("file3.txt", create_str(lst_new))
with open('file3.txt', 'r') as data:
    st3 = data.readlines()
print(f"Сумма многочленов {st3}")