'''
Napisz program sumujący pobrane liczby od użytkownika wg wytycznych:
• program powinien pobierać od użytkownika liczby całkowite,
• niepodanie liczby powinno zakończyć wprowadzanie danych,
• program powinien podać sumę liczb parzystych oraz sumę liczb nieparzystych.
'''
from ipaddress import summarize_address_range

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

sum_parzyst=0
sum_nieparzyst=0

