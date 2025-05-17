# Algorytm SortW:
#  dla i = 2, 3, …, n wykonaj
# v ← A[ i ]
# j ← i
# dopóki (j > 1) oraz (v < A[ j – 1]) wykonaj
# A[ j ] ← A[ j – 1]
# j ← j - 1
# A[ j ] ← v


def sortW(A):
    ile_1 = 0
    ile_2 = 0
    n = len(A)
    for i in range(1, n):
        v = A[i]
        j = i
        ile_1 += 1
        while j > 0 and (v < A[j-1]):
            A[j] = A[j-1]
            j = j - 1
            ile_2 += 1
        A[j] = v

    print(f"{ile_1=},{ile_2=}")
    print(A)

A = [7,2,1,3,8,9,4]
sortW(A)


