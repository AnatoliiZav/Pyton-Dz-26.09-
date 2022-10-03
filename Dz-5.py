# Реализуйте алгоритм перемешивания списка


thislist = ["синий", "желтый", "красный", "черный", "зеленый"]

for i in range(len(thislist)//2):
    thislist[i], thislist[-1-i] = thislist[-1-i], thislist[i]

print(thislist)


