# 12. Dat fiind un set de numere intregi cauta numarul introdus de utilizator, odata gasit numarul respectiv
# iesi din structura repetitiva si printeaza: "Numarul x a fost gasit" sau "Numaru x nu a fost gasit"

numere ={2,3,4}

numar_introdus = int(input('Introduceti un numar: '))

if numar_introdus in numere:
    print(f'Numarul {numar_introdus} a fost gasit.')
else:
    print(f'Numarul {numar_introdus} nu a fost gasit.')
