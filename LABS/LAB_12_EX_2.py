'''
Napisz skrypt obliczający obwód, pole powierzchni i długość przekątnej dla
prostokątów o następujących długościach boków:
• 4 i 5,
• 2678 i 5678,
• 344555 i 788998
'''


# Pole = a*b

def pole(dł_pierwszego_boku,dł_drugiego_boku):
    pole=dł_pierwszego_boku * dł_drugiego_boku
    return pole

# Obwód = 2a +2b

def obwod (dł_pierwszego_boku,dł_drugiego_boku):
    obwod=((2*dł_pierwszego_boku) + (2*dł_drugiego_boku))
    return obwod

# Przekątna=(a**2 + b**2)**(1/2)

def przekatna(dł_pierwszego_boku,dł_drugiego_boku):
    przekatna=((dł_pierwszego_boku**2 + (dł_drugiego_boku**2)**(1/2)))
    return przekatna

a=4
b=5

c=2678
d=5678

e=344555
f=788998

pole1=pole(a,b)
obwod1=obwod(a,b)
przekatna1=przekatna(a,b)

print("Pole prostokąta o bokach " ,a,"cm oraz" ,b,"cm wynosi: ",pole1," cm" )
print("Obwód prostokąta o bokach ",a,"cm oraz",b,"cm wynosi: ",obwod1," cm" )
print("Przekątna prostokąta o bokach ",a,"cm oraz",b,"cm wynosi: ",przekatna1," cm" )

pole2=pole(c,d)
obwod2=obwod(c,d)
przekatna2=przekatna(c,d)

print("Pole prostokąta o bokach ",c," oraz",d," wynosi: ",pole2," cm" )
print("Obwód prostokąta o bokach ",c,"cm oraz",d,"cm wynosi: ",obwod2," cm" )
print("Przekątna prostokąta o bokach ",c,"cm oraz",d,"cm wynosi: ",przekatna2," cm" )

pole3=pole(e,f)
obwod3=obwod(e,f)
przekatna3=przekatna(e,f)

print("Pole prostokąta o bokach ",e," oraz",f," wynosi: ",pole3," cm" )
print("Obwód prostokąta o bokach ",e,"cm oraz",f,"cm wynosi: ",obwod3," cm" )
print("Przekątna prostokąta o bokach ",e,"cm oraz",f,"cm wynosi: ",przekatna3," cm" )