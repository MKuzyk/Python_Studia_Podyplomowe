'''
Zadanie 1
Napisz program obliczający wartość bezwzględną z liczby podanej przez użytkownika.
'''

podana_liczba = int(input("podaj liczbę. W wyniku dostaniesz liczbę bezwzględną! "))

print("wartość bezwzględna z poodanej liczby wynosi :",abs(podana_liczba))

'''
Zadanie 2
Napisz program informujący czy liczba podana przez użytkownika jest większa, mniejsza czy równa zero. Wykorzystaj
 tylko dwie instrukcje warunkowe.
'''

podana_liczba = int(input("podaj liczbę: "))

if podana_liczba>0:
    print("liczba ",podana_liczba," jest większa od zera")
elif podana_liczba<0:
    print("liczba ", podana_liczba, " jest mniejsza od zera")
else: print("padana liczba jest równa 0")

'''
Zadanie 3
Napisz program informujący czy liczba podana przez użytkownika jest parzysta czy nieparzysta.
'''

podana_liczba = int(input("podaj liczbę: "))

if podana_liczba%2==0:
    print("podana liczba jest parzysta!!")
else:
    print("podana liczba jest nieparzysta!")

'''
Zadanie 4
Napisz program wyznaczający najmniejszą z trzech liczb podanych przez użytkownika.
'''

'''
Zadanie 5
Napisz program, który odpowiada na pytanie, czy wśród trzech liczb są choć dwie takie same.
'''

'''
Zadanie 6
Napisz program, który odpowiada na pytanie, czy trzy podawane liczby całkowite są ustawione w porządku rosnącym.
'''