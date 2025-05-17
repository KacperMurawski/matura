#5.1
plik = open("slowa.txt", 'r')
liczniki = [0 for dlugosci in range(13)]
slowa = [linia.rstrip() for linia in plik]
for slowo in slowa:
    liczniki[len(slowo)] = liczniki[len(slowo)] + 1
for dlugosc in range(1,13):
    print(dlugosc,liczniki[dlugosc])
plik.close()
#5.2
plik1 = open("nowe.txt", 'r')
nowe = [linia.rstrip() for linia in plik1]
for slowo in nowe:
    print(slowo,slowa.count(slowo),slowa.count(slowo[::-1]))






