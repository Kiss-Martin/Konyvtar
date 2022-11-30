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
        print('\t3. Keresés azonosító alapján')
        print('\t4. Könyv hozzáadása')
        print('\t0. Kilépés a keresésből')

        choice = input('\nVálasztás (1-4): ')

        if choice == '1':
            CimAlapjan()
        elif choice == '2':
            IroAlapjan()
        elif choice == '3':
            AzonositoAlapjan()
        elif choice == '4':
            BeKonyv()

def CimAlapjan():
    cim = input('Írja be a könyv pontos címét: ')
    i = 1
    while i < len(konyvek) and konyvek[i].nev.lower() != cim.lower():
        i += 1 
    if i < len(konyvek):
        print(f'{konyvek[i].szerzo}: {konyvek[i].nev}, {konyvek[i].kiadasEve} Azonosító: {konyvek[i].azonosito}')
        if konyvek[i].kolcsonozve == 'igen':
            print('\033[1;31;40mA könyv jelenleg nem kölcsönezhető\n\033[0m')
            return konyvek[i]
        else:
            print('\033[1;32;40mA könyv jelenleg kölcsönözhető\n\033[0m')
            return konyvek[i]
    else:
        print('\033[1;31;40mNincs ilyen ilyen című könyv!\n\033[0m')
        return "nem"
    
def IroAlapjan():
    szerzo = input('Írja be a könyv íróját: ')
    for r in konyvek:
        if szerzo.lower() in r.szerzo.lower():
            print(f'{r.szerzo}: {r.nev}, {r.kiadasEve} Azonosító: {r.azonosito}')
            if r.kolcsonozve == 'igen':
                print('\033[1;31;40mA könyv jelenleg nem kölcsönezhető\n\033[0m')
            else:
                print('\033[1;32;40mA könyv jelenleg kölcsönözhető\n\033[0m')

def AzonositoAlapjan(id:int=0):
    if id == 0:
        id = input('Írja be a könyv azonosítóját: ')
    i = 0
    while i < len(konyvek) and konyvek[i].azonosito != id:
        i += 1 
    if i < len(konyvek):
        print(f'{konyvek[i].szerzo}: {konyvek[i].nev}, {konyvek[i].kiadasEve} Azonosító: {konyvek[i].azonosito}')
        if konyvek[i].kolcsonozve == 'igen':
            print('\033[1;31;40mA könyv jelenleg nem kölcsönezhető\n\033[0m')
            return konyvek[i]
        else:
            print('\033[1;32;40mA könyv jelenleg kölcsönözhető\n\033[0m')
            return konyvek[i]
    else:
        print('\033[1;31;40mNincs ilyen azonosítóval rendelkező könyv!\n\033[0m')
    
def KolcsonzoKereses():
    choice = ''
    while choice != '0':
        print('  ===========[Kölcsönzők keresése]=============')
        print('-------------------------------------------------')
        print('\t1. Keresés név alapján')
        print('\t2. Beiratkoztatás/Kiiratkoztatás')
        print('\t0. Kilépés a keresésből')

        choice = input('\nVálasztás (1-3): ')

        if choice == '1':
            NevAlapjan()
        elif choice == '2':
            KiBe()

def NevAlapjan():
    nev = input('Írja be a kölcsönző nevét(teljes név): ')
    i = 0
    while i < len(kolcsonzok) and kolcsonzok[i].nev.lower() != nev.lower():
        i += 1 
    if i < len(kolcsonzok):
        print(f'{kolcsonzok[i].nev}, beiratkozva: {kolcsonzok[i].beiratkozas}')
        if kolcsonzok[i].azonosito == 'nincs' and kolcsonzok[i].visszahozas == 'nincs':
            print('\033[1;33;40mA kölcsönzőnél jelenleg nincs kölcsönzött könyv\n\033[0m')
            return kolcsonzok[i]
        else:
            print(f'kölcsönzött könyve: {kolcsonzok[i].azonosito}, visszahozási határidő: {kolcsonzok[i].visszahozas}\n')
            return kolcsonzok[i]
    else:
        print('\033[1;31;40mNincs ilyen nevű személy!\n\033[0m') 
        return "nem"

def kolcsonzes():
    kolcsonzo = NevAlapjan()
    if kolcsonzo != "nem":
        if kolcsonzo.azonosito == "nincs":
            konyv =  CimAlapjan()
            if konyv != "nem":
                print('Átjutottam')
                if konyv.kolcsonozve == "nem":
                    kolcsonzo.visszahozas = input('Írja be a visszahozás dátumát (éééé.hh.nn): ')
                    kolcsonzo.azonosito = konyv.azonosito
                    konyv.kolcsonozve = "igen"
                    writeFileKolcsonzok()
                    writeFileKonyv()
                    print('Sikeres kölcsönzés')
                else:
                    print('\033[1;31;40mKölcsönzés sikertelen!\n\033[0m')
            else:
                print('\033[1;31;40mKölcsönzés sikertelen!\n\033[0m')
        else:
            print('\033[1;31;40mKölcsönzés sikertelen!\n\033[0m')
    else:
        print('\033[1;31;40mKölcsönzés sikertelen!\n\033[0m')
    input('')

def Visszahozas():
    kolcsonzo = NevAlapjan()
    if kolcsonzo != "nem":
        if kolcsonzo.azonosito != "nincs":
            konyv =  AzonositoAlapjan(kolcsonzo.azonosito)
            if konyv.kolcsonozve == "igen" and konyv.azonosito == kolcsonzo.azonosito:
                kolcsonzo.visszahozas = "nincs"
                kolcsonzo.azonosito = "nincs"
                konyv.kolcsonozve = "Nem"
                writeFileKolcsonzok()
                writeFileKonyv()
                print('Könyv sikeresen visszahozva')
            else:
                print('\033[1;31;40mVisszahozás sikertelen!\n\033[0m')
        else:
            print('\033[1;31;40mVisszahozás sikertelen!\n\033[0m')
    else:
        print('\033[1;31;40mVisszahozás sikertelen!\n\033[0m')

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
            print(f'\033[1;32;40m{name} sikeresen törölve lett a listából\n\033[0m')

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
            print(f'\033[1;32;40m{name} sikeresen törölve lett a listából\n\033[0m')

def BeKonyv():
    nev = input('Új könyv neve: ')
    szerzo = input('Új könyv szerzője: ')
    kiadasEve  = input('Kiadás éve: ')
    kategoria = input('Új könyv kategóriája: ')
    kolcsonozve = "nincs"
    azonosito = len(konyvek) + 101

    row = f'{nev};{szerzo};{kiadasEve};{kategoria};{kolcsonozve};{azonosito}\n'
    f = open('konyvek.csv', 'a', encoding="UTF-8")    
    f.write(row)
    f.close()

    r = konyv(row)
    konyvek.append(r)
    print('\033[1;32;40mHozzáadás sikeres!\033[0m\n')
    