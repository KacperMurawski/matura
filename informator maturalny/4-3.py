with open("dane4.txt", "r") as plik:
    dane = [int(x) for x in plik.readlines()]

maks = 0
for i in range(1,len(dane)):
    ile_par = 0
    for j in range(i):
        if dane[i] > dane[j]:
            ile_par += 1
    if maks < ile_par:
        maks = ile_par
        odp = i
print(odp+1)