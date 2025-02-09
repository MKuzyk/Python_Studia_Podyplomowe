'''
Napisz program wyznaczający wartość n-tego bitu dla dowolnej liczby
całkowitej. Bity liczymy od 0, od najmniej znaczącego bitu.
'''

number=int(input("Podaj liczbę: "))
n=int(input("Podaj numer bitu: "))

mask=1<<n
result=number & mask
bit=int(bool(result))

print("bit na pozycji ", n, " dla liczby ",number," wynosi: ",str(bit)," .")

print("{:08b}".format(number))
print("{:08b}".format(mask))

print("-"*8)

print("{:08b}".format(result))

