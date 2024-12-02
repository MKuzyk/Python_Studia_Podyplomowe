'''
Napisz program sumujący pobrane liczby od użytkownika wg wytycznych:
• program powinien pobierać od użytkownika liczby całkowite,
• niepodanie liczby powinno zakończyć wprowadzanie danych,
• program powinien podać sumę liczb parzystych oraz sumę liczb nieparzystych.
'''
from ipaddress import summarize_address_range
from operator import truediv

numbers=[]
i=0

while True:
    number=(input("Podaj "+str(i+1)+" liczbę: "))
    if number=="":
        break
    else:
        numbers.append(int(number))
    i+=1
print("Podałeś ",len(numbers)," liczby")
print(numbers)

# wersja 1 użycie funkcji sum

sum_parzyste=[]
sum_nieparzyst=[]

for number in numbers:
    if number % 2==0:
        sum_parzyste.append(number)
    else:
        sum_nieparzyst.append(number)

print("suma liczb parzystych to: ",sum(sum_parzyste))
print("suma liczb nieparzystych to: ",sum(sum_nieparzyst))

#wersja 2 bez funkcji

sum_p=0
sum_n=0

for number in numbers:
    if number % 2 == 0:
       sum_p+=number
    else:
        sum_n+=number
print("suma liczb parzystych to: ",str(sum_p),", a suma liczb nieparzystych to: ",str(sum_n))





