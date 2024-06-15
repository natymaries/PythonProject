# 8. Creaza un program care sa primeasca un numar intreg de la tastatura și sa determine daca este par sau impar

numar = int(input('Introdu un numar intreg: '))

if numar % 2 == 0:
      print(f'Numarul {numar} este par')
else:
      print(f'Numarul {numar} este impar')