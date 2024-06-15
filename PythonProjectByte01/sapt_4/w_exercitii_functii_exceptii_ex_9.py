# tratarea exceptiilor pentru functiile exercitiilor de la weekend 3

def calculeaza_media_input():
    # luam un sir de note de la utilizator
    try:
        input_note = input('Introduceti notele separate de spatiu: ')
        if len(input_note) <= 0:
            raise ValueError

    except ValueError:
        print('Va rugam sa introduceti cel putin o nota')
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


#calculeaza_media_input()



def calculeaza_media_division():
    # luam un sir de note de la utilizator
    input_note = input('Introduceti notele separate de spatiu: ')
    lista_input = input_note.split()
    lista_input_float = []
    for nota in lista_input:
        lista_input_float.append(float(nota))
    # avem notele intr-o lista de numere intregi Cum calculam media si cum o stocam?
    # media = suma notelor / numarul notelor
    try:
        media = sum(lista_input_float) / len(lista_input_float)
        if media >= 5:
            print(f'Ai fost admis cu media: {media}!')
        else:
            print(f'Ai fost respins cu media: {media}!')
    except ZeroDivisionError:
        print('Nu ai introdus nici o nota')
    # afisam un mesaj corespunzator(admis/respins)


calculeaza_media_division()