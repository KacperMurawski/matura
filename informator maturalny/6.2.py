with open("dane6.txt", 'r') as dane:
    napisy = [x.strip() for x in dane.readlines()]

def p_min(napis):
    lista = []
    for n in napis:
        lista.append(int(n))
    return max(lista) + 1

def suma_cyfr(napis):
    suma = 0
    for znak in napis:
        suma = suma + int(znak)
    return suma

slownik_p_minimalnych_list = {}


for napis in napisy:
    if p_min(napis) in slownik_p_minimalnych_list:
        slownik_p_minimalnych_list[p_min(napis)].append(napis)
    else:
        slownik_p_minimalnych_list[p_min(napis)] = [napis]


for pmin, lista in slownik_p_minimalnych_list.items():
    sumy = []
    for napis in lista:
        sumy.append(suma_cyfr(napis))
    maks = max(sumy)
    print(f"{pmin}: {maks}")

