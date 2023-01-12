# Imports
from les_meves_funcions.funcions_menu import *
from les_meves_funcions.funcions_joc import *
from pyfiglet import figlet_format


# menus

# Headers
hr00 = "*" * 100 + "\n" + figlet_format("Seven and half", font="starwars") + "*" * 100 + "\n\n"
# Options
mn00 = "1)Add/Remove/Show Players\n2)Settings\n3)Play Game\n4)Ranking\n5)Reports\n6)Exit"
inputOptText = "\nChoose an option:\n"

# Variables
leave = False

# Loops
while not leave:
    print()
    opt = getOpt(hr00, mn00, "\nChoose an option:\n", [1, 2, 3, 4, 5, 6], [], {})

    if opt == 1:
        print("Add/Remove/Show Players")

    elif opt == 2:
        print("Settings")

    elif opt == 3:
        check_settings()
        print("Play game")

    elif opt == 4:
        print("Ranking")

    elif opt == 5:
        print("Reports")

    elif opt == 6:
        leave = True
