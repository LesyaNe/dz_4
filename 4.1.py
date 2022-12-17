# Вычислить число ПИ c заданной точностью d
# *Пример:*
#
# - при d = 0.0001, π = 3.1415.    10^-1 ≤ d ≤ 10^-10
import math
from math import pi

from unicodedata import decimal

d = float(input("Введите число d:\n"))

print(pi)

i = str(d)
a = abs(i.find('.') - len(i)) - 1
print(a)

s = round(math.pi, a)

print(f'число Пи с заданной точностью {d} равно {s}')




