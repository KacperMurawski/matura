def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    pierwiastek = int(liczba**(1/2))
    for i in range (2,pierwiastek+1):
        if liczba % i == 0:
            return False

    return True

print(czy_pierwsza(1))
print(czy_pierwsza(2))
print(czy_pierwsza(21))
print(czy_pierwsza(13))
print(czy_pierwsza(25))


import math

def czy_pierwsza2(liczba):
    if liczba < 2:
        return False
    for i in range (2,int(math.sqrt(liczba))+1):
        if liczba % i == 0:
            return False

    return True

print(czy_pierwsza2(17))