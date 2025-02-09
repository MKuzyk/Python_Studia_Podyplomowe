'''
3. Napisz skrypt symulujący uproszczone działanie gry losowej "jednoręki bandyta",
w tym celu:
• za każdym "pociągnięciem" losuj 3 litery ze zbioru od A do E,
• kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
• wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
• przemyśl jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także
większą liczbę liter.
'''

# zbiór [A,B,C,D,E]

#print(ord("B"))
#print(chr(66))

import random

FIRST_SYMBOL="A"
LAST_SYMBOL="E"
NUMBER_OF_LETTERS=3

def draw_letter():
    return chr(random.randint(ord(FIRST_SYMBOL), ord(LAST_SYMBOL)))

def draw_row():
    return [draw_letter() for _ in range(NUMBER_OF_LETTERS)]

def check_letter(row):
        if row[0]==row[1]==row[2]:
            return True
        return False
# mechanizm wywołujący losowanie do momentu aż trafimy

counter=1
while True:
    row=draw_row()
    print(row,counter)
    if check_letter(row):
        break
    counter+=1
