import os

def menu():    
    os.system('cls')
    print('1. Könyvek kölcsönzése')
    print('2. Könyvek visszahozása')
    print('3. Könyvek keresése')
    print('4. Kölcsönzők keresése\n')
    print('0. Kilépés a programból')

    choice = input('\nVálasztás (0-4): ')
    while len(choice) != 1 or '0' > choice or '4' < choice:
        choice = input('\nVálasztás (0-4): ')
    
    os.system('cls')
    return int(choice)