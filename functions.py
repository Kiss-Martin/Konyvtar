from classes import *

kolcsonzok = []
konyvek = []

def ReadFileKolcsonzok():
    kolcsonzok.clear()
    f = open('kolcsonzok.csv', 'r', encoding="UTF-8")
    f.readline()
    for row in f:
        print(row)
        r = kolcsono(row.strip())
        kolcsonzok.append(r)
    f.close()

def ReadFileKonyvek():
    konyvek.clear()
    f = open('konyvek.csv', 'r', encoding="UTF-8")
    f.readline()
    for row in f:
        r = konyv(row.strip())
        konyvek.append(r)
    f.close()

def writeFileKolcsonzok():
    f = open('kolcsonzok.csv', 'w', encoding='UTF-8')
    for r in kolcsonzok:
        row = f'{r.nev};{r.module};{r.time};{r.percent}'
        f.write(row)
    f.close()

def KeresesMenu():
    choice = ''
    while choice != '0':
        print('1. Keresés cím alapján')
        print('2. Keresés író alapján')
        print('3. Keresés kiadás éve alapján')
        print('4. Keresés azonosító alapján')
        print('0. Kilépés a keresésből')

        choice = input('\nVálasztás (1-4): ')

        if choice == '1':
            CimAlapjan()
        elif choice == '2':
            IroAlapjan()
        elif choice == '3':
            pass
        elif choice == '4':
            pass


def CimAlapjan():
    cim = input('Írja be a könyv címét: ')
    for r in konyvek:
        if cim.lower() in r.nev.lower():
            print(f'{r.szerzo}: {r.nev}')
            if r.kolcsonozve == 'igen':
                print('A könyv nem kölcsönezhető jelenleg')
                input('\n')
            else:
                print('A könyv jelenleg kölcsönözhető\n')
                input('\n')

def IroAlapjan():
    szerzo = input('Írja be a könyv íróját: ')
    for r in konyvek:
        if szerzo.lower() in r.szerzo.lower():
            print(f'{r.szerzo}: {r.nev}')
            if r.kolcsonozve == 'igen':
                print('A könyv nem kölcsönezhető jelenleg')
            else:
                print('A könyv jelenleg kölcsönözhető\n')
    input('\n')