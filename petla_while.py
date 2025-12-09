#petla while - przyklady

'''liczba = 120
licznik = 0

#w petli dajemy warunek TRWANIA petli
while liczba > 0: #tak dlugo jak liczba jest dodatnia petla sie wykonuje
    liczba = liczba // 2
    licznik = licznik + 1

print(licznik)'''

#zad 1
'''x = input('Podaj liczbe lub q aby zakonczyc')
licznik = 0
while x != 'q':
    liczba = int(x)
    if liczba < 2:
        licznik = licznik + 1
    x = input('Podaj liczbe lub q aby zakonczyc')
print(licznik)'''

#zad 2
popr_haslo = 'informatyka'
haslo = input('podaj haslo')
proba = 1
while haslo != popr_haslo and proba < 5:
    print('bledne haslo, podaj raz jeszcze!')
    haslo = input('podaj haslo')
    proba = proba + 1

if haslo == popr_haslo:
    print('witaj w systemie')
else:
    print('nie ma hasla nie ma dostepu')