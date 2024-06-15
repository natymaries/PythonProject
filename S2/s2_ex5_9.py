# 5. Compune opt variabile  și doua constante care sa descrie o masina și atribuiele valori

marca = 'Volkswagen'
model = 'Golf_4'
an_fabricatie = 2003
culoare = 'gri'
numar_usi = 4
cai_putere = 101
viteza_maxima = 200
pret = 3000
TARA_FABRICATIE = 'Germania'
GARANTIE = 5

# 6. Gandeste-te la elementele care descriu o persoana și initializeaza sapte variabile și trei constante

PRENUME = 'Naty'
NUME = 'Maries'
ANUL_NASTERII = 1994
varsta = 29
greutatea = 90
inaltimea = 1.80
ocupatie = 'inginer'
stare_civila = 'casatorit'
educatie = 'universitara'
cetatenie = 'romana'

# 7. Printeaza variabilele initializate la ex 5 și 6 intr-o propozitie fiecare folosind stringuri formatate:
#	f’Masina are {numar_roti} roti’

print(f'Masina pe care o detin este marca {marca}')
print(f'Modelul masinii este {model}')
print(f'Anul fabricatiei masinii este {an_fabricatie}')
print(f'Culoare masinii este {culoare}')
print(f'Masina are {numar_usi} usi')
print(f'Puterea motorului este de {cai_putere} cai putere')
print(f'Viteza maxima cu care poate rula masina este de {viteza_maxima} km/ora')
print(f'Masina are o valoare de piata de {pret} euro')
print(f'Tara de fabricatie a masinii este {TARA_FABRICATIE}')
print(f'Garantia la achizitionarea masinii din fabrica a fost de {GARANTIE} ani')
print('----------------------------------')
print(f' Masina pe care o detin este marca {marca}.\n Modelul masinii este {model}.\n Anul fabricatiei masinii este {an_fabricatie}.\n '
      f'Culoare masinii este {culoare}.\n Masina are {numar_usi} usi.\n Puterea motorului este de {cai_putere} cai putere.\n '
      f'Viteza maxima cu care poate rula masina este de {viteza_maxima} km/ora.\n Masina are o valoare de piata de {pret} euro.\n '
      f'Tara de fabricatie a masinii este {TARA_FABRICATIE}.\n Garantia la achizitionarea masinii din fabrica a fost de {GARANTIE} ani.\n')

print(f'Salut! Numele meu este {PRENUME} {NUME}. M-am nascut in anul {ANUL_NASTERII}, deci am {varsta} de ani. '
      f'Am o greutate de {greutatea} kg si o inaltime de {inaltimea} metri. Ca si ocupatie sunt {ocupatie},'
      f'ultima forma de educatie urmata este cea {educatie}. Sunt {stare_civila} si am cetatenia {cetatenie}.')

# 8. Incearca sa actualizezi, sa dai o noua valoare unei constante, poti?

print(f'Salut! Numele meu este {PRENUME} {NUME}')

# 9. Opereaza cu cate trei variabile initializate la ex 5 și 6 in asa fel sa aiba sens:
#	ex: o persoana isi schimba adresa, sau numărul de telefon.

cai_putere = cai_putere + 50
viteza_maxima = viteza_maxima + 50
pret = pret + 500

print(f'Acum masina are {cai_putere} cai putere, poate ajunge la o viteza maxima de {viteza_maxima} si are pretul de {pret} euro')

varsta = varsta + 1
greutatea = greutatea - 2
inaltimea = inaltimea - 0.01

print(f'Anul acesta fac {varsta} de ani. Am o noua greutate de {greutatea} kg si inaltime de {inaltimea} metri')