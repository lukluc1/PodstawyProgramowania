#zad 1 gr a
'''n = int(input('podaj liczbe'))

iloczyn = 1

for x in range(n):
    iloczyn *= (x + 1)

print(iloczyn)'''

#zad 2 gr a
'''licznik = 0
lista = [4, 12, 8, 1, 5, 6, 3]
for i in range(len(lista)):                                             # for i in lista:
    for j in range(len(lista)):                                             # for j in lista:
        if lista[i] != lista[j] and (lista[i] + lista[j]) % 3 == 0:             # if i != j and (i + j) % 3 == 0:
            #print(lista[i], lista[j])
            licznik += 1
print(licznik)'''


#zadanie 3 gr a
n = int(input('podaj ile bedzie napisow'))
max_napis = ''
for x in range(n):
    napis = input('podaj napis')
    ile_a = napis.count('a')
    max_ile_a = max_napis.count('a')
    if ile_a > max_ile_a:
        max_napis = napis
print(max_napis)
