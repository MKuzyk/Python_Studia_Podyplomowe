'''
2. Korzystając z rekurencji wypisz na ekranie tabliczkę mnożenie do 100.
'''

print("Tabliczka mnożenia na 100:")

def show_operation(a,b):
    print(a, "x",b,"=",a*b)
    if a==10 and b==10:
        return
    elif a==10:
        show_operation(1,b+1)
    else :
        show_operation(a+1,b)

show_operation(1,1)