# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
# (Выполнили на семинаре)
n = int(input("Введите число: \n"))
i = 2
lst = []
n1 = n
while i <= n:
    if n % i == 0:
        lst.append(i)
        n //= i
        i += 1
print(f"множители числа {n1}: {lst}")
print(set(lst).intersection())