#Lista de numere intregi:
numere_intregi = [1, 2, 3, 4, 5]
print(numere_intregi)
print(type(numere_intregi))
numere_intregi.insert(0, 6)
#numere_intregi.insert(7) - insert are nevoie si de indice si de elementul adaugat
print(numere_intregi)

#Lista de float-uri:
numere_float = [1.5, 2.3, 4.7, 3.2, 5.9]
# printati primul element din lista
print(numere_float[0])
print(type(numere_float[0]))
# printati ultimul element
print(numere_float[-1])

index_last = len(numere_float)-1
print(index_last)
print(numere_float[index_last])

# sortati lista numere float folosind metoda sort
numere_float.sort(reverse=True)
print(numere_float)


print('--------------')

#Lista de șiruri de caractere:
cuvinte = ["Python", "este", "un", "limbaj", "de", "programare"]
print(len(cuvinte))
cuvant = '!'
cuvinte.append(cuvant)
print(cuvinte)
# definiti o lista goala
fructe = []
print(fructe)
#legume = list()
#declarati o lista cu 4 legume
legume_t = ('rosie', 'varza', 'ceapa', 'castravete')
legume = list(legume_t)
print(legume)
print(type(legume_t))

#Lista mixta de diferite tipuri de date:
mixt = [1, "Python", 3.14, True, [1, 2, 3]]
total = legume + mixt
print(total)
mixt.extend(legume)
print(mixt)
# printati al doilea element din lista care se afla in lista mixt
print(mixt[4][1])

mixt.reverse()
print(mixt)