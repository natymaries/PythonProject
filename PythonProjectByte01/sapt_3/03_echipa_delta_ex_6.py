# 6. Rezolvati exercitiul 5 utilizand structura iterativa while

lista_produse = {'pat': 2200, 'dulap': 990, 'masa': 535, 'birou': 450, 'coltar': 2990}
# metoda 1
# while lista_produse: # pana avem elemente in lista de produse
#     produs, pret = lista_produse.popitem() # popitem returneaza 2 valori (cheie, valoare): produs, pret =
#                                            # popitem sterge din dictionar elementul returnat si acesta devine tot mai mic
#     print(produs,pret)
#     print(len(lista_produse))

# metoda 2
# i = 0
# while i < len(lista_produse):
#     produs = list(lista_produse.keys())[i]
#     pret = list(lista_produse.values())[i]
#     print(produs, pret)
#     i += 1

# metoda 2.1
i = 0
produse = list(lista_produse.keys())
preturi = list(lista_produse.values())
while i < len(lista_produse):
    produs = produse[i]
    pret = preturi[i]
    print(produs, pret)
    i += 1

