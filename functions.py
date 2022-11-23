from classes import *

kolcsonzok = []
konyvek = []

def ReadFileKolcsonzok():
    kolcsonzok.clear()
    f = open('kolcsonzok.csv', 'r', encoding="UTF-8")
    for row in f:
        print(row)
        r = kolcsonzo(row.strip())
        kolcsonzok.append(r)
    f.close()

def ReadFileKonyvek():
    konyvek.clear()
    f = open('konyvek.csv', 'r', encoding="UTF-8")
    for row in f:
        r = konyv(row.strip())
        konyvek.append(r)
    f.close()

def writeFileKolcsonzok():
    f = open('kolcsonzok.csv', 'w', encoding='UTF-8')
    for r in kolcsonzok:
        row = f'{r.nev};{r.beiratkozas};{r.azonosito};{r.visszahozas}\n'
        f.write(row)
    f.close()

def writeFileKonyv():
    f = open('konyvek.csv', 'w', encoding='UTF-8')
    for r in konyvek:
        row = f'{r.nev};{r.szerzo};{r.kiadasEve};{r.kategoria};{r.kolcsonozve};{r.azonosito}\n'
        f.write(row)
    f.close()

def KeresesMenu():
    choice = ''
    while choice != '0':
        print('  ===========[Könyvek keresése]=============')
        print('----------------------------------------------')
        print('\t1. Keresés cím alapján')
        print('\t2. Keresés író alapján')
        print('\t3. Keresés kiadás éve alapján')
        print('\t4. Keresés azonosító alapján')
        print('\t0. Kilépés a keresésből')

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
    cim = input('Írja be a könyv pontos címét: ')
    for r in konyvek:
        if cim.lower() in r.nev.lower():
            print(f'{r.szerzo}: {r.nev}, {r.kiadasEve} Azonosító: {r.azonosito}')
            if r.kolcsonozve == 'igen':
                print('A könyv jelenleg nem kölcsönezhető')
                input('\n')
                return r
            else:
                print('A könyv jelenleg kölcsönözhető\n')
                input('\n')
                return r

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
        print('  ===========[Kölcsönzők keresése]=============')
        print('-------------------------------------------------')
        print('\t1. Keresés név alapján')
        print('\t2. Keresés beiratkozás ideje alapján')
        print('\t3. Beiratkoztatás/Kiiratkoztatás')
        print('\t0. Kilépés a keresésből')

        choice = input('\nVálasztás (1-3): ')

        if choice == '1':
            NevAlapjan()
        elif choice == '2':
            BeiratkozasAlapjan()
        elif choice == '3':
            KiBe()

def NevAlapjan():
    nev = input('Írja be a kölcsönző nevét(teljes név): ')
    for s in kolcsonzok:
        if nev.lower() in s.nev.lower():
            print(f'{s.nev}, beiratkozva: {s.beiratkozas}')
            if s.azonosito == 'nincs' and s.visszahozas == 'nincs':
                print('A kölcsönzőnél jelenleg nincs kölcsönzött könyv')
                input('\n')
                return s
            else:
                print(f'kölcsönzött könyve: {s.azonosito}, visszahozási határidő: {s.visszahozas}')
                input('\n')
                return s

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
    kolcsonzo = NevAlapjan()
    if kolcsonzo.azonosito == "nincs":
        konyv =  CimAlapjan()
        if konyv.kolcsonozve == "nem":
            kolcsonzo.visszahozas = input('Írja be a visszahozás dátumát (éééé.hh.nn): ')
            kolcsonzo.azonosito = konyv.azonosito
            konyv.kolcsonozve = "igen"
            writeFileKolcsonzok()
            writeFileKonyv()
        else:
            print('Kölcsönzés sikertelen!')
            input('')
    else:
        print('Kölcsönzés sikertelen!')
        input('')

def Visszahozas():
    kolcsonzo = NevAlapjan()
    if kolcsonzo.azonosito != "nincs":
        konyv =  CimAlapjan()
        if konyv.kolcsonozve == "igen" and konyv.azonosito == kolcsonzo.azonosito:
            input('Folyamat megkezdése')
            kolcsonzo.visszahozas = "nincs"
            kolcsonzo.azonosito = "nincs"
            konyv.kolcsonozve = "Nem"
            writeFileKolcsonzok()
            writeFileKonyv()
        else:
            print('Visszahozás sikertelen!')
            input('')
    else:
        print('Visszahozás sikertelen!')
        input('')

def KiBe():
    choice = ''
    while choice != '0':
        print('1. Kiiratkoztatás')
        print('2. Beiratkoztatás')
        print('0. Kilépés')

        choice = input('\nVálasztás (1-2): ')

        if choice == '1':
            Ki()
        elif choice == '2':
            Be()

def Ki():
    name = input('Kiiratkoztani kívánt személy neve: ')
    r = None
    for r in kolcsonzok:
        if r.nev.lower() == name.lower():
            kolcsonzok.remove(r)
            writeFileKolcsonzok()
            print(f'{name} sikeresen törölve lett a listából\n')

def Be():
    nev = input('Új tag neve: ')
    datum = input('Beiratkozás dátuma (éééé.hh.nn): ')
    azonosito = "nincs"
    visszahozas = "nincs"

    row = f'{nev};{datum};{azonosito};{visszahozas}\n'
    f = open('Kolcsonzok.csv', 'a', encoding="UTF-8")    
    f.write(row)
    f.close()

    r = kolcsonzo(row)
    kolcsonzok.append(r)
    
def KiBeKonyv():
    choice = ''
    while choice != '0':
        print('1. Könyv törlése')
        print('2. Könyv hozzáadása')
        print('0. Kilépés')

        choice = input('\nVálasztás (1-2): ')

        if choice == '1':
            KiKonyv()
        elif choice == '2':
            BeKonyv()

def KiKonyv():
    name = input('Kitörölni kívánt könyv neve: ')
    r = None
    for r in konyvek:
        if r.nev.lower() == name.lower():
            konyvek.remove(r)
            writeFileKonyv()
            print(f'{name} sikeresen törölve lett a listából\n')

def BeKonyv():
    nev = input('Új könyv neve: ')
    szerzo = input('Új könyv szerzője: ')
    kiadasEve  = input('Kiadás éve: ')
    kategoria = input('Új könyv kategóriája: ')
    kolcsonozve = "nincs"
    azonosito = ''

    row = f'{nev};{szerzo};{kiadasEve};{kategoria};{kolcsonozve};{azonosito}\n'
    f = open('konyvek.csv', 'a', encoding="UTF-8")    
    f.write(row)
    f.close()

    r = konyv(row)
    konyv.append(r)
    