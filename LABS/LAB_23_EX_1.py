''' Zaprojektuj klasę reprezentującą osobę (Person) wg założeń:
• każdy obiekt tej klasy powinien posiadać właściwości: imię oraz wiek,
• zabezpiecz właściwości obiektu przed przypadkowym nadpisaniem,
• ustawienie odpowiednich właściwości obiektu powinno następować podczas jego tworzenia,
• każdy obiekt tej klasy powinien móc wykonać akcję przedstawienia się.
'''


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def introduce(self):
        print("Cześć, jestem ", self.__name, "i mam", self.__age, "lat/a.")

person_list=[]

person_list.append(Person("Michal Kuzyk", 40))
person_list.append(Person("Tomasz Pysz", 46))
person_list.append(Person("Aleksandra Chatlas", 38))
person_list.append(Person("Aleksandra Ptak", 18))
person_list.append(Person("Maciej Czech", 35))

for Person in person_list:
    print("Osoba: ",Person.getName(),"/ Wiek osoby: ",Person.getAge())

for Person in person_list:
    print("Cześć nazywam się ",Person.getName(),", mam ",Person.getAge(),": lat.")

for Person in person_list:
    Person.introduce()
