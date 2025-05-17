tekst = "asdfg7qqwe8rQtya3safafghfTdhdf4vsdfa7sfa5fhfdhSdfCsfg7sadgjykGghkh7df4hsgsadfgsdh5gsfhsresse"

# ile razy wystapil dany znak w tekscie

znaki = dict()

for znak in tekst:
    if znak in znaki:
        znaki[znak] += 1
    else:
        znaki[znak] = 1

print(znaki)

for klucz,wartosc in znaki.items():
    print(f"{klucz}: {wartosc}")




