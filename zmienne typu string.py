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