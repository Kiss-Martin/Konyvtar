from menu import *
from kereses import*

choice = menu()
while choice != 0:
    if choice == 1:
        KonyvekKolcsonzese()
    elif choice == 2:
        MindenKonyv()
    elif choice == 3:
        UjKonyv()
    elif choice == 4:
        ModositasKonyv()
    elif choice == 5:
        KolcsonzottKonyvek()
    elif choice == 6:
        KeresesMenu()
    choice = menu()

