from menu import *
from functions import *
from classes import *

ReadFileKolcsonzok()
ReadFileKonyvek()
choice = menu()
while choice != 0:
    if choice == 1:
        kolcsonzes()
    elif choice == 2:
        KeresesMenu()
    elif choice == 3:
        ()
    choice = menu()

