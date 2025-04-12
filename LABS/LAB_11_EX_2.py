'''
Napisz skrypt pobierający od użytkownika serię liczb całkowitych, a
następnie wyświetl je w kolejności malejącej pozbywając się wcześniej
duplikatów.
'''

numbers=[]
numbers_total=int(input("Podaj liczę elementów zbioru: "))

for i in (range(numbers_total)):
    number=int(input("Podaj "+str(i+1)+" element zbioru: "))
    numbers.append(number)

numbers.sort(reverse=True)
print(numbers)

# pierwszy sposób na usunięcie duplikatów
unique_numbers = list(set(numbers))
print(unique_numbers)

# drugi sposób na usunięcie duplikatów
numbers_without_duplicate=[]

for number in numbers:
    if number not in numbers_without_duplicate:
        numbers_without_duplicate.append(number)

numbers_without_duplicate.sort()
print(numbers_without_duplicate)