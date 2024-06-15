# 9.  Declara o variabila pentru o lista de cumparaturi care sa contina 4 produse la initializare. Mai
#      adauga inca 3 produse pe aceasta lista și apoi printeaza-o.

#varianta 1
lista_1 = ['ulei', 'zahar', 'paine', 'faina']
lista_2 = ['apa', 'portocale', 'banane']
cumparaturi = lista_1 + lista_2
print(cumparaturi)

#varianta 2
lista_1.append(lista_2)
print(lista_1)

#varianta 3
lista_cumparaturi = ['ulei', 'zahar', 'paine', 'faina']
lista_cumparaturi.extend(['apa', 'portocale', 'banane'])
print(lista_1)
