# 1. creeaza o functie care sa printeze la multi ani si apoi apeleaz-o
# def nume_functie(param 1, param 2, ...):

# def ureaza_lamultiani():
#     print('La multi ani!')
#
#
# ureaza_lamultiani()

# 2. Cum printam la multi ani de 4 ori?
# Varianta 1: apelam medoda de 4 ori
#
# ureaza_lamultiani()
# ureaza_lamultiani()
# ureaza_lamultiani()

# Varianta 2: cream o structura repetitiva in care sa apelam metoda
print('-------' * 10)


# for i in range(4):
#     ureaza_lamultiani()


# 3. creaza o functie care sa primeasca un nume de la utilizator si sa printeze numele
# cu prima litera in majuscula

# def printeaza_nume():
#     nume = input('Introdu un nume: ')
#     nume_majuscule = nume.capitalize()
#     print(nume_majuscule)
#
# # apelam metoda printeaza_nume:
# printeaza_nume()

# 4. Fa o a doua varianta ca aceasta sa primeasca un argument si sa printeze la multi ani

def ureaza_cu_dedicatie(nume):
    print(f'La multi ani {nume} !')


# ureaza_cu_dedicatie('Naty')

# 5. Fa o alta versiune a exercitiului 3 care sa returneze un nume
# introdus de utilizator cu prima litera in majuscule

# def returneaza_nume():
#     nume = input('Introdu un nume: ')
#     nume_m = nume.capitalize()
#     return nume_m

# print(returneaza nume())
# nume = returneaza_nume()
# print(nume)

# 6. Foloseste valoarea returnata de returneaza_nume pt a apela functia de la ex.4

# ureaza_cu_dedicatie(nume)

# 7. Scrie 2 functii care sa primeasca un numar intreg care reprezinta latura unui patrat
# prima functie returneaza aria patratului iar a doua perimetrul lui

def calculeaza_aria(latura):
    return latura * 2


def calculeaza_perimetrul(latura):
    return latura * 4


latura = 4
calculeaza_aria(latura)
aria = calculeaza_aria(latura)
print(f'Aria unu patrat cu latura {latura} este {aria}.')

perimetru = calculeaza_perimetrul(latura)
print(f'Perimetrul unu patrat cu latura {latura} este {perimetru}.')


# 8. Scrie o functie care sa primeasca date de la utilizator. In cazul in care datele introduse formeaza
# un cuvant atunci se va apela metoda exercitiului 4, in cazul in care datele introduse sunt un numar intreg
# se vor apela metodele exercitiului 7.

def trateaza_inputul_utilizatorului():
    date = input('Introduceti un numar sau un nume: ')
    # incercam sa transformam datele introduse intr-un numar intreg - try:
    try:
        numar = int(date)
        print(calculeaza_aria(numar))
        print(calculeaza_perimetrul(numar))
    # daca primim eroare inseamna ca datele reprezinta un nume - except:
    except ValueError:
        ureaza_cu_dedicatie(date)


trateaza_inputul_utilizatorului()
