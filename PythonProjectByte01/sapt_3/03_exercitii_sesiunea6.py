# Parcurgeti un sir de caractere si afisati fiecare caracter pe o linie separata

sir = 'python'
for litera in sir:
    print(litera, end='')

# Parcurgeti o lisa de numere si afisati dublul fiecarui numar folosind un foreach

lista_numere = [1, 2, 3, 4, 5, 6]
for numere in lista_numere:
    print(numere * 2)

# Parcurgeti o lisa de numere si afisati dublul fiecarui numar folosind un for

lista_numere = [1, 2, 3, 4, 5, 6]
for i in range(len(lista_numere)):
    print(lista_numere[i] * 2)

# Parcurgeti o lisa de numere si salvati dublul fiecarui element intr-o lista noua cu foreach
# variabila de loop reprezinta elementele unei structuri de date

lista_dublu = []
for numar in lista_numere:
    lista_dublu.append(numar * 2)
print(lista_numere)
print(lista_dublu)

# Parcurgeti o lisa de numere si salvati dublul fiecarui element intr-o lista noua cu for
# variabila de loop reprezinta indicele/pozitia dintr-o structura de date

for i in range (0, len(lista_numere)):
    lista_dublu[i] = lista_numere[i] * 2
print(lista_numere)
print(lista_dublu)

# Parcurgeti un tuplu de stringuri si afisati numarul de caractere al fiecarui element

fructe = ('apple', 'banana', 'cherry')

for fruct in fructe:
    print(len(fruct))

print('------------------------------------')
# Parcurgeti un set care contine diferite tipui de date si printati doar elementele de tip intreg

elemente = {'123', 1, 2, 3.14}

for element in elemente:
    if isinstance(element, int):
        print(element)
    else:
        print('Elementul nu este un numar intreg')


# Parcurgeti un dictionar si afisati cheile si valorile elementelor separate de '-'

dictionar = {'a' : 1, 'b' : 2, 'c': 3 }

for cheie, valoare in dictionar.items():
    print(cheie, '-', valoare)


# Parcurgeti un sir si afisati caracterele in ordine folosind un while

sir = ['Ana are mere']
# setarea conditiei
dim_sir = len(sir)
i = 0
# while + conditie
while i < dim_sir:
    print(sir[i])
# modificarea conditiei in interiorul blocului de cod
    i += 1

print('------------------------------------')
# Parcurgeti un sir si afisati caracterele in ordine inversa folosind un while

sir = ['Ana are mere']
# setarea conditiei
dim_sir = len(sir)-1
j = len(sir)
# while + conditie
while j >= 0:
    print(sir[j])
# modificarea conditiei in interiorul blocului de cod
    j -= 1

print(sir)

# Parcurgeti un sir de la sfarsit spre inceput si construiti un alt string
# Rezultatul trebuie sa fie identic cu o segmentare de inversare

anti_sir = sir[::-1]
print(anti_sir)

anti_sir_manual = ''
# setarea conditiei
k = len(sir)-1
# while + conditie
while k >= 0:
    #adaugam/concatenam in sirul manual caracterele de pe pozitia k din sir
    anti_sir_manual += sir[k]
# modificarea conditiei
    k -= 1
print(anti_sir_manual)