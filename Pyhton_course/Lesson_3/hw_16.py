from random import randint

lst_len = int(input("Введите длину массива:"))
if lst_len < 1:
    print("Длина массива должна быть натуральным числом!")
else:
    answer =input("""Хотите ввести массив сами, тогда введите '1'\n
    или массив сгенерируется самостоятельно, для этого введите '2'.\n
    Длина массива должна быть {0}.\n
    Значения необходимо вводить через "," без пробелов.\n""".format(lst_len))
    if answer == '1':
        lst = list(map(int,input().split(","))) #элементы отделяем запятой и текст переводим в числовой список
    else:
        lst = [randint(1, 1001) for i in range(lst_len)]
    print(lst)   # we have list now

    find = int(input("Введите число, частоту встречаемости которого хотите посчитать в списке:\n"))
    print("Число {0} встречается в списке: {1}".format(find,lst.count(find)))