'''
Napisz, przetestuj i zastosuj własny moduł do obsługi list liczb całkowitych:
• stwórz modułu o dowolnej nazwie,
• dodaj funkcję weryfikującą czy podana lista zawiera wyłącznie liczby całkowite,
• dodaj funkcję sumującą wszystkie liczby z listy,
• dodaj funkcję zwracającą iloczyn wszystkich liczb z listy,
• dodaj testy weryfikujące poprawne działanie napisanych funkcji,
• zaimportuj utworzony moduł i skorzystaj z jego funkcji.
'''

# LAB_16_EX_2_modul_obsluga_liczb

def czy_lista_calkowita(lista):
    """Sprawdza, czy wszystkie elementy w liście są liczbami całkowitymi."""
    return all(isinstance(x, int) for x in lista)


def suma_listy(lista):
    """Zwraca sumę wszystkich liczb w liście."""
    if not czy_lista_calkowita(lista):
        raise ValueError("Lista zawiera elementy niebędące liczbami całkowitymi!")
    return sum(lista)


def iloczyn_listy(lista):
    """Zwraca iloczyn wszystkich liczb w liście."""
    if not czy_lista_calkowita(lista):
        raise ValueError("Lista zawiera elementy niebędące liczbami całkowitymi!")

    iloczyn = 1
    for liczba in lista:
        iloczyn *= liczba
    return iloczyn