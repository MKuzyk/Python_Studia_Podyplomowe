'''
Napisz grę w zgadywanie liczby z przedziału od 1 do 10. Gracz powinien dostać
3 szanse. Po nieudanej próbie, gracz powinien otrzymać podpowiedź np.
o parzystości zgadywanej liczby itp.
'''

#zgadnij liczbę

import random

number=random.randint(1,10)
guess=int(input("Zgadnij jaką liczbę mam na myśli od 1 do 10: "))


if guess==number:
    print("podałeś poprawną liczbę")
else:
    print("niestety podałeś niepoprawną liczbę")
    if number%2==0:
        print("Podpowiedz:liczba jest liczba przystą")
    else:
        print("Podpowiedz:liczba jest liczba nieprzystą")
        guess2 = int(input("podaj drugi raz liczbę: "))
        if guess2==number:
            print("podałeś poprawną liczbę")
        else:
            print("niestety podałeś niepoprawną liczbę")
            print("różnica pomiędzy twoją drugą podaną liczbą a wylosowaną wynosi",number-guess2)
            guess3=int(input("ostatnia próba może teraz się uda: "))
            if guess3==number:
                print("podałeś poprawną liczbę")
            else:
                print("niestety podałeś niepoprawną liczbę")
                print("Poprawna Liczba wynosi ",number)


