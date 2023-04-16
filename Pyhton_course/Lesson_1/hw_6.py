#Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
#Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
#Вам требуется написать программу, которая проверяет счастливость билета.
#*Пример:*
#385916 -> yes
#123456 -> no

ticket = str(input("Введите шестизначное число:"))
if len(ticket) != 6:
    print("Число не шестизначное!")
else:
    if int(ticket[0])+int(ticket[1])+int(ticket[2]) == int(ticket[-1])+int(ticket[-2])+int(ticket[-3]):
        print("Yes!")
    else:
        print("No!")