# 10. Modifica lista, ex: in loc de mere sa apara alt fruct, și apoi elimina un produs, printeaza lista dupa
#       fiecare operatie

#varianta 1
lista_cumparaturi = ['ulei', 'zahar', 'paine', 'faina']
lista_cumparaturi[1] = 'miere'
lista_cumparaturi.remove('paine')
print(lista_cumparaturi)

#varianta 2
lista_cumparaturi_1 = ['ulei', 'zahar', 'paine', 'faina']
lista_cumparaturi[2] = 'chifle'
lista_cumparaturi_1.pop(-1)
print(lista_cumparaturi)
