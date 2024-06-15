# 8. Scrieți un program care să calculeze suma numerelor citite de la utilizator până când acesta introduce un număr negativ.
# odata ce numărul introdus este negativ programul trebuie sa iasa din bucla while și sa printeze rezultatul.

suma = 0

while True:
    numar_introdus = int(input('Introduceti numar: '))
    if numar_introdus < 0:
        break
    suma += numar_introdus
    print(suma)