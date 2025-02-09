'''
Korzystając z odpowiednich modułów napisz skrypt realizujący następujące
zadania:
• wyświetl informacje o procesorze komputera,
• wylosuj 3 niepowtarzalne liczby ze zbioru 1-10,
• wyznacz sinus 90 stopni.
'''


import platform
import random
import math

# Wyświetlenie informacji o procesorze
print("Informacje o procesorze:", platform.processor())

# Wylosowanie 3 niepowtarzalnych liczb ze zbioru 1-10
liczby = random.sample(range(1, 11), 3)
print("Wylosowane liczby to:", liczby)

# Wyznaczenie sinusa 90 stopni
sin_90 = math.sin(math.radians(90))
print("Sinus 90 stopni wynosi:", sin_90)