'''
Napisz program pobierający od użytkownika liczbę całkowitą i zwracający
liczbę jedynek w ciągu bitów reprezentujących tę liczbę.
'''

number=int(input("Podaj liczbę całkowitą: "))


print("liczba jedyne w ciągu bitów reprezentujących tę liczbę t: ")
print("{:08b}".format(number))