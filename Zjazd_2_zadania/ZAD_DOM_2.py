'''
Napisz program, który wylosuje kilka serii liczb całkowitych i wyświetli je
na ekranie, przy czym:
• program zapyta użytkownika o zakres minimum oraz maksimum,
• będzie losował odpowiednie liczby z zakresu podanego przez użytkownika,
• będzie losował liczbę liczb do wylosowania z zakresu podanego przez użytkownika,
• będzie losował liczbę serii liczb do wylosowania z zakresu podanego przez
użytkownika,
• wyświetli wylosowane serie liczb.
'''

import random
from dataclasses import replace

l_range=int(input("podaj dolny zakres: "))
u_range=int(input("podaj górny zakres: "))

rand_numbers=[]
series_numbers = []
series=int(random.randint(l_range,u_range))

for i in range(l_range,u_range+1):
    rand_numbers.append(int(random.randint(l_range,u_range)))

print(rand_numbers)

for j in range(series):

    series_numbers.clear()

    for i in range(l_range,u_range+1):
        series_numbers.append(int(random.randint(l_range,u_range)))
    print(series_numbers,end=" ")



