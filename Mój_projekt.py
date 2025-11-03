import random

nagroda = ['10zł', '20zł', '15zł', '25zł', '30zł', '50zł', 'monster ultra white', 'monster ultra ruby red' ]
kara = ['2zł', '3zł', '5zł', '10zł', 'cały maraton sprintem (udokumentowane)']

otrzymane_kary = []#Lista od otrzymanych kar, ktore potem zostaną wyswietlone (sktypt od 40 linijki)

while True: #jest to pętla, która bedzie aktywna do momentu zgadniecia liczby przez użytkownika
    a = int(input('Podaj liczbę od 1 do 9:'))
    b = random.randrange(1, 10)

    decyzja = input('jesteś pewien co do liczby? (tak/nie): ').lower()

    if decyzja == "tak":
        if a == b:
            print(f'Brawo, wygrałes {random. choice(nagroda)}!')
            break #kończy pętle
        elif b == (a + 1) or b == (a - 1):
            print(f'No, blisko było ale jednak żeś nie trafił: {random.choice(kara)})')
            print(f'Liczbą była cyfra {b}')
        else:
            print(f'Przegrałeś, a karą jest {random.choice(kara)}')
            print(f'Liczbą była cyfra {b}')

    elif decyzja == "nie":
        c = int(input('Podaj nową liczbę (następnej szansy nie ma!): '))
        if c == b:
            print(f'Brawo, wygrałes {random.choice(nagroda)}!')
            break  # kończy pętle
        elif b == (c + 1) or b == (c - 1):
            print(f'No, blisko było ale jednak żeś nie trafił: {random.choice(kara)})')
            print(f'Liczbą była cyfra {b}')
        else:
            print(f'Przegrałeś, a karą jest {random.choice(kara)}')
            print(f'Liczbą była cyfra {b}')

    else:
        print('Po Polskiemu nie rozumiesz? odpowiedzi są dwie: "tak" lub "nie".')

if otrzymane_kary:
    print("\n Twoje kary: ")
    for idx, k in enumerate(otrzymane_kary + 1):
        print(f"{idx}. {k}") #idx = index; k = poszczególna kara
        print(f"No cóż, otrzymałeś razem {otrzymane_kary} kar(y)")