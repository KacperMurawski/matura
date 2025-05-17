plik = open("dane4.txt", 'r')
liczby = []
import math

def ile_pierwszych(liczby):
    if liczby < 2:
        return False
    for i in range (2,int(math.sqrt(liczby))+1):
        if liczby % i == 0:
            return False

    return True




