'''
Napisz grę polegającą na zapamiętywaniu kolejnych słów. Wylosowany
gracz podaje pierwsze słowo a kolejny powtarza słowo i dodaje swoje.
Następny w kolejce gracz musi podać wszystkie wcześniejsze słowa w tej
samej kolejności i także dodać swoje. Rozgrywka kończy się gdy, któryś z
graczy popełni błąd. Na ekranie komputera przy każdej turze należy
wymazać ekran np. przez wyświetlenie 100 pustych wierszy.
'''

import random
import os
import time


def clear_screen():
    """Funkcja do wyczyszczenia ekranu"""
    os.system('cls' if os.name == 'nt' else 'clear')


def gra():
    print("Witaj w grze polegającej na zapamiętywaniu słów!")
    gracze = input("Podaj imiona graczy (oddzielone przecinkami): ").split(",")
    gracze = [gracz.strip() for gracz in gracze]

    kolejka_graczy = random.sample(gracze, len(gracze))  # Losowanie kolejności graczy
    slowa = []  # Lista do przechowywania słów

    while True:
        for gracz in kolejka_graczy:
            # Losowanie pierwszego słowa
            if len(slowa) == 0:
                slowo = input(f"{gracz}, podaj pierwsze słowo: ")
                slowa.append(slowo)
            else:
                # Gra polega na powtarzaniu poprzednich słów i dodawaniu nowego
                clear_screen()  # Czyszczenie ekranu
                print("Słowa do zapamiętania:")
                print(" ".join(slowa))  # Wyświetlanie dotychczasowych słów
                slowo = input(f"{gracz}, powtórz wszystkie słowa i dodaj swoje: ")
                # Sprawdzanie, czy gracz podał poprawne słowo
                if slowo != " ".join(slowa) + " " + slowo.split()[-1]:
                    print("Błąd! Gra skończona.")
                    return
                slowa.append(slowo.split()[-1])  # Dodanie nowego słowa do listy

            time.sleep(1)  # Krótkie opóźnienie dla wygody gry


if __name__ == "__main__":
    gra()
