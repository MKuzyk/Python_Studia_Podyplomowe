'''
Napisze kod do gry w lotto
'''

import random

def pobierz_system_gry():
    while True:
        try:
            ilość=int(input("Podaj ile liczb chcesz skreślić ( od 6 do 12) : "))
            if ilość < 6 or ilość > 12:
                print("Należy podac liczbę z przedziału od 6 do 12")
                continue
            return ilość
        except ValueError:
            print("To nie jest liczba!")
            continue

def losuj_liczby():
    """6 unikalnych liczb z zakresu 1-49."""
    return sorted(random.sample(range(1, 50), 6))


def pobierz_liczby_od_gracza():
    """Pobiera 6 unikalnych liczb od użytkownika."""
    liczby_gracza = set()
    print(f"Podaj {(system)} unikalnych liczb z zakresu 1-49:")
    while len(liczby_gracza) < system:
        try:
            liczba = int(input(f"Liczba {len(liczby_gracza) + 1}: "))
            if liczba < 1 or liczba > 49:
                print("Błąd: liczba musi być w zakresie 1-49.")
            elif liczba in liczby_gracza:
                print("Błąd: ta liczba została już wybrana.")
            else:
                liczby_gracza.add(liczba)
        except ValueError:
            print("Błąd: wpisz poprawną liczbę.")

    return sorted(liczby_gracza)


def sprawdz_wynik(liczby_gracza, liczby_wygrane):
    """Porównuje liczby gracza z wylosowanymi i zwraca liczbę trafień."""
    trafienia = set(liczby_gracza) & set(liczby_wygrane)
    return trafienia


# --- Główna część gry ---
print("Witaj w grze LOTTO!\n")

system=pobierz_system_gry()
liczby_gracza = pobierz_liczby_od_gracza()
liczby_wygrane = losuj_liczby()

print("Ilość losowanych liczb:", system)
print("Twoje liczby:", liczby_gracza)
print("Wylosowane liczby:", liczby_wygrane)

trafienia = sprawdz_wynik(liczby_gracza, liczby_wygrane)

if trafienia:
    print(f"Trafiłeś {len(trafienia)} liczbe / liczby: {sorted(trafienia)}!")
else:
    print("\nNiestety, nie trafiłeś żadnej liczby.")


