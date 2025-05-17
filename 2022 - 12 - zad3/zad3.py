with open("liczby_przyklad.txt", 'r') as plik:
    liczby = plik.readlines()
liczby = list(map(int,liczby))
#print(liczby)

n = 1000000
sito = [True] * (n+1)
sito[0] = False
sito[1] = False
pierwiastek = int(n**(1/2))
for i in range(2,pierwiastek+1):
    if sito[i] == False:
        continue
    for j in range(i*i, n+1, i):
        sito[j] = False

pierwsze = []
for i in range(2,n+1):
    if sito[i] == True:
        pierwsze.append(i)
#print(pierwsze)
wyjscie = open("wyniki3.txt", 'w')

# 3.2
"""
ile_pierwszych = 0
for liczba in liczby:
    for pierwsza in pierwsze:
        if liczba -1 == pierwsza:
            ile_pierwszych += 1
            break
wyjscie.write(f"3.2\n")
wyjscie.write(f"{ile_pierwszych}")
"""

# 3.3
najwieksza_liczba_rozkladow = 0
najmniejsza_liczba_rozkladow = 1000000

for liczba in liczby:
    print(f"{liczba=}")
    biezaca_liczba_rozkladow = 0
    for i in range(len(pierwsze)):
        for j in range(i,len(pierwsze)):
            if liczba > pierwsze[i] + pierwsze[j]:
                break
            if liczba == pierwsze[i] + pierwsze[j]:
                biezaca_liczba_rozkladow += 1
    if biezaca_liczba_rozkladow > najwieksza_liczba_rozkladow:
        najwieksza_liczba_rozkladow = biezaca_liczba_rozkladow
        liczba_najwieksza_liczba_rozkladow = liczba
    if biezaca_liczba_rozkladow < najmniejsza_liczba_rozkladow:
        najmniejsza_liczba_rozkladow = biezaca_liczba_rozkladow
        liczba_najmniejsza_liczba_rozkladow = liczba

    print(f"{liczba_najwieksza_liczba_rozkladow=} {najwieksza_liczba_rozkladow=} ")
    print(f"{liczba_najmniejsza_liczba_rozkladow=} {najmniejsza_liczba_rozkladow=}")






wyjscie.close()





