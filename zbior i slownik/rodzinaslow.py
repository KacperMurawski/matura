wyrazy = ["aa", "abc", "cba", "ba", "x", "xy", "z", "a", "kajak"]
# stworz rodzine wyrazow, ktore maja ta sama liczbe liter
#np. 2: aa, xy, ba
rodziny = dict()
for wyraz in wyrazy:
    dlugosc = len(wyraz)
    if dlugosc in rodziny:
        rodziny[dlugosc].append(wyraz)
    else:
        rodziny[dlugosc] = [wyraz]
print(rodziny)