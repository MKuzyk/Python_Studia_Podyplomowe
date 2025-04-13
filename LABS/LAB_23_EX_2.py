'''
Program dices -- symulujący rzuty dwiema kostkami do gry
Rzucamy dwiema kostkami do momentu aż nie wyrzucimy dubletu
Dokonaj odpowiednich zmian w programie do rzucania kośćmi do gry (dices.py), aby
zabezpieczyć zmienne instancji przed przypadkowym nadpisaniem (enkapsulacja).
'''

import random

class Dices:

    def __init__(self):
        self.__value = None

    def get_value(self):
        return self.__value

    def roll(self):
        self.__value = random.randint(1, 6)

    def __str__(self):
        return f"[{(self.__value)}]" # przykład: [6]

class DicePair:

    def __init__(self):
        self.__pair = [Dices(), Dices()]

    def roll(self):
        self.__pair[0].roll()
        self.__pair[1].roll()

    def __str__(self):
        return str(self.__pair[0]) + str(self.__pair[1])

    def is_double(self):
        return self.__pair[0].get_value() == self.__pair[1].get_value()

dices = DicePair()
while True:
    dices.roll()
    print(dices)
    if dices.is_double():
        break



