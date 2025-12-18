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
'''popr_haslo = 'informatyka'
haslo = input('podaj haslo')
proba = 1
while haslo != popr_haslo and proba < 5:
    print('bledne haslo, podaj raz jeszcze!')
    haslo = input('podaj haslo')
    proba = proba + 1

if haslo == popr_haslo:
    print('witaj w systemie')
else:
    print('nie ma hasla nie ma dostepu')'''

#zad 6
'''wynik1 = 0
wynik2 = 0
akcja = 0
while not ((wynik1 >= 21 or wynik2 >= 21) and abs(wynik1 - wynik2) >= 2): #abs(x) = |x|
    akcja += 1  # akcja = akcja + 1
    print(f'akcja {akcja}')
    druzyna = int(input('Podaj numer druzyny, ktora wygrala akcje'))
    if druzyna == 1:
        wynik1 += 1
    elif druzyna == 2:
        wynik2 += 1
    print(f'Wynik {wynik1} : {wynik2}')
if wynik1 > wynik2:
    print('wygrala druzyna 1')
else:
    print('wygrala druzyna 2')'''
#zad 6 random
'''from random import randint
from time import sleep
wynik1 = 0
wynik2 = 0
akcja = 0
while not ((wynik1 >= 21 or wynik2 >= 21) and abs(wynik1 - wynik2) >= 2): #abs(x) = |x|
    akcja += 1  # akcja = akcja + 1
    print(f'akcja {akcja}')
    druzyna = randint(1, 2)
    if druzyna == 1:
        wynik1 += 1
    elif druzyna == 2:
        wynik2 += 1
    print(f'Wynik {wynik1} : {wynik2}')
    sleep(0.5)
if wynik1 > wynik2:
    print('wygrala druzyna 1')
else:
    print('wygrala druzyna 2')'''

#zad 7
'''liczba = int(input('Podaj liczbe'))

while liczba > 0:
    cyfra = liczba % 10
    liczba = liczba // 10
    print(cyfra, end = '')'''

#zad 8
'''liczba = int(input('Podaj liczbe'))
d = 2
ile_czyn = 0
ile_r_czyn = 0
while liczba > 1:
    if liczba % d == 0:
        ile_r_czyn += 1
    while liczba % d == 0:
        liczba = liczba // d
        ile_czyn += 1
    d += 1
print(ile_czyn)
print(ile_r_czyn)'''

#zad 5
from random import randint
from time import sleep
x, y = 0, 0
ruchy = ['p'] * 10 + ['d'] * 5 + ['l'] * 5 + ['g'] * 10 + ['q']
while True:
    #ruch = input('Podaj ruch')
    ruch = ruchy[randint(0, len(ruchy) - 1)]
    if ruch == 'q':
        print('koniec')
        break
    elif ruch == 'g':
        if y < 9:
            y += 1
        else:
            print('niemozliwy ruch')
    elif ruch == 'd':
        if y > 0:
            y -= 1
        else:
            print('niemozliwy ruch')
    elif ruch == 'p':
        if x < 9:
            x += 1
        else:
            print('niemozliwy ruch')
    elif ruch == 'l':
        if x > 0:
            x -= 1
        else:
            print('niemozliwy ruch')
    else:
        print('ruch nieznany')
    print(f'({x}, {y})')
    sleep(0.5)