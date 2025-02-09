'''
Napisz program przechowujący informacje o pracownikach:
• możliwe typy osób to: menedżer, zwykła osoba, pracownik,
• każda z osób powinna posiadać imię,
• tylko menadżer będzie miał przydzielony projekt,
• zwykła osoba nie będzie posiadała informacji o wynagrodzeniu.
Zademonstruj działanie programu przechowując listę różnych typów osób/pracowników.
'''


class Osoba:
    def __init__(self, imie):
        self.imie = imie

    def __str__(self):
        return f"Imię: {self.imie}"


class Pracownik(Osoba):
    def __init__(self, imie, wynagrodzenie):
        super().__init__(imie)
        self.wynagrodzenie = wynagrodzenie

    def __str__(self):
        return f"{super().__str__()}, Wynagrodzenie: {self.wynagrodzenie} PLN"


class ZwyklaOsoba(Osoba):
    def __init__(self, imie):
        super().__init__(imie)

    def __str__(self):
        return super().__str__()


class Menedzer(Pracownik):
    def __init__(self, imie, wynagrodzenie, projekt):
        super().__init__(imie, wynagrodzenie)
        self.projekt = projekt

    def __str__(self):
        return f"{super().__str__()}, Projekt: {self.projekt}"


# Tworzymy listę różnych osób/pracowników
osoby = [
    Pracownik("Jan Kowalski", 3000),
    ZwyklaOsoba("Anna Nowak"),
    Menedzer("Michał Kuzyk", 5000, "Projekt A"),
    Pracownik("Katarzyna Nowak", 3500),
    ZwyklaOsoba("Paweł Kucharski")
]

# Wyświetlamy wszystkie osoby
for osoba in osoby:
    print(osoba)