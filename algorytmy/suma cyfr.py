def suma_cyfr(liczba:str)->int:
    suma = 0
    for x in liczba:
        suma = suma+int(x)      #suma += int(x)
    return suma

print(suma_cyfr("12345"))


def suma_cyfr2(liczba:int)->int:
    suma = 0
    while liczba > 0:
        ostatnia_cyfra = liczba % 10
        suma += ostatnia_cyfra
        liczba = liczba//10         #liczba //=10 (alternatywnie)
    return suma

print(suma_cyfr2(12345))

def suma_cyfr3(liczba:str)->int:
    cyfry = []
    for x in liczba:
        cyfry.append(int(x))
    return sum(cyfry)
print(suma_cyfr3("123"))
