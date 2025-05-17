def najczesciej(n, nukleotyd):
    ile = [0, 0, 0, 0]  # Tablica do zliczania liczby wystąpień dla A, C, G, T

    for i in range(n):
        if nukleotyd[i] == "A":
            ile[0] += 1
        elif nukleotyd[i] == "C":
            ile[1] += 1
        elif nukleotyd[i] == "G":
            ile[2] += 1
        elif nukleotyd[i] == "T":
            ile[3] += 1

    maks = ile[0]
    N = 0
    for i in range(1, 4):
        if maks < ile[i]:
            maks = ile[i]
            N = i
    print(ile)
    ACGT = ["A", "C", "G", "T"]
    return ACGT[N]

# Przykładowe użycie
n = 20
nukleotyd = "CTATGAAAATGTAGATGGTA"
print(najczesciej(n, nukleotyd))
