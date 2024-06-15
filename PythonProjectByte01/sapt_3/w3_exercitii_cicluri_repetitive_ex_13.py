# 13. Scrie un program care sa gaseasca minimul si maximul intr-o lista de numere decimale,
#  fara sa foloseasca functiile min si max ale listelor in python

numere = [float(x) for x in input('Introduceti numerele: ').split()]

minim = numere[0]
maxim = numere[0]


for numar in numere:
    if numar < minim:
        minim = numar
    if numar > maxim:
        maxim = numar

print(f'Minimul din lista este: {minim}')
print(f'Maximul din lista este: {maxim}')

