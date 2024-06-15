
#Set de numere întregi:
set_intregi = {1, 8, 3, 20, 5, 0, 10, 6, 28, 25, 14}
print(set_intregi)
set_intregi.add(-1)
print(set_intregi)

#Set de șiruri de caractere:
set_cuvinte = {"unu", "doi", "trei", "patru"}

#Set de numere reale:
set_reale = {1.5, 2.3, 3.7, 4.2, 5.9}

#Set de valori booleene:
set_bool = {True, False}

set_cuvinte = {"unu", "doi", "trei", "patru"}

#Adaugă un element în set.
set_cuvinte.add("cinci")
print(set_cuvinte)
#Elimină un element din set. Dacă elementul nu există, va genera o excepție.
set_cuvinte.remove("cinci")
print(set_cuvinte)
#Elimină un element din set, fara exceptie in caz de eroare.
set_cuvinte.discard("sapte")
print(set_cuvinte)
#Elimină și returnează un element aleatoriu din set.
print(set_cuvinte.pop())
print(set_cuvinte)
