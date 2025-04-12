#Npisz skrypt, który oblicza ile warta byłaby inwestycja na kwotę
#14 000 zł, gdyby jej wartość zwiększyła się w pierwszym roku o 40%, w
#drugim roku zanotowała stratę w wysokości 1500 zł, a w trzecim roku
#zwiększyła się o 12%.

a=.4
b=1500
c=.12
d=14_000

print("Wartość inwestycji " + str(d)," po wzroscie w 1 roku o "+str(a),
      " stracie w drogim roku w wysokosci "+str(b)," oraz wzroscie w 3 roku roku o "+str(c)
      ,"wyniosla ",(d*(1+a)-1500)*(1+c))