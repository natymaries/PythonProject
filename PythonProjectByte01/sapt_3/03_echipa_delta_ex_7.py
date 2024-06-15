# 7.  Scrieți un program care să îi permită utilizatorului să ghicească un număr întreg ales
# (de exemplu: 6), oferind indicii despre dacă numărul introdus este mai mare sau mai mic decât numărul ales.
# Folositi o conditie bazata pe o variabila booleana numita ghicit.
# todo: modificati programul ca dupa 4 incercari utilizatorul sa nu mai fie intrebat, se inchide programul

numar_ales = 10
ghicit = False
incercari = 0

while incercari < 4:
    numar_ghicit = int(input('Alege un numar: '))
    incercari += 1

    if numar_ghicit == numar_ales:
        print('Felicitari! Ati ales numarul corect!')

    elif numar_ghicit > numar_ales:
        print('Ati ales un numar mai mare. Incercati din nou')
    else:
        ghicit = True
        print('Ati ales un numar mai mic. Incercati din nou')

if incercari == 4:
    print('Game Over!')