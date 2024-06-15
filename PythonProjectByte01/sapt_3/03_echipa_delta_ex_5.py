# 5. Folositi un for each ca sa printati cheile și valorile unui dictionar ce contine 5 perechi de cheie și valoare.

lista_produse = {'pat': 2200, 'dulap': 990, 'masa': 535, 'birou': 450, 'coltar': 2990}

for produs, pret in lista_produse.items():
    print(f'Produsul {produs} costa {pret} lei')
