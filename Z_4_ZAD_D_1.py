'''
Napisz funkcję sprawdzającą, czy podany ciąg znaków jest palindromem
(czy czyta się tak samo od przodu i od tyłu). Ignoruj wielkość liter oraz spacje.
'''

def czy_palindrom(string):
# Usuwam spacje i zamieniam litery na małe

    string = string.replace(" ", "").lower()

    #  "slicing"
    return string == string[::-1]

tekst = "łapał za kran a kanarka złapał"

if czy_palindrom(tekst):
    print("Ciąg jest palindromem.")
else:
    print("Ciąg nie jest palindromem.")
