
pesle = []
plik = open("dane.txt", 'r')
for linia in plik:
    linia = linia.strip()
    pesle.append(linia)
plik.close()

wyjscie = open("wyniki6.txt", 'w')
#6.1
meskie = 0
zenskie = 0
for pesl in pesle:
    przedostatnia = int(pesl[9])
    if przedostatnia % 2 == 0:
        zenskie += 1
    if przedostatnia % 2 == 1:
        meskie += 1
wyjscie.write("6.1\n")
wyjscie.write(f"{zenskie = }\n")
wyjscie.write(f"{meskie = }\n")


#6.2
ile_w_listopadzie = 0
for pesl in pesle:
    #miesiac = pesl[2] + pesl[3]
    miesiac = pesl[2:4]
    if miesiac == "11" or miesiac == "31":
        ile_w_listopadzie += 1
wyjscie.write("6.2\n")
wyjscie.write(f"{ile_w_listopadzie}\n")


#6.3
wyjscie.write("6.3\n")
for p in pesle:
    suma = 1 * int(p[0]) + 3 * int(p[1]) + 7 * int(p[2]) + 9 * int(p[3]) + 1 * int(p[4]) + 3 * int(p[5]) + 7 * int(p[6]) + 9 * int(p[7]) + 1 * int(p[8]) + 3 * int(p[9]) + int(p[10])
    if suma % 10 != 0:
        wyjscie.write(f"{p}\n")




wyjscie.close()


    





