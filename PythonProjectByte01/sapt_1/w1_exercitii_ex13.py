# 7. Scrie un program care sa primeasca un cuvant și printeze daca acel cuvant este palindrom sau nu.

cuvant = input('Scrieti un cuvant: ')

if cuvant == cuvant[::-1]:
      print(f'Cuvantul {cuvant} este palindrom')
else:
      print(f'Cuvantul {cuvant} nu este palindrom')