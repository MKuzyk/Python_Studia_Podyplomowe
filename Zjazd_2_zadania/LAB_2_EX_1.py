#Napisz skrypt sprawdzający czy pierwiastek kwadratowy z liczby całkowitej
#pobranej od użytkownika jest także liczbą całkowitą

number=int(input("Enter a number: "))
wynik=(number**(1/2))
print(wynik)

if wynik-round(wynik)==0:
    print("wynik jest liczbą całkowitą")
else:
    print("wynik nie jest liczbą całkowitą")