'''
2. Napisz program pobierający od użytkownika 3 liczby zmiennoprzecinkowe.
Uwzględnij możliwość pomyłki użytkownika.
'''

print('Podaj 3 liczby zmiennoprzecinkowe!')

numbers = []
counter=1

while True:
    if counter > 3:
        break
    try:
        number=float(input("Podaj {} liczbę:".format(counter)))
        numbers.append(number)
        counter+=1
    except :
        print('Podana wartość jest nie poprawna, spróbuj ponownie!!!')

print(numbers)