#1. co można wyświetlać printem?
print(5)
print((2 + 2) * 2)

x = 34

print(x)

print('informatyka')
print(round(2.234, 2))
print(2 == 3 and 1 > 0)
print([6, 1, 9, 4, 2])

#2. Formatowanie wyświetlania tekstu

imie = input('Podaj imie')
nazwisko = input('Podaj nazwisko')
wiek = int(input('Podaj swój wiek'))

#sposób 1
'''print('witaj ' + imie + ' ' + nazwisko +'. masz ' + str(wiek) + ' lat. za 5 lat bedziesz miec ' + str(wiek + 5) + ' lat')'''


#sposob 2
'''print(f'Witaj {imie} {nazwisko}. masz {wiek} lat. za 5 lat bedziesz miec {wiek + 5} lat')'''
liczba = 4.1237
print(f'Kwota = {liczba: 0.3f}')

#sposob 3.1.
print('Witaj {} {}. Masz {} lat. Za 5 lat będziesz mieć {} lat.'.format(imie, nazwisko, wiek, wiek + 5))

#sposob 3.2.
print('Witaj {1} {0}. Masz {3} lat. Za 5 lat będziesz mieć {2} lat.'.format(nazwisko, imie, wiek +