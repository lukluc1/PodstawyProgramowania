#symbole logiczne

#koniunkcja
print(2 == 3 and 3 > 1)

#alternatywa
login = 'qwerty'
haslo = 'uiop'
print(login == 'admin' or haslo == 'uiop')

#zaprzeczenie
print(not(login == 'admin' or haslo == 'uiop'))

#alternatywa wykluczjaca
fryzjer = True
murarz = False

print(fryzjer == True ^ murarz == True)

#priorytety operatorów
print(2 == 3 and 3 < 1 or 2 < 6)

#operatory standardiwe
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)

#potęgowanie
print(2 ** 5)

#pierwiastkowanie
print(36 ** 0.5)
print(125 ** (1 / 3))

#dzielenie calkowite (div) - dzielimy i zaokrąlgamy zawsze w dol do liczby calkowitej
print(12 // 5)

#reszta z dzielenia liczby a przez liczbe b
print(12 % 5)