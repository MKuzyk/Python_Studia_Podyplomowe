#Wyznacz zysk z 3 letniej lokaty bankowej wg założeń:
# inwestowane środki 46 567,00 zł
# stałe oprocentowanie roczne 7.5%
# coroczna kapitalizacja odsetek
# w obliczeniach zastosuj złożony operator przypisania

a=46_567
b=3
c=0.075

print("Zysk z 3 letniej lokaty bankowej procentowanej ",str(c)," wynosi ",a*((1+c)**b))

