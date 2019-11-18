import math
import threading


def obliczenia(strnazwa, intliczba):
    for dzialanie, zapisywaniepliku in zip(intliczba, strnazwa):
        znumeru = dzialanie
        liczenie = 0
        while liczenie <= 1499:
            dzialanie = dzialanie + math.sin(dzialanie) * math.cos(dzialanie) * math.tan(dzialanie) * \
                        1.000000000087 * math.pi
            liczenie += 1
        try:
            plik = open('folder/' + zapisywaniepliku + '.txt', "w")
            plik.write(str(dzialanie))
            print("Zapisywanie pliku:", zapisywaniepliku, ";Z numeru:", znumeru, ";Wynikiem:", dzialanie)
            plik.close()
        except FileNotFoundError:
            print("Nie znaleziono docelowego folderu dla plików.")
            exit()


nazwa, liczba = [], []
try:
    tekst = open("listaNazwILiczb2.txt", "r")
    for line in tekst:
        nazwazpliku, liczbazpliku = line.split(";")
        nazwa.append(nazwazpliku)
        liczbazpliku = liczbazpliku[:-1]
        liczba.append(int(liczbazpliku))
    tekst.close()
except ValueError:
    print("Plik jest nieprawidłowy")
    exit()
except FileNotFoundError:
    print("Nie znaleziono pliku źródłowego.")
    exit()

t = threading.Thread(target=obliczenia, daemon=False, args=(nazwa, liczba))
t.start()
