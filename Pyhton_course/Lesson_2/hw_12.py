#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
#Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
#а Катя должна их отгадать. Для этого Петя делает две подсказки. 
#Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
s = int(input('Введите сумма чисел:'))
p = int(input('Введите произведние чисел:'))

for i in range(1001):
    for j in range(1001):
        if i+j == s and i*j == p:
            print(i,j)
            break
        else:
            j +=1
    if i+j == s and i*j == p:
            break
    i +=1