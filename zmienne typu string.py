from traceback import print_tb

napis = 'informatyka'

#Ifragment tekstu:
#1) wycinanie od ... do
print(napis[2:5]) #czyli tak naprawde od 2 do 4

#2) wycinanie od ... do co ileś
print(napis[2:10:2])

#3) wycinanie od początku
print(napis[:3])

#4) wycinanie do konca
print(napis[7:])

#5) czytanie od końca
print(napis[::-2])

#II zawieranie sie literki w słowie
if 'a' in napis:
    print('naleźy')
else:
    print('nie należy')
# III. Laczenie napiso(konkatenacja)
napis2 = napis + 'jestnajlepsza'
print(napis2)

# IV. funkcje zmiennych typu string

    # 1. poszukiwanie danego fragmentu w tekscie

napis3 = 'matematyka'
index_gdzie_jest = napis3.find('tem')
print(index_gdzie_jest)

napis4 = 'alabalalalabala'
index_gdzie_jest2 = napis4.find('bala')
index_gdzie_jest3 = napis4.find('bala', index_gdzie_jest2 + 1)
index_gdzie_jest4 = napis4.find('xyz', index_gdzie_jest2 + 1)
print(index_gdzie_jest2)
print(index_gdzie_jest3)
print(index_gdzie_jest4)

if napis4.find('xyz') != -1:
    print('xyz nie jest w napisie')
else:
    print('xyz nie jest w napisie')

# 2. podzial tekstu na fragmenty
# piec_liczb = input('podaj piec liczb. oddziel je przecinkiem ')
# piec_liczb_po_podziale =  piec_liczb.split(',')
# print(piec_liczb_po_podziale)
# trzecia_liczba = piec_liczb_po_podziale[2]
# print(trzecia_liczba + 33)

# 3. laczenie napisow
lista_napisow = ['windows', 'jest', 'tworzony', 'dla', 'kasy']
cale_zdanie = '$'.join(lista_napisow)
print(cale_zdanie)

lista_napisow2 = ['abc', 'xyz', 'bbc', 'tvn']
cale_zdanie2 = '\n'.join(lista_napisow2)
print(cale_zdanie2)

# 4. liczenie danego znaku w tekscie
napis5 = 'prawdopodobienstwo'
ile_razy_o = napis5.count('o')
print(ile_razy_o)

#5.) "mutowalność" stringów
napis6 = "fizyka"
'''napis6[2] = 'z'
print(napis6)
#wniosek: string są niemutowalne,z czyli nie można podmieniać pojedyńczych liter'''

#sposób na zmutowanie stringa
napis6_lista = list(napis6)
print(napis6_lista)
napis6_lista[2] = 'z'
print(napis6_lista)
napis6_gotowy = ''.join(napis6_lista)
print(napis6_lista)

#6) Długość napisu
napis7 = 'język polski'
print(len(napis7))

#7) powielanie stringa
napis8 = 'informatyka'
print(napis8 * 3)

#8) funkcje testujące cyfry i litery
napis9 = 'qwerty'
if napis9.isalpha() == True:
    print('słowo składa sie z liter')
else:
    print('słowo nie składa sie z liter')

napis10 = '1410w'
if napis10.isdigit() == True:
    print('słowo składa sie z cyfr')
else:
    print('słowo nie składa sie z cyfr')

napis11 = '1410w!'
if napis11.isalnum() == True:
    print('słowo składa sie z cyfr lub liter')
else:
    print('słowo nie składa sie z cyfr lub liter')
