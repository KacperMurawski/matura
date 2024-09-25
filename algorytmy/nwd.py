# algorytm euklidesa = nwd
import math
a = 24
b = 18
print(math.gcd(a,b))


def nwd(a,b):   #algorytm euklidesa z odejmowaniem
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print(nwd(a,b))

def nwd2(a,b): #algorytm euklidesa z modulo
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

print(nwd2(a,b))


def nwd3(a,b): #nwd2 z magią pythona
    while b != 0:
        a,b = b, a % b
    return a
print(nwd3(a,b))




def nwd4(a,b): #algorytm euklidesa z rekurencja
    if b == 0:
        return a
    return nwd4(b,a % b)
print(nwd4(a,b))
