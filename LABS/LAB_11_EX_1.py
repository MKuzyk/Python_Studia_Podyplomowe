'''
Napisz skrypt symulujący grę losową:
• użytkownik obstawia 6 liczb z 49,
• program losuje 6 liczb z 49,
• użytkownik dostaje informacje o ilości trafień.
'''

import random
number_list=[]

print("Podaj 6 liczb z 49!!")

for i in range(6):
    number_list.append(int(input("Podaj "+str(i+1)+" liczbę: ")))

draw_number=[]

for i in range(6):
    draw_number.append(random.randint(1,49))

number_list.sort()
draw_number.sort()

print("wybrane liczby to :",number_list)
print("wylosowane liczby to :",draw_number)

number_total=0

for number in number_list:
    if number in draw_number:
        number_total+=1
        print("Udało ci się trafić: ",str(number_total)," liczb")