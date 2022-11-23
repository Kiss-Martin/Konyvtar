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
        print('\t5. Könyv hozzáadása')
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
        elif choice == '5':
            BeKonyv()


def CimAlapjan():
    cim = input('Írja be a könyv pontos címét: ')
    for r in konyvek:
        if cim.lower() in r.nev.lower():
            print(f'{r.szerzo}: {r.nev}, {r.kiadasEve} Azonosító: {r.azonosito}')
            if r.kolcsonozve == 'igen':
                print('\033[1;31;40mA könyv jelenleg nem kölcsönezhető\033[0m')
                input('\n')
                return r
            else:
                print('\033[1;32;40mA könyv jelenleg kölcsönözhető\033[0m\n')
                input('\n')
                return r

def IroAlapjan():
    szerzo = input('Írja be a könyv íróját: ')
    for r in konyvek:
        if szerzo.lower() in r.szerzo.lower():
            print(f'{r.szerzo}: {r.nev}, {r.kiadasEve} Azonosító: {r.azonosito}')
            if r.kolcsonozve == 'igen':
                print('\033[1;31;40mA könyv jelenleg nem kölcsönezhető\033[0m')
            else:
                print('\033[1;32;40mA könyv jelenleg kölcsönözhető\033[0m\n')
    input('\n')

def EvAlapjan():
    ev = input('Írja be a könyv kiadásának évét: ')
    for r in konyvek:
        if ev.lower() in r.kiadasEve.lower():
            print(f'{r.szerzo}: {r.nev}, {r.kiadasEve} Azonosító: {r.azonosito}')
            if r.kolcsonozve == 'igen':
                print('\033[1;31;40mA könyv jelenleg nem kölcsönezhető\033[0m')
            else:
                print('\033[1;32;40mA könyv jelenleg kölcsönözhető\033[0m\n')
    input('\n')

def AzonositoAlapjan():
    id = input('Írja be a könyv azonosítóját: ')
    for r in konyvek:
        if id.lower() in r.azonosito.lower():
            print(f'{r.szerzo}: {r.nev}, {r.kiadasEve} Azonosító: {r.azonosito}')
            if r.kolcsonozve == 'igen':
                print('\033[1;31;40mA könyv jelenleg nem kölcsönezhető\033[0m')
            else:
                print('\033[1;32;40mA könyv jelenleg kölcsönözhető\n\033[0m')
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
    i = 0
    while i < len(kolcsonzok) and kolcsonzok[i].nev.lower() != nev.lower():
        i += 1 
    if i < len(kolcsonzok):
        print(f'{kolcsonzok[i].nev}, beiratkozva: {kolcsonzok[i].beiratkozas}')
        if kolcsonzok[i].azonosito == 'nincs' and kolcsonzok[i].visszahozas == 'nincs':
            print('A kölcsönzőnél jelenleg nincs kölcsönzött könyv')
            input('\n')
            return kolcsonzok[i]
        else:
            print(f'kölcsönzött könyve: {kolcsonzok[i].azonosito}, visszahozási határidő: {kolcsonzok[i].visszahozas}')
            input('\n')
            return kolcsonzok[i]
    else:
        print('\033[1;31;40mNincs ilyen nevű személy!\033[0m\n')

    # for s in kolcsonzok:
    #     if nev.lower() in s.nev.lower():
    #         print(f'{s.nev}, beiratkozva: {s.beiratkozas}')
    #         if s.azonosito == 'nincs' and s.visszahozas == 'nincs':
    #             print('A kölcsönzőnél jelenleg nincs kölcsönzött könyv')
    #             input('\n')
    #             return s
    #         else:
    #             print(f'kölcsönzött könyve: {s.azonosito}, visszahozási határidő: {s.visszahozas}')
    #             input('\n')
    #             return s

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
            print('\033[1;31;40mKölcsönzés sikertelen!\033[0m')
            input('')
    else:
        print('\033[1;31;40mKölcsönzés sikertelen!\033[0m')
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
            print('\033[1;31;40mVisszahozás sikertelen!\033[0m')
            input('')
    else:
        print('\033[1;31;40mVisszahozás sikertelen!\033[0m')
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
            print(f'\033[1;32;40m{name} sikeresen törölve lett a listából\033[0m\n')

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
            print(f'\033[1;32;40m{name} sikeresen törölve lett a listából\033[0m\n')

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
    