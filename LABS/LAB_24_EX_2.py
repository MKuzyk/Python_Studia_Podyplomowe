'''
Dokonaj modyfikacji programu ze zwierzętami (animals.py):
• dodaj 2 kolejne dowolne zwierzęta,
• dodaj metody symulujące wydawanie dźwięków przez zwierzęta np. wyświetlając napis "miau",
• dodaj właściwość pozwalającą zliczać wszystkie zwierzęta,
• uwzględnij sumę wszystkich zwierząt oraz wydawane przez zwierzę dźwięki w metodzie introduce().
'''

class Animal:
    all_counter=0

    def __init__(self):
        Animal.all_counter+=1

    def introduce(self):
        print(f"Jestem typem {self.type} mam na imię {self.name}, jest nas {self.counter},a wszystkich zwierząt jest {self.all_counter},{self.make_sound()}.")

    def intrduce_2(self):
        print(self.make_sound)

class Dog(Animal):
    type = "pies"
    counter=0

    def __init__(self, name):
        super().__init__()
        self.name=name
        Dog.counter+=1

    def make_sound(self):
        return "Hau"

class Cat(Animal):
    type = "kot"
    counter = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        Cat.counter += 1

    def make_sound(self):
        return "miau"

class Horse(Animal):
    type = "koń"
    counter = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        Horse.counter += 1

    def make_sound(self):
        return "ihaaaa"

class Mouse(Animal):
    type = "mysz"
    counter = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        Mouse.counter += 1

    def make_sound(self):
        return "mi"

class Pig(Animal):
    type = "świnka"
    counter = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        Pig.counter += 1

    def make_sound(self):
        return "hrum"

class Bird(Animal):
    type = "ptak"
    counter = 0

    def __init__(self, name):
        super().__init__()
        self.name = name
        Bird.counter += 1

    def make_sound(self):
        return "pi"

animals=[
    Dog("Burek"),
    Dog("Czarek"),
    Cat("Filemon"),
    Cat("Lucek"),
    Horse("Karino"),
    Mouse("Mickey"),
    Mouse("Mouse"),
    Pig("Piggy"),
    Bird("Tuptuś")
    ]


for animal in animals:
    animal.introduce()







