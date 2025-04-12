'''
1. Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.
'''

numbers=[]
i=0



while True:
    element = input("Podaj " + str(i + 1) + " element który mam wstawić do listy: ")

    if element == "":
        break
    else:

        numbers.append(int(element))
    i+1
print ("Lista zawiera elementy: ",numbers)

exp=int(input("Podaj do jakiej potęgi chcesz podnieść elementy listy:"))

#pierwszy sposób

def pow2 (numbers,exp):
    results=[]
    for i in range (len(numbers)):
        results.append(numbers[i]**exp)
    return results

print(pow2(numbers,exp))

# drugi sposób

def power_numbers(numbers,exp):
    for i in range (len(numbers)):
        numbers[i]=numbers[i] ** exp
    return numbers

print(power_numbers(numbers,exp))