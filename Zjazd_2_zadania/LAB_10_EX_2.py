'''Napisz program, który zasymuluje 16 rzutów kostką do gry a następnie
wyświetli poniższe informacje:
• zestaw wylosowanych wyników,
• wyrzucaną wartość za 8 razem,
• liczbę wyrzuconych szóstek,
• maksymalną liczbę wyrzuconych tych samych wartości pod rząd.
'''

import random
dice_rolls_total=16
rolls=[]

for i in range(dice_rolls_total):
    rolls.append(random.randint(1,6))

print("zbiór wyników po", dice_rolls_total, "rzutach kostką do gry:", rolls)

print("Za 8 razem wyrzucono wartość",str(rolls[8-1])+".")

sixes_total=0
for roll in rolls:
    if roll==6:
        sixes_total+=1
print("wyrzucono",sixes_total,"razy szóstkę")

in_row_value_tmp = rolls[0]
in_row_total_tmp = 0
in_row_value = 0
in_row_total = 0

for roll in rolls:
    if roll==in_row_value_tmp:
        in_row_total_tmp +=1

    else:
        in_row_value_tmp = roll
        in_row_total_tmp = 1

    if in_row_total_tmp > in_row_total:
        in_row_value=in_row_value_tmp
        in_row_total=in_row_total_tmp

print("pod rząd wyrzucono",in_row_total,"razy wartość", str(in_row_value)+".")
