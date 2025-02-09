'''
Napisz, przetestuj i zastosuj własny moduł do obsługi list liczb całkowitych:
• stwórz modułu o dowolnej nazwie,
• dodaj funkcję weryfikującą czy podana lista zawiera wyłącznie liczby całkowite,
• dodaj funkcję sumującą wszystkie liczby z listy,
• dodaj funkcję zwracającą iloczyn wszystkich liczb z listy,
• dodaj testy weryfikujące poprawne działanie napisanych funkcji,
• zaimportuj utworzony moduł i skorzystaj z jego funkcji.
'''




# test_lista_utils.py

import unittest
import lista_utils

class TestListaUtils(unittest.TestCase):

    def test_czy_lista_calkowita(self):
        self.assertTrue(lista_utils.czy_lista_calkowita([1, 2, 3, 4]))
        self.assertFalse(lista_utils.czy_lista_calkowita([1, 2.5, 3, "4"]))

    def test_suma_listy(self):
        self.assertEqual(lista_utils.suma_listy([1, 2, 3, 4]), 10)
        self.assertEqual(lista_utils.suma_listy([-1, -2, -3]), -6)
        with self.assertRaises(ValueError):
            lista_utils.suma_listy([1, 2.5, 3])

    def test_iloczyn_listy(self):
        self.assertEqual(lista_utils.iloczyn_listy([1, 2, 3, 4]), 24)
        self.assertEqual(lista_utils.iloczyn_listy([-1, 2, -3]), 6)
        with self.assertRaises(ValueError):
            lista_utils.iloczyn_listy([1, "2", 3])

if __name__ == '__main__':
    unittest.main()




# main.py

import lista_utils

lista = [1, 2, 3, 4, 5]

if lista_utils.czy_lista_calkowita(lista):
    print(f"Suma elementów listy: {lista_utils.suma_listy(lista)}")
    print(f"Iloczyn elementów listy: {lista_utils.iloczyn_listy(lista)}")
else:
    print("Lista zawiera elementy niebędące liczbami całkowitymi.")
