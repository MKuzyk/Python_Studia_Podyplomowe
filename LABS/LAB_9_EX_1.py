'''
Wyświetl tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu
określonego przez użytkownika.
'''

zakres=int(input("Podaj zakres od 0 do:"))

for i in range (zakres+1):

    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print (i,end=" ")
        i+=1




