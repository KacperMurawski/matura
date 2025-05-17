with open("dane6.txt", 'r') as dane:
    napisy = [x.strip() for x in dane.readlines()]

def antypalindrom(napis):
    return napis != napis[::-1]

for napis in napisy:
    if antypalindrom(napis):
        print(napis)

def palindrom(napis):
    for i in range(len(napis) // 2):
        if napis[i] != napis[len(napis) - i - 1]:
            return False
    return True


