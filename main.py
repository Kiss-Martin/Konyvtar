from menu import *

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

