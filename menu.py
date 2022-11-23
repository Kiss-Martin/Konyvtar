import os

def menu():    
    os.system('cls')
    print('  ===========[Könyvtár]=============')
    print('--------------------------------------')
    print('\t1. Könyvek kölcsönzése')
    print('\t2. Könyvek visszahozása')
    print('\t3. Könyvek keresése')
    print('\t4. Kölcsönzők keresése\n')
    print('\t0. Kilépés a programból')

    choice = input('\nVálasztás (0-4): ')
    while len(choice) != 1 or '0' > choice or '4' < choice:
        choice = input('\nVálasztás (0-4): ')
    
    os.system('cls')
    return int(choice)