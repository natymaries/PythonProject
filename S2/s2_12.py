# 6. Creaza un program care sa ceara 3 numere intregi și sa returneze care dintre ele este cel mai mare

numar_1 = int(input('Introduceti primul numar: '))
numar_2 = int(input('Introduceti al doilea numar: '))
numar_3 = int(input('Introduceti al treilea numar: '))

if numar_1 > numar_2 and numar_1 > numar_3:
      print(f'Numarul {numar_1} e cel mai mare')
elif numar_2 > numar_1 and numar_2 > numar_3:
      print(f'Numarul {numar_2} e cel mai mare')
else:
      print(f'Numarul {numar_3} e cel mai mare')