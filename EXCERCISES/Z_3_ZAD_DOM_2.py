'''
2. Chcemy ułożyć wieżę z puszek. Wieża składa się z poziomów, gdzie każdy wyższy poziom wymaga jednej puszki mniej
niż poziom na którym go zbudowano.
Korzystając z rekurencji napisz program, który pozwoli wyliczyć ilość potrzebnych puszek do wybudowania wieży o zadanym
poziomie
oraz ilość poziomów wieży jakie jesteśmy wstanie ułożyć z
dostępnej liczby puszek. Przykład: jeżeli chcemy ułożyć 3 poziomową wieżę
potrzebujemy 6 puszek a np. mając 10 puszek, ułożymy 4 poziomową wieżę.
'''

print('Funkcja pierwsza zwracająca ile puszek jest potrzebnych dla danej liczby poziomów.')

def number_of_cans(levels):
    total=0
    for number in range(levels+1):
        total += number
    print('Potrzeba' , total , 'puszek do budowy wieży!!')

number_of_cans (150)

print('Funkcja druga zwraca  ile poziomów mozna zbudować mając daną liczbę puszek.')

def number_of_levels(cans):
    level=0
    num=[]
    while sum(num) < cans and level+sum(num) < cans:
        level+=1
        num.append(level)
    print('Jeśli masz', cans, 'puszek możesz zbudować',level,'poziomy wieży!')

number_of_levels(11320)

print('Funkcja trzecia korzysta z rekurencji wyznaczając ilośc poziomów albo ilośc puszek potrzebnych do zbudowania wieży.')

def cans_or_levels (cans,levels):
    try:
        if cans is None:
            return number_of_cans(levels)
        elif levels is None:
            return number_of_levels(cans)
        elif cans is not None and levels is not None:
            return number_of_cans(levels)
            return number_of_levels(cans)
        else:
            print('Podaj któryś z agumentów funkcji! (cans - ilośc dostępnych puszek / levels - ilość poziomów')
    except:
        print('Podaj któryś z agumentów funkcji! (cans - ilośc dostępnych puszek / levels - ilość poziomów')

cans_or_levels(1000,None)
cans_or_levels(None,44)




