# Logica metodelor/functiilor de clasa se poate rezuma la a printa descrierea comportamentului și parametrii.
#1. Identifica 5 obiecte din lumea reala și modeleaza o clasa pentru fiecare. Acestea trebuie sa contina cel putin 5
#   atribute fiecare și 4 metode (fara setters, getters și deleters)
#2. Implementeaza cele 5 obiecte in python fiecare in fisierul sau.
#3. Pentru fiecare obiect creaza o metoda constructor explicit cu atributele pe care le consideri necesare.
#4. Creaza un nou fisier, importeaza clasele create la exercitiile aterioare, creaza cel putin cate 2 obiecte din fiecare și
#    apeleaza metodele de clasa.

# angajat, angajator, banca, elev, profesor, sportiv

from elev import Elev

elev = Elev('Andrei', 18, 1.80, 11, 7.15 )
elev.schimba_varsta(20)
elev.absolva(4)