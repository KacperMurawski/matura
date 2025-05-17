with open("slowa.txt", 'r') as plik:
    slowa = plik.readlines()
# print(slowa)
slowa = [slowo.strip() for slowo in slowa]
print(slowa)

rodziny = dict()
for slowo in slowa:
    if len(slowo) in rodziny:
        rodziny[len(slowo)].append(slowo)
    else:
        rodziny[len(slowo)] = [slowo]

print(rodziny)

for klucz,wartosc in rodziny.items():
    print(f"{klucz} {len(wartosc)}")

rodziny2 = dict()
for slowo in slowa:
    if len(slowo) in rodziny2:
        rodziny2[len(slowo)] += 1
    else:
        rodziny2[len(slowo)] = 1
print(rodziny2)