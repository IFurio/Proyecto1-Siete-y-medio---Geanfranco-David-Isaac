# Imports
from les_meves_funcions.funcions_menu import *
from les_meves_funcions.funcions_joc import *
from pyfiglet import figlet_format


# Variables
leave = False

# Loops
while not leave:
    opt = getOpt(menus["00"]["header"],
                 menus["00"]["textOpts"],
                 menus["00"]["inputOptText"],
                 menus["00"]["rangeList"], {}, [])

    if opt == 1:
        opt = getOpt(menus["01"]["header"],
                     menus["01"]["textOpts"],
                     menus["01"]["inputOptText"],
                     menus["01"]["rangeList"], {}, [])

    elif opt == 2:
        opt = getOpt(menus["02"]["header"],
                     menus["02"]["textOpts"],
                     menus["02"]["inputOptText"],
                     menus["02"]["rangeList"], {}, [])

    elif opt == 3:
        the_game_starts = check_settings()
        if the_game_starts:
            print("Play game")
            round_loop()
    elif opt == 4:
        print("Ranking")

    elif opt == 5:
        print("Reports")

    elif opt == 6:
        leave = True
