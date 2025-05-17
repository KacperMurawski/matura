dane = open("liczby.txt",'r')
plik = dane.readlines()
liczby = [x.strip() for x in plik]
dane.close()
wyjscie = open("wyniki_6.txt",'w')


#6.1
ile = 0
for liczba in liczby:
    if liczba[-1] == "8":
        ile += 1
wyjscie.write("6.1\n")
wyjscie.write(f"{ile}\n")

#6.2
ile2 = 0
for liczba in liczby:
    if liczba[-1] == "4" and liczba.count("0") == 0:
        ile2 += 1
wyjscie.write("6.2\n")
wyjscie.write(f"{ile2}\n")

#6.3
ile2 = 0
for liczba in liczby:
    if liczba[-1] == "2" and liczba[-2] == "0":
        ile2 += 1
wyjscie.write("6.3\n")
wyjscie.write(f"{ile2}\n")


#6.4
suma = 0
for liczba in liczby:
    if liczba[-1] == "8":
        liczba8 = liczba[0:len(liczba)-1]
        suma += int(liczba8,8)
wyjscie.write("6.4\n")
wyjscie.write(f"{suma}\n")

#6.5
min = 10000000000000000000000
max = 0
minodp = ""
maxodp = ""
for liczba in liczby:
    liczba10 = liczba[0:len(liczba)-1]
    liczba10 = int(liczba10,int(liczba[-1]))
    if min > liczba10:
        min = liczba10
        minodp = liczba
    if max < liczba10:
        max = liczba10
        maxodp = liczba

wyjscie.write("6.5\n")
wyjscie.write(f"min={minodp} {min}\n")
wyjscie.write(f"max={maxodp} {max}\n")
