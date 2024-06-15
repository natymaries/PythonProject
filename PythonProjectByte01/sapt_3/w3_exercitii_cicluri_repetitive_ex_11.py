# 11. Scrieți un program care primește un an de la utilizator și determină dacă este un an bisect sau nu.

an = int(input('Introduceti anul: '))
if (an % 4 == 0 ):
    print(f'{an} este un an bisect')
else:
    print(f'{an} nu este un an bisect')
