from math import inf
from random import randint
#petle czesc 1
#zad 1
'''total = 0
for i in range(1, 20):
    if i % 5 == 0:
        continue
    total += i
    if total > 100:
        print(f'Suma przekroczyla 100 przy liczbie {i}')
        break
print(f'Końcowa summa to: {total}')

#zad 3


liczba = int(input('podaj liczbe calkowita dodatnia'))
liczek = 0
for x in range (1, liczba + 1):
    if liczba % x == 0 and x % 2 == 0:
        liczek += 1
print(liczek)

# zad 4

for y in range(100, 1001):
    if y % 11 == 0:
        print(y, end=", ")



#zad 5













#zad 6


zad = (20, 1)
for z in zad:
    if z % 3 == 0:
        print('fizz')
    elif z % 5 == 0:
        print('buzz')
    else:
        print('zadne')


#zad 7

qwer = (1, 51)
for u in range(len(qwer)):
    if not u % 2 == 0 or not u % 3 == 0:
        print(u, end= ", ")'''

'''lista = [12, 48, 78, 101, 9, -5, 9, 7, 23]
for x in lista:
    if x % 2 != 0:
        print(x)

g = int(input('Podaj liczbę'))
while g != 0:
    print(g)
    g = int(input('Podaj liczbę'))'''


'''napis = ('informatyka')
for x in range(5):
    print(napis)

ilosc = [1, 2, 3, 4, 5]
for x in range(len(ilosc)):
    print(napis)

lista = [34, 90, 77, 56, 54, 33, 21, 98, 45]
for i in lista:
    if i % 3 == 0:
        print(i)

xd = []
k = 1
while True:
    xd.append(k)
    k += 1'''
#zad 1
'''D = [-2, 0, 4, 6, 7, 11]
Zwf = [3 * x - 2 for x in D]
print(Zwf)'''

#2
lista = ['kot', 'pies', 'żółw', [4, 6, 7, 1], 2.7, [[8, 9], [3, 5]]]
#a)
#policzy wszyskie elementy w liscie  len(lista) = 6
#b
print(lista[5][1][1])
print(sum(lista[3]))


'''przeslanie = [[90, 65, 87, 83, 90, 69], [87, 65, 82, 84, 79], [66, 89,
67], [80, 82, 90, 89, 90, 87, 79, 73, 84, 89, 77]]

slowo = [''.join(map(chr, x))for x in przeslanie]
wynik = ' '.join(slowo)
print(wynik)'''

'''przedmioty = ['informatyka', 'matematyka pp', 'matematyka pr',
'język polski', 'język angielski']
wyniki = [100, 28, 98, 30, 80]
matura = dict(zip(przedmioty, wyniki))
print(matura)
print(matura['język polski'])
matura['matematyka pp'] *= 1.5
print(matura)
matura['fizyka'] = 90
print(matura)'''


'''tekst = 'NAUCZYCIELEMWSZYSTKIEGOJESTPRAKTYKA'

for litera in set(sorted(tekst)):
    ile = tekst.count(litera)
    print(litera, ile)'''


#zad 3
'''odp = 0
odp_prawidlowa = randint(1, 100)
while odp != odp_prawidlowa:
    odp = int(input('Podaj liczbe od 1 do 100'))
print('brawo zgadles')'''
#zad 4
'''n = int(input('podaj liczbe calkowita dodatnia'))
licznik = 0
dzielnik = 2
while n > 1:
    if n % dzielnik == 0:
        if 10 <= dzielnik <=99:
            licznik += 1
        n = n // dzielnik
    else:
        dzielnik += 1
print(licznik)'''

#5
'''b = int(input('podaj liczbe b'))
a = int(input('podaj liczbe a'))
orginal_a = a
orginal_b = b
while a != b:
    if a > b:
        b += orginal_b
    else:
        a += orginal_a
nww = a
print(nww)'''
#1
'''licznik = 0
while licznik < 10:
    print(67)
    licznik += 1'''
'''print(125 // 3)'''
#3
'''proby = 3
haslo = 'informatyka'
while proby > 0:
    pytanie = input(f'podaj haslo, zostalo ci jeszcze {proby} prob')
    if pytanie == haslo:
        print('witamy w systemie')
        break
    else:
        proby -= 1
        if proby > 0:
            print('zle haslo sproboj jeszcze raz')
        else:
            print('nie ma hasla nie ma dostepou')
'''


#4
'''liczba = int(input('podaj liczbe '))
suma = 0
while liczba > 0:
    cyfra = liczba % 10
    if cyfra % 3 == 0:
        suma += cyfra
    liczba //= 10
print(suma)'''

#4
#petla jest nieskonczona poniewaz i to bedzie wikelokrotnosc 2 ktora nigdy nie jest rowna 5