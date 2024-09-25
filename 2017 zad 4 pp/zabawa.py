"""
a,b = input().split()
print(a,b)
a = int(a)
b = int(b)
c,d,e = input().split(",")
print(c,d,e)
"""
tekst = input().split()
print(tekst)
for i in range(len(tekst)):
    tekst[i] = int(tekst[i])
print(tekst)



# inaczej (nie polecam)
tekst = input().split()
for x in tekst:
    x = int(x)  #zamienia na liczbe, ale tylko w tym momencie, nie zmienil w liscie (tekst)
print(tekst)
## inaczej 2
tekst = input().split()
tekst = [int(x) for x in tekst]
print(tekst)
### inaczej 3 (fajne, ale trzeba pamietac)
tekst = input().split()
tekst = list(map(int, tekst))
print(tekst)




