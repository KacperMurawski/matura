x = "[][[][[][[][]]]]"
def nawiasy(x:str):
    suma = 0
    for c in x:
        if c == "[":
            suma += 1
        elif c == "]":
            suma -= 1
        if suma < 0:
            return False
    if suma != 0:
        return False
    return True

print(nawiasy(x))

def glebokosc(x:str):
    suma = 0
    najwieksza_glebokosc = 0
    for g in x:
        if g == "[":
            suma += 1
            if najwieksza_glebokosc < suma:
                najwieksza_glebokosc = suma
        elif g == "]":
            suma -= 1
    return najwieksza_glebokosc

print(glebokosc(x))






