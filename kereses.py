from classes import * 
from functions import *

def KeresesMenu():
    print('1. Keresés cím alapján')
    print('2. Keresés író alapján')
    print('3. Keresés kiadás éve alapján')
    print('4. Keresés azonosító alapján')

    choice = input('\nVálasztás (1-4): ')
    return int(choice)

def CimAlapjan():
    cim = input('Írja be a könyv címét: ')
    i = 0
    for r in konyvek:
        if cim.lower() in r.nev.lower():
            i += 1
            if r.kolcsonozve == 'igen':
                print('A könyv nem kölcsönezhető jelenleg')
                input('\n')
            else:
                print('A könyv jelenleg kölcsönözhető\n')
                input('\n')
    if i == 0:
        print('Nem található ilyen könyv a listában.')


ReadFileKonyvek()
choice = KeresesMenu()
while choice != 0:
    if choice == 1:
        CimAlapjan()
    elif choice == 2:
        ()
    elif choice == 3:
        ()
    elif choice == 4:
        ()
    choice = KeresesMenu()