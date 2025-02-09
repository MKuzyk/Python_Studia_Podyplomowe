'''
Napisz skrypt wyświetlający na ekranie macierz. Rozmiar macierzy oraz
znak z jakiej będzie zbudowana powinien określić użytkownik
'''
print()
print("zadanie_2")
print()

rozmiar=int(input("Podaj liczbę wierszy i kolumn: "))
znak=str(input("Podaj znak który stworzy macierz:"))

for i in range (0,rozmiar):

    print(znak*rozmiar)
    i+1
