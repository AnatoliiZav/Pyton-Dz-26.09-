# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму

n = int(input('Введите число: '))

def f(x):
    num = (1+1/x)**x
    return num

list1 = list(f(i) for i in range(1, n + 1))

print(sum(list1))