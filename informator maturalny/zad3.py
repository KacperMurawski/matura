# from operator import itemgetter
# A = [[-2,4],[-4,3],[-4,1],[-4,7],[-4,-2],[-3,6],[0,3],[1,1],[7,9]]
#
# A.sort()
# print(A)
#
#
#
#
#
# A.sort(key=itemgetter(1))
# print(A)


A = [[-2,4],[-4,3],[-3,6],[0,3],[1,1],[7,9]]
A = sorted(A)
lista = [1]*len(A)
for i in range(1,len(A)):
    if A[i-1][1] < A[i][1]:
        lista[i] = 1
    else:
        lista[i] = lista[i-1] + 1
maks = max(lista)
print(maks)



print(int("11210",3))

