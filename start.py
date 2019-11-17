import math

tekst = open("listaNazwILiczb2.txt", "r")
nazwa = []
liczba = []
for line in tekst:
    nazwazpliku, liczbazpliku = line.split(";")
    nazwa.append(nazwazpliku)
    liczbazpliku = liczbazpliku[:-1]
    liczba.append(int(liczbazpliku))
tekst.close()

def fasfaeasd(strNazwa, intLiczba):
    for dzialanie in intLiczba:
        liczenie = 0
        while liczenie <= 1499:
            dzialanie = dzialanie + math.sin(dzialanie) * math.cos(dzialanie) * math.tan(dzialanie) * 1.000000000087 * math.pi
            liczenie += 1
        for zapisywaniepliku in strNazwa:
            plik = open('folder/'+zapisywaniepliku+'.txt', "w")
            plik.write(str(dzialanie))
            plik.close()


fasfaeasd(nazwa, liczba)
