tekst = "asdfg7qqwe8rQtya3safafghfTdhdf4vsdfa7sfa5fhfdhSdfCsfg7sadgjykGghkh7df4hsgsadfgsdh5gsfhsresse"

znaki = set()       #zbior - nieposortowany
# set jest struktura danych, ktora przechowuje niepowtarzajace sie elementy w sposob nieposortowany

for znak in tekst:
    znaki.add(znak)

print(znaki)

znaki = list(znaki) #zamiana set na list
znaki = sorted(znaki) #posortowana lista
print(znaki)
znaki = set(znaki) # zamiana list na set
print(znaki)


