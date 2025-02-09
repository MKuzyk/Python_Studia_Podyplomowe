'''
Rozszyfruj poniższą wiadomość wiedząc, że została ona zaszyfrowana szyfrem
cezara z parametrem przesunięcia równym 3.
VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ
'''

code='VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ'

# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# XYZABCDEFGHIJKLMNOPQRSTUVW

delta=3

'''
for c in range(ord('A'), ord('Z')+1):
    print(chr(c),end="")

print()

for c in range(ord('A') + delta, ord('Z')+1+ delta):
    if c > ord('Z'):
        c-= ord('Z') - ord('A') +1
    print(chr(c),end="")
'''

def decode_letter(letter, delta):
    if letter < 'A' or letter > 'Z':
        return letter
    n = ord(letter) - delta
    if n < ord('A'):
        n+=ord('Z') - ord('A') +1
    return chr(n)

#print(decode_letter('J', delta))

def decode(string,delta):
    decoded = ""
    for letter in string:
        decoded += decode_letter(letter, delta)
    return decoded

print(decode(code,delta))

