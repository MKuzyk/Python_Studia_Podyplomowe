'''
• dodaj funkcję weryfikującą czy podana lista zawiera wyłącznie liczby całkowite (nazwa funkcji 'czy_lista_calkowita')
• dodaj funkcję sumującą wszystkie liczby z listy (nazwa : 'suma_listy')
• dodaj funkcję zwracającą iloczyn wszystkich liczb z listy (nazwa : 'suma_listy')
• zaimportuj utworzony moduł i skorzystaj z jego funkcji.
'''

import LAB_16_EX_2_modul_obsluga_liczb

lista = [2, 3, 4]

if LAB_16_EX_2_modul_obsluga_liczb.czy_lista_calkowita(lista):
    print(f"Czy lista zawiera tylko liczy całkowite ? : {LAB_16_EX_2_modul_obsluga_liczb.czy_lista_calkowita(lista)}")
    print(f"Suma elementów listy: {LAB_16_EX_2_modul_obsluga_liczb.suma_listy(lista)}")
    print(f"Iloczyn elementów listy: {LAB_16_EX_2_modul_obsluga_liczb.iloczyn_listy(lista)}")
else:
    print("Lista zawiera elementy niebędące liczbami całkowitymi.")





