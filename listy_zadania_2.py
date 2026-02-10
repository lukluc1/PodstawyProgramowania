#zadanie 2.
'''lista = [178, 192, 184, 182, 180, 179, 186, 190, 191, 191]

x_max = max(lista)
x_min = min(lista)

lista_norm = [(x - x_min) / (x_max - x_min) for x in lista]
print(lista_norm)'''

#zadanie3
'''lista = [123, 89, 5600, 432, 11, 45, 900, 12450, 1410, 390, 9999]
lista = [x for x in lista if x < 1000 or x > 9999]
lista = [x for x in lista if not (x >= 1000 and x <=9999)]'''


#zad4
tekst = 'LITWOOJCZYZNOMOJATYJESTESZJAKZDROWIEILECIETRZEBACENICTENTYLKOSIEDOWIEKTOCIESTRACILDZISPIEKNOSCTWACALEJOZDOBIEWIDZEIOPISUJEBOTESKNIEPOTOBIEPANNOSWIETACOJASNEJBRONISZCZESTOCHOWYIOSTREJSWIECISZBRAMIETYCOGRODZAMKOWYNOWOGRODZKIOCHRANIASZZJEGOWIERNMLUDEMJAKMNIEDZIECKODOZDROWIAPOWROCILASCUDYMGDYODPLACZACEJMATKIPODTWOJAOPIEKEOFIAROWANYMARTWAPODNIOSELMOJEPOWIEKEIZARAZMOGLEMPIESZODOTWYCZSWIATYNPROGUISTZAWROCONEZYCIEPODZIEKOWACBOGUTAKNASPOWROCISCUDYMNADOJCZYZNYLONOTYMCZASEMPRENOSMOJADUSZEUTESKNIONADOTYCHPAGORKOWLESNYCHDOTYCHLAKZIELONYCHSZEROKONADBLEKITNYMNIEMNEMROZCIAGNIONYCHDOTYCHPOLMALOWANYCHZBOZEMROZMAITEMWYZLACANYCHPSZENICAPOSREBRZANYCHZYTEMGDZIEBURSZTYNOWYSWIERZOPGRYKAJAKSNIEGBIALAGDZIEPANIENSKIMRUMIENCEMDZIECIELINAPALAAWSZYSTKOPRZEPASANEJAKBYWSTEGAMIEDZAZIELONANANIJZZADKACICHEGRUSZESIEDZA'

'''suma = 0
for x in tekst:
    suma += ord(x)

print(suma)

#sposob 2
print(sum(list(map(ord, tekst))))'''
'''kody_ascii_map = map(ord, tekst)
kody_ascii_map = list(kody_ascii_map)
print(sum(kody_ascii_map))'''

#zad6
plansza = [
[3, 8, 1, 9],
[4, 6, 5, 2],
[7, 1, 8, 3],
[2, 9, 4, 6]
]
#6.1
'''#średnie w wierszach
for x in plansza:
    print(sum(x) / len(x))

#średnie w kolumnach
for i in range(len(plansza[0])):
    suma = 0
    for j in range(len(plansza)):
        suma += plansza[j][i]
    print(suma / len(plansza))'''


#Zadanie 6.2.
'''for i in range(len(plansza)):
    for j in range(len(plansza[0])):
        licznik = 0
        srodkowy = plansza[i][j] #szary element
        if srodkowy < plansza[i - 1][j]:
            licznik += 1
        if srodkowy < plansza[i + 1][j + 1]:
            licznik += 1

        for x in range(i - 1, (i + 1) + 1):
            for y in range(j - 1, (j + 1) + 1):
                if i < 0:
                    x = len(plansza) - 1
                elif x > len(plansza) - 1:
                    x = 0
                if y < 0:
                    y = len(plansza[0]) - 1
                elif y > len(plansza[0]) - 1:
                    y = 0
                czerwony = plansza[x][y]
                if srodkowy < czerwony:
                    licznik += 1
        print(i, j, licznik)'''

#6.3
'''for i in range(len(plansza)):
    suma = 0
    for j in range(len(plansza[0])):
        srodkowy = plansza[i][j]
        suma += srodkowy
    print(suma)'''
'''   najwiekszasuma = max(suma)
print(najwiekszasuma)'''

#6.4














#8
'''lista = [1, 5, 1, 2, 2, 1, 6, 7, 3, 2, 2, 1, 1, 4]
zbior = list(set(lista))
print(zbior)
for x in zbior:
    print(x, lista.count(x))
'''


#9
plecak = [
    ("ksiazka", 1.2),
    ("zeszyt", 0.5),
    ("laptop", 2.5),
    ("piornik", 0.3),
    ("botelka z woda", 1.0),
    ("stroj sportowy", 1.8),
]
#a
'''lekkie = []
for  y in plecak:
    nazwa = y[0]
    waga = y[1]
    if waga > 1:
        lekkie.append(nazwa)
print(lekkie)'''
#b
nowe_wagi = []

'''for i in plecak:
    waga = i[1]
    nowa_waga = round(waga * 1.1, 2)
    nowe_wagi.append(nowa_waga)
print(nowe_wagi)
'''
#c
'''licznik = 0
for x in plecak:
    waga = x[1]
    if waga > 1.5:
        licznik += 1
print(licznik)'''

#d
wynik = []
for x in plecak:
    nazwa = x[0]
    waga = x[1]
    if waga <= 1.5 and len(nazwa) > 5:
        wynik.append(nazwa)
print(wynik)



#10