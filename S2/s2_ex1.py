# 1. Fa un program care sa primeasca un numar intreg de la tastatura și sa printeze categoria in care se
#    afla: zero, pozitiv sau negativ. Indiciu: input interpreteaza ca string orice primeste de la tastatura.

numar = input('Indroduceti un numar: ')
numar = int(numar)
if numar == 0:
    print('Numarul este 0')
elif numar < 0:
    print('Numarul este negativ')
else:
    print('Numarul este pozitiv')