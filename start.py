import math
import threading

tekst = open("listaNazwILiczb2.txt", "r")
nazwa = []
liczba = []
try:
    for line in tekst:
        nazwazpliku, liczbazpliku = line.split(";")
        nazwa.append(nazwazpliku)
        liczbazpliku = liczbazpliku[:-1]
        liczba.append(int(liczbazpliku))
    tekst.close()
except ValueError:
    print("Plik jest nieprawidłowy")
    exit()


def fasfaeasd(strNazwa, intLiczba):
    for dzialanie, zapisywaniepliku in zip(intLiczba, strNazwa):
        znumeru = dzialanie
        liczenie = 0
        while liczenie <= 1499:
            dzialanie = dzialanie + math.sin(dzialanie) * math.cos(dzialanie) * math.tan(dzialanie) * 1.000000000087 * math.pi
            liczenie += 1
        plik = open('folder/' + zapisywaniepliku + '.txt', "w")
        plik.write(str(dzialanie))
        print("Zapisywanie pliku:", zapisywaniepliku, ";Z numeru:", znumeru, ";Wynikiem:", dzialanie)
        plik.close()


t = threading.Thread(target=fasfaeasd, daemon=False, args=(nazwa, liczba))
t.start()
