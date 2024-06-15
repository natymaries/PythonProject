#1. Declara 10 variabile și atribuiestele valori de diferite tipuri de date

nume = 'Naty'
varsta = 30
inaltime = 1.80
greutate = 89.5
forma_geometrica = 'triunghi'
latura_1 = 13
latura_2 = 10
latura_3 = 12
unghi_1 = 90
unghi_2 = 40.5
unghi_3 = 49.5
suma_unghi_corecta = 180
print('---------------------')

# 2. Printeaza numele variabilelor, valorile și tipul lor de date pe un singur rand, un rand pentru fiecare din cele 10 variabile, in total 10 randuri:

print("nume", nume , type(nume))
print("varsta", varsta , type(varsta))
print("inaltime", inaltime , type(inaltime))
print("greutate", greutate , type(greutate))
print("forma_geometrica", forma_geometrica , type(forma_geometrica))
print("latura_1", latura_1 , type(latura_1))
print("latura_2", latura_2 , type(latura_2))
print("latura_3", latura_3 , type(latura_3))
print("unghi_1", unghi_1 , type(unghi_1))
print("unghi_2", unghi_2 , type(unghi_2))
print("unghi_3", unghi_3 , type(unghi_3))
print("suma_unghi_corecta", suma_unghi_corecta , type(suma_unghi_corecta))
print('---------------------')

#3. Creaza 10 instructiuni care sa opereze cu variabilele declarate (și altele noi in caz ca este necesar)

coeficient_greutate = greutate / (inaltime ** 2)
anul_nasterii = 2024 - varsta
pensionar = varsta >= 65
bun_de_munca =  16 <= varsta and varsta < 65
nume_corect = 'Nati' == nume

suma_unghi_calculata = unghi_1 + unghi_2 + unghi_3
verificare_suma_unghiuri = suma_unghi_calculata == suma_unghi_corecta
verificare_triunghi_dreptunghic = unghi_1 == 90 or unghi_2 == 90 or unghi_3 == 90
perimetru_triunghi = latura_1 + latura_2 + latura_3
semiperimetru_triunghi = (latura_1 + latura_2 + latura_3) / 2

# 4. Pentru fiecare instructiune printeaza rezultatul și anaizeaza tipul de date

print(coeficient_greutate, type(coeficient_greutate))
print(anul_nasterii, type(anul_nasterii))
print(pensionar, type(pensionar))
print(bun_de_munca, type(bun_de_munca))
print(nume_corect, type(nume_corect))

print(suma_unghi_calculata, type(suma_unghi_calculata))
print(verificare_suma_unghiuri, type(verificare_suma_unghiuri))
print(verificare_triunghi_dreptunghic, type(verificare_triunghi_dreptunghic))
print(perimetru_triunghi, type(perimetru_triunghi))
print(semiperimetru_triunghi, type(semiperimetru_triunghi))
print('---------------------')
# 5. Copiati exerctiile de pe slideul 26, 38 și rulati scriptul de python.

#numere intregi - int/integer
varsta = 30
numar_masini = 3

#numere cu zecimale - float(double)
intaltime = 1.90
pret = 289.85

#booleani - bool/boolean, adevarat sau fals
inchis = False
deschis = True

#absenta unei valori - null/NoneType
salariu = None

#constante - nume a unor pozitii de memorie #care nu vor fi schimbate pe durata executiei
NUME_FIRMA = "Carpatheq Works SRL"
NUMAR_PANTOFI = 46

#Strings cu ghilimele - caractere sau cuvinte
nume = "Andrei"
intiala_tatalui = "V"

#Strings cu apostrofuri
oras = 'Baia Mare'
clasa = '8A'

zicala = 'Invatatura este o comoara care isi urmeaza stapanul peste tot'


# Calculati perimetrul si aria unui dreptungi
lungime = 5
latime = 3
perimetru = lungime * 2 + latime * 2
aria = lungime * latime

# Calculati perimetrul si aria unui cerc
PI = 3.14159
raza = 2

perimetrul_cercului = 2 * PI * raza
aria_cercului = PI*(raza*raza)
aria_cercului_alt = PI*raza**2
aria_cercului_alt_2 = PI*pow(raza,2)

#cate bomboane primeste fiecare copil
bomboane = 20
copii = 5
bomboane_copil = bomboane/copii

#ce tip de date este bomboane_copil?
print(type(bomboane_copil))


#cate bomboane primeste fiecare copil
bomboane = 20

#cineva a mancat 5 bomboane
bomboane = bomboane - 5
bomboane -= 5