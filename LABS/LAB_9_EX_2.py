'''
Udowodnij, że w zbiorze liczb z zakresu 1-100, jest 11 liczb, które są
parzyste i jednocześnie większe od 90, a gdy są nieparzyste, to
przynajmniej dzielą się przez 9.
'''

counter=0

for i in range (1,101):
    if i % 2==0 and i>90 or i % 2!=0 and i % 9==0:
        counter+=1
print(counter)
