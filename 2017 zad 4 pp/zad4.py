import math

trojki = []
plik = open("liczby.txt", 'r')
for linia in plik:
    linia = linia.strip()
    trojki.append(linia)
#print(trojki)

def czy_rosnaco(a,b,c):
    if a < b < c:       #if a < b and b < c:
        return True
    return False

def suma_cyfr(liczba:int)->int:
    suma = 0
    while liczba > 0:
        ostatnia_cyfra = liczba % 10
        suma += ostatnia_cyfra
        liczba = liczba//10
    return suma

ile_rosnacych = 0
suma_dzielnikow = 0
suma_cyfr_trojki = []
for trojka in trojki:
    trojka = trojka.split()
    a = int(trojka[0])
    b = int(trojka[1])
    c = int(trojka[2])
    if czy_rosnaco(a,b,c):
        ile_rosnacych += 1

    nwd = math.gcd(a,math.gcd(b,c))
    suma_dzielnikow += nwd
    suma_cyfr_trojki.append(suma_cyfr(a)+suma_cyfr(b)+suma_cyfr(c))


print(ile_rosnacych)
print(suma_dzielnikow)

ile_35 = 0
for liczba in suma_cyfr_trojki:
    if liczba == 35:
        ile_35 += 1
print(ile_35)

#magia pythona
print(suma_cyfr_trojki.count(35))


maks = max(suma_cyfr_trojki)
print(f"{maks=}")
print(suma_cyfr_trojki.count(maks))

