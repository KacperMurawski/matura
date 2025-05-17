tekst = "asdfg7qqwe8rQtya3safafghfTdhdf4vsdfa7sfa5fhfdhSdfCsfg7sadgjykGghkh7df4hsgsadfgsdh5gsfhsresse"

# ile razy wystapil dany znak w tekscie

ile_wystapien = [0 for i in range(128)]
# print(ile_wystapien)
for znak in tekst:
    ile_wystapien[ord(znak)]+=1
# print(ile_wystapien)

# print(ord("A"))

for i in range(128):
    if ile_wystapien[i] != 0:
        print(f"{chr(i)}: {ile_wystapien[i]}")





