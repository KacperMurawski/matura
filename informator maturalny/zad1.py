A = [2, -3, 1, -7, 4, -2, -1, 5, -3, 2, -1]

def max_suma(A):
    maks = A[0]
    for i in range(len(A)):
        suma = 0
        for j in range(i,len(A)):
            suma += A[j]
            if maks < suma:
                maks = suma
                koniec = j
                poczatek = i
    return maks,A[poczatek:koniec+1]

print(max_suma(A))

