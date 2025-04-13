'''
Wyświetl polski alfabet (tylko małe litery, także litery ze znakami diakrytycznymi)
wraz z punktami kodowymi dla każdej litery.
'''

# alfabet (małe litery)
alfabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"

# Wyświetlenie liter wraz z kodami Unicode
for litera in alfabet:
    print(f"{litera} ->", ord(litera))