# 1. Scrieti un program care sa ceara userului un numar, apoi sa calculeze suma numerelor naturale
# pana la acel numar, folositi o structura repetitiva for

numar = int(input('Introduceti un numar natural: '))
suma = 0

for i in range(1,numar + 1):
    suma += i

print(f'Suma numerelor naturale pana la {numar} este {suma}')
