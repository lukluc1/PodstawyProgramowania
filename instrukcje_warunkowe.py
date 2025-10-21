'''"#instrukcja warunkowa if

#Przykład 1
liczba = int(input('podaj liczbe od 1 do 3'))

if liczba == 1:
    print('jeden')
if liczba == 2:
    print('dwa')
if liczba == 3:
    print('trzy')

# Przykład 2
liczba = int(input('podaj liczbe od 1 do 3'))

if liczba == 1:
    print('jeden')
elif liczba == 2:
    print('dwa')
elif liczba == 3:
    print('trzy')'''

#przyklad 3
liczba = int(input('podaj liczbe calkowita dodawnia'))

if liczba % 2 == 0:
    print('parzysta')
if liczba % 3 == 0:
    print('podzielma przez 3')
if liczba > 0:
    print('Dodatnia')
else:
    print('czytac nie umiesz?')