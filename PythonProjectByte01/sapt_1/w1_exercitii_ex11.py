# 11. Fa din nou exercitiul anterior, in caz ca al doilea numar este 0 sa ceara utilizatorului sa introduca al doilea numar din nou

numar_1 = float(input('Introduceti primul numar: '))
numar_2 = float(input('Introduceti al doilea numar: '))

impartire = numar_1 / numar_2

if numar_2 != 0:
      print(impartire)
else:
      print('Reintroduceti numar_2: ')