from menu import *
from kereses import*

choice = menu()
while choice != 0:
    if choice == 1:
        Kolcsonzes()
    elif choice == 2:
        konyvKereses()
    elif choice == 3:
        kolcsonzoKereses()
    choice = menu()

