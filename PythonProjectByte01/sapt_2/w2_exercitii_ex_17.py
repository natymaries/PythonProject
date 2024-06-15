# 17. Cere-i utilizator un numar cu sugestia (1 - len(tuplu_concatenat). Daca introduce un numar in rangul
#      asta printeaza in consola: “La pozitia {pozitie_introdusa} se afla un {forma_geometrica}”, in caz contrar
#      printeaza: “Indexul introdus este invalid!”

forme_geometrice_1 = ('patrat', 'dreptunghi', 'triunghi', 'romb')
forme_geometrice_2 = ('hexagon', 'trapez', 'pentagon')
forme_geometrice = forme_geometrice_1 + forme_geometrice_2

valoare_introdusa = int(input(f'Introduceti o valoare intre 1 si {len(forme_geometrice)}: '))

if valoare_introdusa >= 1 and valoare_introdusa <= len(forme_geometrice):
    forma_geometrica = forme_geometrice[valoare_introdusa - 1]
    print(f'La pozitia {valoare_introdusa} se afla un {forma_geometrica}')

else:
    print('Indexul introdus este invalid!')

