# Imports
from les_meves_funcions.funcions_menu import *
from pyfiglet import figlet_format

# Variables
leave = False

# Loops
while not leave:
    print()
    textOpts = "*" * 100 + "\n" + figlet_format("Seven and half", font="starwars") + "*" * 100 + \
               "\n\n1)Add/Remove/Show Players\n2)Settings\n3)Play Game\n4)Ranking\n5)Reports\n6)Exit"
    inputOptText = "\nChoose an option:\n"
    rangeList = [1, 2, 3, 4, 5, 6]
    exceptions = []
    dictionary = {}  # Aqui va el nombre del dicc sin los {} (si se da el caso de usar un dicc)
    opt = getOpt(textOpts, inputOptText, rangeList, dictionary, exceptions)

    if opt == 1:
        print("Add/Remove/Show Players")

    elif opt == 2:
        print("Settings")

    elif opt == 3:
        print("Play game")

    elif opt == 4:
        print("Ranking")

    elif opt == 5:
        print("Reports")

    elif opt == 6:
        leave = True
