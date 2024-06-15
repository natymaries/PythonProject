# 16. Da controlul utilizatorului ca sa introduca o forma geometrica. Folosind cuvantul cheie in, verifica
#       daca forma respectiva este prezenta in tuplu obtinut dupa concatenarea celor doua tupluri. Și sa
#       raspunda corespunzator : ’{Forma_geometrica} se afla in tuplu’

forme_geometrice_1 = ('patrat', 'dreptunghi', 'triunghi', 'romb')
forme_geometrice_2 = ('hexagon', 'trapez', 'pentagon')
forme_geometrice = forme_geometrice_1 + forme_geometrice_2

forma_geometrica = input('Introduceti o forma geometrica: ')

if forma_geometrica in forme_geometrice:
    print(f'{forma_geometrica} se afla in tuplu')
else:
    print(f'{forma_geometrica} nu se afla in tuplu')
