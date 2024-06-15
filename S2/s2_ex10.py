# 10. Scrie un program care sa primeasca doua numere și sa returneze rezultatul impartirii primului
#       numar la al doilea. Programul va returna o eroare și se va opri in cazul in care al doilea numar
#       introdus este 0 inainte ca sa execute operatia de impartire. Indiciu: foloseste un assert.

numar_1 = float(input('Introduceti primul numar: '))
numar_2 = float(input('Introduceti al doilea numar: '))

assert numar_2 != 0 'Numarul trebuie sa fie diferit de 0'
impartire = numar_1 / numar_2

print(f'Rezultatul impartirii numarului {numar_1} la numarul {numar_2} este: {impartire}')