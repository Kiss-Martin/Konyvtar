from classes import *

kolcsonzok = []
konyvek = []

def ReadFileKolcsonzok():
    kolcsonzok.clear()
    f = open('kolcsonzok.csv', 'r', encoding="UTF-8")
    f.readline()
    for row in f:
        r = kolcsono(row.strip())
        kolcsonzok.append(r)
    f.close()

def ReadFileKonyvek():
    konyvek.clear()
    f = open('kolcsonzok.csv', 'r', encoding="UTF-8")
    f.readline()
    for row in f:
        r = konyv(row.strip())
        kolcsonzok.append(r)
    f.close()