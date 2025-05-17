
def czy_palindrom_dz(n):
    return str(n) == str(n)[::-1]
def czy_palindrom_bin(n):
    binarna = bin(n)[2:]
    return czy_palindrom_dz(binarna)

palindromy = []
for liczba in range(10000,100000):
    if czy_palindrom_dz(liczba) and czy_palindrom_bin(liczba):
        palindromy.append(liczba)

suma_palindrom = 0
for liczba in range(1,1000000):
    if czy_palindrom_dz(liczba) and czy_palindrom_bin(liczba):
        suma_palindrom += liczba
print(palindromy)
print(suma_palindrom)