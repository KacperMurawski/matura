from math import sqrt
#4.1
plik = open("liczby.txt", 'r')
liczby = list(map(str.strip,plik.readlines()))
licznik = 0
pierwsza1 = -1
for liczba in liczby:
    pierwsza = liczba[0]
    ostatnia = liczba[-1]
    if pierwsza == ostatnia:
        licznik += 1
        if pierwsza1 == -1:
            pierwsza1 = int(liczba)
print(licznik, pierwsza1)

#4.2
def czy_pierwsza(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, int(sqrt(x)) +1):
        if x % i == 0:
            return False
        return True
pierwsze = [0 for x in range(10001)]
for i in range(10001):
    if czy_pierwsza(i):
        pierwsze.append(i)
print(pierwsze)



