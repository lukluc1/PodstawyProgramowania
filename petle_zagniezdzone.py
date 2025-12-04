#tabliczbka mnozenia
'''for i in range(1, 21):
    for j in range(1, 21):
        print(i * j, end = '\t') #\n - jednym wezykiem      \t - kolumna
    print()'''

#trojkat prostokatny
'''n = int(input('wysokosc trojkata = '))

for x in range(n):
    for y in range(x + 1):
        print('*', end = '  ')
    print()'''

'''n = int(input('wysokosc trojkata = '))
for x in range(n):
    print('*' * (x + 1))'''

#trojkat rownoramienny dowolny
n = int(input('wysokosc choinki = '))
spacje = n - 1
gwiazdki = 1

for i in range(n):
    print(' ' * spacje, end = '')
    print('*' * gwiazdki)
    spacje = spacje - 1
    gwiazdki = gwiazdki + 2