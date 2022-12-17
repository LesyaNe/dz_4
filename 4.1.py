# Вычислить число ПИ c заданной точностью d
# *Пример:*
#
# - при d = 0.0001, π = 3.1415.    10^-1 ≤ d ≤ 10^-10


# from math import pi
#
# d =  input("Введите число для заданной точности числа Пи:\n")
# d = string
#
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

from math import pi

d = int(input("Введите число d:\n"))

print(pi)

template = '{:.' + str(d) + 'f}'
print(template.format(pi))
