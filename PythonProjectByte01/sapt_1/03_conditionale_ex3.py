# 3. Creaza un program care sa ceara utilizatorului anul de nastere și sa determine varsta lui. Foloseste print cu mai multe # argumente separate de virgula pentru printarea rezultatului in fraza:
#   “Aveti varsta de 20 de ani”, și apoi foloseste stringuri formatate pentru a printa acelasi rezultat.
#    Care metoda ti se pare mai usoara?

anul_nasterii = input('Introdu anul nasterii: ')
anul_nasterii = int(anul_nasterii)
anul_curent = 2024
varsta = anul_curent - anul_nasterii
print('Aveti varsta de',varsta, 'de ani!')
print(f'Aveti varsta de {varsta} de ani!')