#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input("Введите количество монеток:"))
while n > 0:
    list = [random.randint(0,1) for i in range(n)]
    print("Так лежат монетки: {}".format(list))

    #переменные сторон монеток
    heads = 0
    tails = 0

    #пробегаемся по нашим монеткам
    for i in list:
        if i == 1:
            heads +=1
        else:
            tails +=1

    if heads >= tails:
        print("Орлом вверх: {0},\nОрешкой вверх: {1},\nМинимальное количество монеток, которое необходимо перевернуть: {2}".format(heads, tails, tails))
    else:
        print("Орлом вверх: {0},\nОрешкой вверх: {1},\nМинимальное количество монеток, которое необходимо перевернуть: {2}".format(heads, tails, heads)) 
    break
else:
    print("Нет монеток на столе!")