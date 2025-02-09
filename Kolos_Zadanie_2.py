def usun_duplikaty(lista):
    return list(set(lista))

lista = [1, 'Michal', 'Michal',2, 3, 'Zosia','Zosia',4, 4, 5, 6, 6]
unikalne = usun_duplikaty(lista)
print(unikalne)