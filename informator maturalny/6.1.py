



def p_min(napis):
    lista = []
    for n in napis:
        lista.append(int(n))
    return max(lista) + 1

print(p_min("2001030035"))
print(p_min("0010100001"))
print(p_min("7111190009"))
print(p_min("5550001110"))


