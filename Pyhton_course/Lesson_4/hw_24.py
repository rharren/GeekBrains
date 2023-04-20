# В фермерском хозяйстве в Карелии выращивают чернику. 
#Она растёт на круглой грядке, причём кусты высажены только по окружности. 
#Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод 
#— на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
#Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
#Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
#собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
#находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint

def control(lst_len):
    if lst_len < 1:
        print("Количество кустов должно быть натуральным числом!")
    else:
        answer = input("""Хотите ввести количество ягод на каждом кусте сами, тогда введите '1'\n
        или сгенерируем самостоятельно, для этого введите '2'.\n
        Количество кустов должно быть {0}.\n
        Значения необходимо вводить через "," без пробелов.\n""".format(lst_len))
        if answer == '1':
            lst = list(map(int,input().split(","))) #элементы отделяем запятой и текст переводим в числовой список
        else:
            lst = [randint(1, 101) for i in range(lst_len)]
        print(lst)   # we have list now
        return lst
lst_len_1 = int(input("Введите количество кустов:"))
lst_1 = control(lst_len_1)

# получили массив его индексы отражают кусты, а значения в массиве - количество ягод с каждого куста
bush = int(input("Введите номер куста с которого хотите собрать ягоды (номера с 1 по {}. Модуль соберет ягоды и с двух соседних кустов.)\n".format(lst_len_1)))
if bush > lst_len_1:
    print("Вы ввели значение больше количества кустов!")
elif bush < 1:
    print("Вы ввели значение меньше 1! Кусты прономерованы с 1")


if lst_len_1 >= 3:
# чтобы получить индекс куста вычитаем из него 1 получается что выписывая индекс 2 второй куст в списке это будет индекс 1 тк индексирование идет с 0
    if bush == lst_len_1:
        berry = lst_1[bush-2] + lst_1[bush-1] + lst_1[0]
    else:
        berry = lst_1[bush-2] + lst_1[bush-1] + lst_1[bush-1+1] 
    print("Ответ с кустов соберем: {}".format(berry))
elif lst_len_1 == 1:
    print("У нас всего 1 куст, с него можно собрать {} ягод.".format(lst_1[0]))
elif lst_len_1 == 2:
    print("У нас всего 2 куста, с них можно собрать {} ягод.".format(lst_1[0]+lst_1[1]))
else: 
    print("Error! #1")


print("Какое максимальное количество ягод можно было собрать нашим автоматическим модулем за раз:")
max_berry = 0

for i in range(lst_len_1):
    if lst_len_1 == 1:
        print("Ответ: {}".format(lst_1[0]))
        break
    elif lst_len_1 == 2:
        print("Ответ: {}".format(lst_1[0]+lst_1[1]))
        break
    elif lst_len_1 >= 3:
        if i == lst_len_1 -1:
            if max_berry < lst_1[i-1] + lst_1[i] + lst_1[0]:
                max_berry = lst_1[i-1] + lst_1[i] + lst_1[0]
        else:
            if max_berry < lst_1[i-1] + lst_1[i] + lst_1[i+1]:
                max_berry = lst_1[i-1] + lst_1[i] + lst_1[i+1]
        print("Ответ: {}".format(max_berry))
    else:
        print("Error! #2")