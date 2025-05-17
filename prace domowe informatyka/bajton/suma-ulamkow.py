import math
def suma_ulamkow(a,b,c,d):
    licznik = a*d+b*c
    mianownik = b*d
    nwd = math.gcd(licznik, mianownik)
    licznik = licznik // nwd
    mianownik //= nwd
    return licznik, mianownik


n = int(input())
for i in range(n):
    linia = input().split()
    a = int(linia[0])
    b = int(linia[1])
    c = int(linia[2])
    d = int(linia[3])
    l,m = suma_ulamkow(a,b,c,d)
    print(f"{l}/{m}")
