'''
Program dices -- symulujący rzuty dwiema kostkami do gry
Rzucamy dwiema kostkami do momentu aż nie wyrzucimy dubletu
'''

import random

class Dices:

    def __init__(self):
        self.value = None

    def roll(self):
        self.value = random.randint(1, 6)

    def __str__(self):
        return f"[{(self.value)}]" # przykład: [6]

class DicePair:

    def __init__(self):
        self.pair = [Dices(), Dices()]

    def roll(self):
        self.pair[0].roll()
        self.pair[1].roll()

    def __str__(self):
        return str(self.pair[0]) + str(self.pair[1])

    def is_double(self):
        return self.pair[0].value == self.pair[1].value

dices = DicePair()
while True:
    dices.roll()
    print(dices)
    if dices.is_double():
        break
