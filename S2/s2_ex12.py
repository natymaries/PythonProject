# 5. Fa un program care sa primeasca doua numere cu zecimale de la utilizator și sa determine care dintre cele doua
#    numere este mai mare. Foloseste stringuri formatate pentru a printa și numerele, ex: 5 este mai mare ca 4

numar_1 = float(input('Introduceti primul numar: '))
numar_2 = float(input('Introduceti al doilea numar: '))

if numar_1 > numar_2:
      print(f'{numar_1} mai mare decat {numar_2}')
else:
      print(f'{numar_2} mai mare decat {numar_1}')