'''
Napisz skrypt, pobierający od użytkownika zbiór imion, w tym celu:
• skrypt powinien zapytać użytkownika o liczbę elementów zbioru,
• pobrać kolejne elementy i zapisać je do listy,
• wyświetlić w podsumowaniu jakie imiona pobrał od użytkownika
'''

names = []
total_elements=int(input("Podaj liczbę imion jakie zamierzasz wprowadzić: "))

for i in range(total_elements):
    names.append(input("Podaj "+str(i+1)+" imię: "))

print("Od użytkownika pobrano następujący zbiór imion: " ,names)