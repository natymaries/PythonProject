# 9.  Scrie un program  care primește un numar indefinit de note de la utilizator separate de
# spatiu si calculează media acestora. Apoi afișează un mesaj corespunzător, în funcție de media obținută
# (admis sau respins).

def calculeaza_media():
    # luam un sir de note de la utilizator
    input_note = input('Introduceti notele separate de spatiu: ')
    lista_input = input_note.split()
    lista_input_float = []
    for nota in lista_input:
        lista_input_float.append(float(nota))
    # avem notele intr-o lista de numere intregi Cum calculam media si cum o stocam?
    # media = suma notelor / numarul notelor
    media = sum(lista_input_float) / len(lista_input_float)
    # afisam un mesaj corespunzator(admis/respins)
    if media >= 5:
        print(f'Ai fost admis cu media: {media}!')
    else:
        print(f'Ai fost respins cu media: {media}!')


calculeaza_media()
