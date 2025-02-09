'''
Załóżmy, że na pierwsze pole szachownicy kładziemy 1 ziarno zboża, na
drugie 2 ziarna, na trzecie 4 ziarna i na każde następne pole dwa razy
więcej ziaren niż na pole poprzednie. Napisz program, który zasymuluje
taką sytuację i zliczy sumę wszystkich ziaren na szachownicy
'''

print()
print("zadanie_3")
print()

#liczba pól na szachownicy
#1 2 4 8 16 32 64....

s=0

for i in range(64):
    s += 2 ** i
print("suma wszystkich ziaren na szachwnicy " + str(s))

# 1 ziarno 0.4 mg -> 0,0004g

# 1k = 1000g
# 1kg = 1t

tons = int(s * 0.0004 / 1000 / 1000)
print("to będzie ",tons," ton zboża")

#roczna produkcja przenicy na świecie to 782 mln ton "

years=int(tons/782_000_000)

print("ilość lat porzebna na wyprodukowanie zboża (swiatowa podaż) to: " , years)

#pociąg może przetransportować 2200 ton

trains=int(tons/2200)
print("ilość pociągów potrzebnych do przewiezienia zboża to: " , trains)
