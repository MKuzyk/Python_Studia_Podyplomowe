'''
Napisz skrypt, który znajdzie najczęściej występującą cyfrę w zbiorze.
Np. w zbiorze [4, 1, 2, 9, 4, 4] najczęściej występującą cyfrą jest 4,
występuje 3 razy
'''

digits=[1, 2, 3, 3, 4, 1, 2, 3]
frequency=[0,0,0,0,0,0,0,0,0,0]
for digit in digits:
    frequency[digit]+=1

print(digits)
print(frequency)

most_common = 0
for i in range(len(frequency)):
    if frequency[i]>frequency[most_common]:
        most_common=i

print("najczęściej wystepującą liczbą jest ",most_common," wystapiła ",frequency[most_common]," razy.")
