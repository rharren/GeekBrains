#Требуется определить, можно ли от шоколадки размером n × m долек 
#отломить k долек, если разрешается сделать один разлом по прямой между дольками 
#(то есть разломить шоколадку на два прямоугольника).
#*Пример:*
#3 2 4 -> yes
#3 2 1 -> no

n = int(input("Введите ширину шоколадки:"))
m = int(input("Ввведите длину шоколадки:"))
k = int(input("введите сколько долек нужно отломить:"))
if (k % n != 0 and k % m != 0) or k in [0,1]:
    print("No!")
else:
    print("Yes!") 