'''
Wyświetl tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu
określonego przez użytkownika.
'''

zakres_from=int(input("Podaj początkową liczbę zakresu:"))
zakres_to=int(input("Podaj końcową liczbę zakresu:"))
is_first=True

print("liczby podziene przez 3, 5 lub t z zakresu od ",zakres_from," do ",zakres_to," to: ",end=" ")

for i in range (zakres_from,zakres_to+1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        if not is_first:
            print(",",end="")
        print ( i,end="")
        is_first = False
    i+=1

print(".")




