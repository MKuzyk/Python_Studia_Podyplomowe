'''
1. Napisz funkcję, która pozbędzie się z listy powtarzających się elementów.
'''

lista_1=[22,22,22,10,10,1,2,2,3,3,3,3,3,4,5,5,5,5,5,5,5,5]
Lista_2=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,'Michal','Michal','Ala','Ala']
Lista_3=['Ewa','Ewa','Ola','Ola','Tomek','Tomek']

print('Pełne listy z duplikatami to :')

print(lista_1)
print(Lista_2)
print(Lista_3)

def unique_elements(list_name):
    elements=list(set(list_name))
    print(elements)

print()
print('Listy bez duplikatów to :')

unique_elements(lista_1)
unique_elements(Lista_2)
unique_elements(Lista_3)