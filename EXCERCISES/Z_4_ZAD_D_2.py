'''
Napisz program, zliczający wystąpienia danego słowa we wskazanym tekście, w tym celu:
analizowany tekst wczytaj z pliku tekstowego np. znachor.txt,
pobierz od użytkownika szukane słowo,
wyświetl liczbę wystąpień zliczanego słowa.
'''

def zlicz_wystapienia(plik, slowo):
    try:
        # Otwieramy plik w trybie odczytu
        with open(plik, 'r') as p:
            tekst = p.read().lower().replace(',', ' ')

        # Zliczamy wystąpienia słowa w tekście

        liczba_wystapien = tekst.split().count(slowo.lower())
        return liczba_wystapien
    except FileNotFoundError:
        print(f"Plik {plik} nie został znaleziony.")
        return 0

# Pobieramy nazwę pliku i szukane słowo od użytkownika
plik = 'znachor.txt'  # Można to zmienić na nazwę pliku podaną przez użytkownika
slowo = input("Podaj słowo do zliczenia: ")

# Wywołujemy funkcję i wyświetlamy wynik
liczba_wystapien = zlicz_wystapienia(plik, slowo)
print(f"Słowo '{slowo}' występuje {liczba_wystapien} razy w pliku {plik}.")
