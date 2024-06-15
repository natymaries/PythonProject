# 10. Scrieți un program care primește un număr întreg de la utilizator și calculează suma cifrelor acestuia.

numar = int(input('Introduceti un numar: '))
suma = 0

while numar != 0:
    cifra = numar % 10 # obtinem ultima cifra a numarului
    suma += cifra # la suma se adauga cifrele numarului de la final spre inceput
    numar //= 10
    print(suma, numar)

print(suma)