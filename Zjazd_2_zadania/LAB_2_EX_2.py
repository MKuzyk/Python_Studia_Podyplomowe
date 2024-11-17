#Napisz skrypt wyznaczający ocenę jaką otrzyma student, ze względu na ilość
#otrzymanych punków z kolokwium:
# ocena bardzo dobra (5,0), jeżeli student otrzymał 95 lub więcej punktów,
# jeżeli punktów jest mniej niż 95, ale więcej niż 84 studentowi przysługuje ocena ponad dobra (4,5),
# ocena dobra (4,0) przyznawana jest dla ilości punktów z przedziału [70, 84],
# jeżeli student otrzymał więcej niż 60 ale mniej niż 70 to przysługuje mu ocena dość dobra (3,5),
# ocena dostateczna jest dla studentów z punktowym wynikiem równym przynajmniej 60 ale
#powyżej 50 punktów,
# wszystkie wyniki równe 50 i mniej punktów wiążą się z otrzymaniem oceny niedostatecznej (2.0).


ilosc_punktow=int(input("podaj ilość otrzymanych puntów: "))

if ilosc_punktow>=95:
    print("ocena bardzo dobra (5,0)")
elif ilosc_punktow>84 and ilosc_punktow<95:
    print("ocena ponad dobra (4,5)")
elif ilosc_punktow >=70 and ilosc_punktow<=84:
    print("ocena dobra (4,0)")
elif ilosc_punktow > 60 and ilosc_punktow < 70:
    print("ocena dość dobra (3,5)")
elif ilosc_punktow > 50 and ilosc_punktow <= 60:
    print("ocena dość dostateczna (3,0)")
else:
    print ("ocena niedostateczna")