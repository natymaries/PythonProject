# 14. Dupa printarea dictionarului da controlul utilizatorului sa specifice un produs, daca produsul se afla
#       pe lista de produse atunci programul va printa: “Produsul {produs} se afla pe lista”, in caz ca
#       produsul introdus nu se afla pe lista, intreaba utilizatorul cantitatea și apoi adauga-l in dictionar și
#       printeaza pe ecran: “Produsul {produs} a fost pus pe lista cu {num_unitati} unitati”

lista_cumparaturi = {'ulei': 6, 'zahar': 2, 'paine': 3, 'faina': 1, 'apa': 10, 'portocale': 2, 'banane': 4}
produs = input('Alege un produs: ')
if produs in lista_cumparaturi:
    print(f'Produsul {produs} se afla pe lista')
else:
    num_unitati = input('Introdu cantitatea produsului ales: ')
    lista_cumparaturi[produs] = num_unitati
    print(f'Produsul {produs} a fost pus pe lista cu {num_unitati} unitati')
    print(lista_cumparaturi)


