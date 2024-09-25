def palindrom1(txt):
    return txt == txt[::-1]
print(palindrom1("kajak"))
print(palindrom1("kacper"))

def palindrom2(txt):
    n = len(txt)
    for i in range(n//2):
        if txt[i] != txt[n-i-1]:
            return False
    return True

print(palindrom1("kajak"))
print(palindrom1("kacper"))

