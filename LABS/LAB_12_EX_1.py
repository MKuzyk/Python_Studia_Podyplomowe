'''
Napisz funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak, dowolną
ilość razy, w poziomie lub w pionie
'''

znak_podany = str(input("Podaj znak do wyświetlenia: "))
ilość_podana = int(input("Podaj ile razy znak ma zostać wyświetlony : "))
ver_hor=int(input("Czy tekst należy wyświetlić w pionie? (Podaj 0 jeśli tak, w przeciwnym wypadku podaj 1) : "))

def znaki(znak,ilość,ver_or_hor):
    if ver_hor ==1:
        print(znak * ilość)
    else:
        for i in range(ilość_podana):
            print(znak_podany)
            print(" ")

znaki(znak_podany,ilość_podana,ver_hor)