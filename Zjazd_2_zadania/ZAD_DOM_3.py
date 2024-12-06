'''
Napisz program pobierający od użytkownika liczbę całkowitą i zwracający
liczbę jedynek w ciągu bitów reprezentujących tę liczbę.
'''
from itertools import count

number=int(input("Podaj liczbę całkowitą: "))
print("{:08b}".format(number))
print(len("{:08b}".format(number)))

bits=[]

for i in range(len("{:08b}".format(number))):
    mask = 1 << i
    result = number & mask
    bit = int(bool(result))
    bits.append(bit)
    i += 1
print(bits)

total=0

for bit in bits:
    if bit==1:
        total+=1


print("liczba jedynek w ciągu bitów reprezentujących tę liczbę t: ",str(total))