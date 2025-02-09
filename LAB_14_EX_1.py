'''
1. Napisz wyszukiwarkę numerów telefonów:
• zdefiniuj słownik par imię -> numer telefonu,
• zapytaj użytkownika o imię,
• wyświetl użytkownikowi numer telefonu lub informację o jego braku.
'''

phones={"Tomek":503128792,
        "Ada":666555999,
        "Ola":777999222,
        "Maria":666828792,
        "Barbara":765241888
        }

name=input("Podaj osobę: ")

if name in phones.keys():
    print("Numer telefonu to:",phones[name])
else:
    print("nie znaleziono osoby w słowniku!")



while True:
    name_2=input("Podaj imię: ")
    if name_2 =="":
        break
    if name_2 in phones:
        print("Telefon:",phones[name_2])
    else:
        print("Nie znaleziono numeru telefonu!")