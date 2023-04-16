#Найдите сумму цифр трехзначного числа.
print("Enter 3 digit number:")
number = str(input())

if len(number) != 3:
    print("Wrong umber entered. You have to enter 3 digit number!")
else:
    sum = int(number[0]) + int(number[1]) + int(number[2])
    print("Sum of number's digits is {}".format(sum))