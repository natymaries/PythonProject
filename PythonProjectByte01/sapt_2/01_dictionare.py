#Dictionar cu informații despre o persoană:
persoana = {"nume": "John", "varsta": 30, "oras": "New York"}

#Dictionar cu punctaje ale studenților:
punctaje = {"Ana": 8.5, "Maria": 9, "Ion": 7.8}

#Dictionar cu culori în format RGB:
culori = {"rosu": (255, 0, 0), "verde": (0, 255, 0), "albastru": (0, 0, 255)}

#Dictionar cu preturi din meniul unui restaurant:
meniu = {"Pizza": 15, "Burger": 8, "Salata": 6}


#Returnează valoarea asociată cu o anumită cheie.
pret_pizza = meniu.get("Pizza")
print(pret_pizza)
#printati dimensiunea dicionarului meniu
print(len(meniu))

#Returnează o listă cu toate cheile din dicționar.
chei = meniu.keys()
print(type(chei))
print(chei)
#Returnează o listă cu toate valorile din dicționar.
valori= meniu.values()
print(valori)
#Returnează o listă cu tupluri de cheie-valoare din dicționar.
elemente = meniu.items()
print(elemente)

# declara un dictionar cu 4 cuvinte si definitiile lor
# cere utilizatorului sa introduca un cuvint si returneaza definitia cuvantului

dict = {
     "apa" : "Lichid incolor, fără gust și fără miros, compus hidrogenat al oxigenului, "
             "care formează unul dintre învelișurile Pământului.",
     "pamant" : "Scoarța globului terestru, partea de uscat a globului terestru; "
                "suprafața lui (împreună cu atmosfera) pe care trăiesc oamenii și alte vietăți.",
     "zebra" : "Nume generic dat speciilor de cai sălbatici africani cu blana vărgată cu benzi alternative, "
               "deschise și închise; animal care face parte din aceste specii"
 }

cuvint_introdus = input('Introduceti un cuvant: ')
if cuvint_introdus in dict.keys():
    #pornind de la dictionarul creat in variabila dict accesam cheia introdusa de utilizator
    print(dict[cuvint_introdus])
else:
    print('Cuvantul introdus nu este in dictionar!')
