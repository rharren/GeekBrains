# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

from random import randint

def control(lst_len):
    if lst_len < 1:
        print("Длина массива должна быть натуральным числом!")
    else:
        answer = input("""Хотите ввести массив сами, тогда введите '1'\n
        или массив сгенерируется самостоятельно, для этого введите '2'.\n
        Длина массива должна быть {0}.\n
        Значения необходимо вводить через "," без пробелов.\n""".format(lst_len))
        if answer == '1':
            lst = list(map(int,input().split(","))) #элементы отделяем запятой и текст переводим в числовой список
        else:
            lst = [randint(1, 1001) for i in range(lst_len)]
        print(lst)   # we have list now
        return lst
lst_len_1 = int(input("Введите длину массива 1:"))
lst_1 = control(lst_len_1)
lst_len_2 = int(input("Введите длину массива 2:"))
lst_2 = control(lst_len_2)
print(sorted(set(lst_1).intersection((set(lst_2)))))