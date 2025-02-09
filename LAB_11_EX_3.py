'''
Napisz skrypt symulujący rozgrywkę gry w szachy, w tym celu:
• stwórz wirtualną szachownicę,
• na wirtualnej szachownicy rozmieść losowo 2. dowolne figury szachowe i 3. piony,
• zaprezentuj użytkownikowi stan wirtualnej szachownicy.
'''

import random

BLANK_SQUARE="--"
pieces=["WP","BP","BP","BT","WQ"]

chessboard=[[BLANK_SQUARE for _ in range(8)] for _ in range(8)]

print(chessboard)

counter=0

while counter<5:
    row=random.randint(0,7)
    col=random.randint(0,7)
    if chessboard[row][col]==BLANK_SQUARE:
        chessboard[row][col]=pieces[counter]
        counter+=1

for row in range(len(chessboard)):
    if row==0:
        print(" ","A","B","C","D","E","F","G","H",sep="  ")
    print(row +1,end=" ")
    for col in range(len(chessboard[row])):
        print(chessboard[row][col],end=" ")
    print()