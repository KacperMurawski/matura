import string
litery =[char for char in string.ascii_letters]
tekst = "2" "ola ma psa" "ala ma kota"
znaki = dict()

for znak in tekst:
    if znak in znaki and znak in litery:
        znaki[znak] += 1
    else:
        if znak in litery:
            znaki[znak] = 1

for klucz,wartosc in znaki.items():
    print(f"{klucz}: {wartosc}")
