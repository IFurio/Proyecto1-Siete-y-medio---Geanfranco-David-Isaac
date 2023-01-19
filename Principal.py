# Imports
from les_meves_funcions.funcions_menu import *
from les_meves_funcions.funcions_consultesDB import *
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
        menu01()

    elif opt == 2:
        menu02()

    elif opt == 3:
        the_game_starts = check_settings()
        if the_game_starts:
            SetRound_setting()
            addDataToPlayerGame("beginning")
            round_loop()
            addDataToCardGame("")
            addDataToPlayerGame("")

            print(cardgame)
            print(player_game)
            print(player_game_round)

            players = {}
            contextGame["players"] = []
            contextGame["deck"] = ""
            contextGame["round"] = 0
            contextGame["maxRounds"] = 0

    elif opt == 4:
        menu04()

    elif opt == 5:
        menu05()

    elif opt == 6:
        leave = True
