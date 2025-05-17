temperatura = [-7,-5,0,-3,-4,-7,-3,1,2,3,5,9,2,3]
temp = [1] * len(temperatura)
for i in range(1,len(temperatura)):
    if temperatura[i-1] < temperatura[i]:
        temp[i] = temp[i-1] + 1
    else:
        temp[i] = 1

print(temp)
poczatek = temp.index(max(temp)) - max(temp) + 1
koniec = temp.index(max(temp))
for i in range(poczatek, koniec+1):
    print(temperatura[i],end=" ")
with open("BIT18.txt",'r') as dane:
    samochody = dane.readlines()
print(samochody)
predkosc = []
for p in samochody:
    p = p.split()
    predkosc.append(int(p[1]))
print(predkosc)


