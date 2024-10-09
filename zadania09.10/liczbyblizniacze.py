"""
Zadanie: Wypisz wszystkie pary liczb bliźniaczych w przedziale od A do B :
Scenariusz:
1. Za pomocą sita eratostenesa stwórz listę liczb pierwszych.
2. Znajdź pary dwóch kolejnych liczb pierwszych, których różnica wynosi 2.
"""

a,b = input().split()
a = int(a)
b = int(b)
n = b
sito = [True] * (n+1)
sito[0] = False
sito[1] = False
pierwiastek = int(n**(1/2))
for i in range(2,pierwiastek+1):
    if sito[i] == False:
        continue
    for j in range(i**2, n+1, i):
        sito[j] = False
pierwsze = []
for i in range(2,n+1):
    if sito[i] == True:
        pierwsze.append(i)
print(pierwsze)


for i in range(1,len(pierwsze)):
    if pierwsze[i] - pierwsze[i-1] == 2 and pierwsze[i-1] >= a:
        print(f"{pierwsze[i-1]} {pierwsze[i]}")

