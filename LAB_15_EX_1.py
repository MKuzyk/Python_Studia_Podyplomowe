'''
1. Utwórz funkcję o nazwie safe_int(), która pobiera pojedynczy argument arg.
Jeśli to możliwe, funkcja powinna przekonwertować podany argument na typ int
i zwrócić go. Jeśli jednak nie jest to możliwe (tj. jeśli wystąpi wyjątek), funkcja
powinna zwrócić None.
'''

def safe_int(arg):
    try:
        return int(arg)
    except:
        return None

print(safe_int(1))
print(safe_int('1'))
print(safe_int(22.1))
print(safe_int('dwa'))