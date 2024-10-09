# Sito Eratostenesa
n = int(input())
sito = [True] * (n+1)
sito[0] = False
sito[1] = False
pierwiastek = int(n**(1/2))
for i in range(2,pierwiastek+1):
    if sito[i] == False:
        continue
    for j in range(i*i, n+1, i):
        sito[j] = False

print(sito)
for i in range(2,n+1):
    if sito[i] == True:
        print(i,end=" ")