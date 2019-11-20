import math
import threading


def obliczenia(strnazwa, dzialanie):
    liczenie = 0
    while liczenie < 1500:
        dzialanie = dzialanie + math.sin(dzialanie) * math.cos(dzialanie) * math.tan(dzialanie) * \
                   1.000000000087 * math.pi
        liczenie += 1
    plik = open('folder/' + strnazwa + '.txt', "w")
    plik.write(str(dzialanie))
    plik.close()


tekst = open("listaNazwILiczb2.txt", "r")
for line in tekst:
    nazwazpliku, liczbazpliku = line.split(";")
    liczbazpliku = liczbazpliku.strip()
    watek = threading.Thread(target=obliczenia, daemon=False, args=(nazwazpliku, int(liczbazpliku)))
    watek.start()
tekst.close()
