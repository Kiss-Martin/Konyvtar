from classes import * 
from functions import *


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
                





ReadFileKonyvek()
choice = KeresesMenu()
while choice != 0:
    if choice == 1:
        CimAlapjan()
    elif choice == 2:
        IroAlapjan()
    elif choice == 3:
        ()
    elif choice == 4:
        ()
    elif choice == 0:
        kilepes()
    choice = KeresesMenu()