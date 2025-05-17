slownik = {1:3,"A":7,"owoc":4}
print(slownik[1])
print(slownik["A"])
print(slownik["owoc"])

angtopol = {"bread":"chleb","school":"szkola","one":"jeden","car":"auto"}
print(angtopol["bread"])
angtopol["sun"] = "slonce"
print(angtopol)

print(angtopol.keys())
print(angtopol.values())

for klucz,wartosc in angtopol.items():
    print(f"{klucz}: {wartosc}")
