import os

def menu():    
    os.system('cls')
    print('1. Könyvek kölcsönzése')
    print('2. Könyvek keresése')
    print('3. Kölcsönzők keresése\n')
    print('0. Kilépés a programból')

    choice = input('\nVálasztás (0-3): ')
    while len(choice) != 1 or '0' > choice or '3' < choice:
        choice = input('\nVálasztás (0-3): ')
    
    os.system('cls')
    return int(choice)