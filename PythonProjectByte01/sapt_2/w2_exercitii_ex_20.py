# 20. Da optiunea utilizatorului sa introduca un nume pentru a anula participarea. In caz ca numele
#        introdus exista in set anuleaza inscrierea lui stergandu-l din set și confirma asta cu un print:
#        “Rezervarea cu numele: {nume} a fost anulata!”

lista_participanti = {'Andrei','Diana', 'Matei', 'Daniel', 'David', 'Ana'}

anulare_participare = input('Alege un nume care sa fie sters de pe lista invitatilor: ')

if anulare_participare in lista_participanti:
    lista_participanti.remove(anulare_participare)
    print(lista_participanti)
    print(f'Rezervarea cu numele: {anulare_participare} a fost anulata!')
