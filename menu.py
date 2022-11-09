import os

def menu():    
    os.system('cls')
    print('1. Könyvek kölcsönzése')
    print('2. Minden könyv listázása')
    print('3. Új könyv felvétele')
    print('4. Könyv adatinak módosítása')
    print('5. Jelenleg kölcsönzött könyvek listázása')
    print('6. Adott könyvre keresés\n')
    print('0. Kilépés a programból')

    choice = input('\nVálasztás (0-6): ')
    while len(choice) != 1 or '0' > choice or '6' < choice:
        choice = input('\nVálasztás (0..6): ')
    
    os.system('cls')
    return int(choice)
    
choice = menu()
while choice != 0:
    if choice == 1:
        konyvekKolcsonzese()
    elif choice == 2:
        mindenKonyv()
    elif choice == 3:
        ujKonyv()
    elif choice == 4:
        modositasKonyv()
    elif choice == 5:
        kolcsonzottKonyvek()
    elif choice == 6:
        keresesKonyv()
    choice = menu()

