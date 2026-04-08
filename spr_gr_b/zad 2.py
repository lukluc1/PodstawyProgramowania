plik = open('liczby.txt')
dane = plik.readlines()

'''for x in range(len(dane)):
    dane[x] = dane[x].strip()

for x in dane:
     if int(x[::-1]) % 17  == 0:
         print(x[::-1])'''

#2.2
print(len(set(dane)))

'''lista = []
for x in dane:
    ile = dane.count(x)
    if ile == 2:
        lista.append(ile)
print(len(set(lista)))'''

licznik2 = 0
licznik3 = 0
for i in set(dane):
    if dane.count(i) == 2:
        licznik2 +=1
    elif dane.count(i) == 3:
        licznik3 +=1
print(licznik2, licznik3)
