def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    pierwiastek = int(liczba**(1/2))
    for i in range (2,pierwiastek+1):
        if liczba % i == 0:
            return False

    return True

print(czy_pierwsza(61))
