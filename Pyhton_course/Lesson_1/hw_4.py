# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

sum = int(input("Ввведите число журавликов которое сделали дети: "))
if sum % 6 != 0:
    print("Введенное число не подходит под условие задачи!")
else:
    peter = sum / 6
    serge = peter
    kate = 2*(serge + peter)
    print("Петя сделал: {0}, Катя сделала: {1}, Сергей сделал: {2}".format(int(peter), int(kate), int(serge)))