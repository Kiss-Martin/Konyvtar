from classes import *

kolcsonzok = []
konyvek = []

def ReadFileKolcsonzok():
    kolcsonzok.clear()
    f = open('kolcsonzok.csv', 'r', encoding="UTF-8")
    f.readline()
    for row in f:
        print(row)
        r = kolcsonzo(row.strip())
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
            EvAlapjan()
        elif choice == '4':
            AzonositoAlapjan()


def CimAlapjan():
    cim = input('Írja be a könyv címét: ')
    for r in konyvek:
        if cim.lower() in r.nev.lower():
            print(f'{r.szerzo}: {r.nev}, {r.kiadasEve} Azonosító: {r.azonosito}')
            if r.kolcsonozve == 'igen':
                print('A könyv jelenleg nem kölcsönezhető')
                input('\n')
            else:
                print('A könyv jelenleg kölcsönözhető\n')
                input('\n')

def IroAlapjan():
    szerzo = input('Írja be a könyv íróját: ')
    for r in konyvek:
        if szerzo.lower() in r.szerzo.lower():
            print(f'{r.szerzo}: {r.nev}, {r.kiadasEve} Azonosító: {r.azonosito}')
            if r.kolcsonozve == 'igen':
                print('A könyv jelenleg nem kölcsönezhető')
            else:
                print('A könyv jelenleg kölcsönözhető\n')
    input('\n')

def EvAlapjan():
    ev = input('Írja be a könyv kiadásának évét: ')
    for r in konyvek:
        if ev.lower() in r.kiadasEve.lower():
            print(f'{r.szerzo}: {r.nev}, {r.kiadasEve} Azonosító: {r.azonosito}')
            if r.kolcsonozve == 'igen':
                print('A könyv jelenleg nem kölcsönezhető')
            else:
                print('A könyv jelenleg kölcsönözhető\n')
    input('\n')

def AzonositoAlapjan():
    id = input('Írja be a könyv azonosítóját: ')
    for r in konyvek:
        if id.lower() in r.azonosito.lower():
            print(f'{r.szerzo}: {r.nev}, {r.kiadasEve} Azonosító: {r.azonosito}')
            if r.kolcsonozve == 'igen':
                print('A könyv jelenleg nem kölcsönezhető')
            else:
                print('A könyv jelenleg kölcsönözhető\n')
    input('\n')

def KolcsonzoKereses():
    choice = ''
    while choice != '0':
        print('1. Keresés név alapján')
        print('2. Keresés beiratkozás ideje alapján')
        print('0. Kilépés a keresésből')

        choice = input('\nVálasztás (1-2): ')

        if choice == '1':
            NevAlapjan()
        elif choice == '2':
            BeiratkozasAlapjan()

def NevAlapjan():
    nev = input('Írja be a kölcsönző nevét: ')
    for s in kolcsonzok:
        if nev.lower() in s.nev.lower():
            print(f'{s.nev}, beiratkozva: {s.beiratkozas}')
            if s.azonosito == 'nincs' and s.visszahozas == 'nincs':
                print('A kölcsönzőnél jelenleg nincs kölcsönzött könyv')
                input('\n')
            else:
                print(f'kölcsönzött könyve: {s.azonosito}, visszahozási határidő: {s.visszahozas}')
                input('\n')

def BeiratkozasAlapjan():
    signin = input('Írja be a kölcsönző beiratkozásának dátumát (éééé.hh.nn): ')
    for s in kolcsonzok:
        if signin.lower() in s.beiratkozas.lower():
            print(f'{s.nev}, beiratkozva: {s.beiratkozas}')
            if s.azonosito == 'nincs' and s.visszahozas == 'nincs':
                print('A kölcsönzőnél jelenleg nincs kölcsönzött könyv')
                input('\n')
            else:
                print(f'kölcsönzött könyve: {s.cim}: {s.azonosito}, visszahozási határidő: {s.visszahozas}')
                input('\n')


def kolcsonzes():
    nev = input('Irja be a kölcsönző nevét: ') 
    pass