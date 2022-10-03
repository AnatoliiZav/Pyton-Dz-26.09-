# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n! = 1 * 2 * … * n,

n = int(input('Введите число: '))

def f(x):
    return ((x == 1) and 1) or x * f(x - 1)

list1 = list(f(i) for i in range(1, n + 1))
print(list1)
