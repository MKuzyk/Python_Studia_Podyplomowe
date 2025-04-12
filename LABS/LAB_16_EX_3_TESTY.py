'''
Napisz, przetestuj i zastosuj własny moduł do obsługi list liczb całkowitych:

• zaimportuj utworzony moduł i skorzystaj z jego funkcji.
'''


import LAB_16_EX_2_modul_obsluga_liczb
import unittest


class TestListaUtils(unittest.TestCase):

    def test_czy_lista_calkowita(self):
        self.assertTrue(LAB_16_EX_2_modul_obsluga_liczb.czy_lista_calkowita([1, 2, 3, 4]))
        self.assertFalse(LAB_16_EX_2_modul_obsluga_liczb.czy_lista_calkowita([1, 2.5, 3, "4"]))

    def test_suma_listy(self):
        self.assertEqual(LAB_16_EX_2_modul_obsluga_liczb.suma_listy([1, 2, 3, 4]), 10)
        self.assertEqual(LAB_16_EX_2_modul_obsluga_liczb.suma_listy([-1, -2, -3]), -6)
        with self.assertRaises(ValueError):
            LAB_16_EX_2_modul_obsluga_liczb.suma_listy([1, 2.5, 3])

    def test_iloczyn_listy(self):
        self.assertEqual(LAB_16_EX_2_modul_obsluga_liczb.iloczyn_listy([1, 2, 3, 4]), 24)
        self.assertEqual(LAB_16_EX_2_modul_obsluga_liczb.iloczyn_listy([-1, 2, -3]), 6)
        self.assertEqual(LAB_16_EX_2_modul_obsluga_liczb.iloczyn_listy([5]), 5)
        self.assertEqual(LAB_16_EX_2_modul_obsluga_liczb.iloczyn_listy([]), 1)  # Iloczyn pustej listy to 1
        with self.assertRaises(ValueError):
            LAB_16_EX_2_modul_obsluga_liczb.iloczyn_listy([1, "2", 3])

if __name__ == '__main__':
    unittest.main()