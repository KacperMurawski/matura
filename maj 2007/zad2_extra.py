def pisz(A):
    for i in range(len(A)):
        for j in range(len(A)):
            print(A[i][j], end=" ")
        print()
n = input("podaj wymiary planszy:")
n = int(n)
plansza = []
for i in range(n):
    wiersz = []
    for j in range(n):
        wiersz.append(j)
    plansza.append(wiersz)

k = 3*(n-1)

for j in range(n // 2 + 1):
    for i in range(j, n-j):
        plansza[j][i] = k + (2*j)
        plansza[n-1-j][i] = k + (2*j)
    for i in range(j, n-j):
        plansza[i][j] = k + 2*j
        plansza[i][n-1-j] = k + 2*j

pisz(plansza)