tekst = "asdfg7qqwe8rQtya3safafghfTdhdf4vsdfa7sfa5fhfdhSdfCsfg7sadgjykGghkh7df4hsgsadfgsdh5gsfhsresse"

# ktore znaki wystapily w tekscie

ile_wystapien = [0 for i in range(128)]
# print(ile_wystapien)
for znak in tekst:
    ile_wystapien[ord(znak)]+=1
# print(ile_wystapien)

# print(ord("A"))

znaki = []               #mozna tez znaki = list()

for i in range(128):
    if ile_wystapien[i] != 0:
        znaki.append(chr(i))

print(znaki)