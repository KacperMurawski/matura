tekst = input()
tekst2 = ""
for x in tekst:
    if x != " ":
        tekst2 += x
tekst = tekst2
litery = set()
for litera in tekst:
    litery.add(litera.lower())
if len(litery) == 26:
    print(f"TAK")
else:
    print(f"NIE")