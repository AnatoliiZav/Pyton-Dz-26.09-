#  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


def sumNums(nums):
    sum = 0
    for i in str(nums):
        if i != "." and i != "-":
            sum += int(i)
    return sum

num = float(input("Введите число:"))

print(f"Сумма цифр = {sumNums(num)}")