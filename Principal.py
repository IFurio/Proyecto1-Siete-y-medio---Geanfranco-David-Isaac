# Imports
from les_meves_funcions.funcions_joc import *
from les_meves_funcions.funcions_menu import *
from les_meves_funcions.datos import *
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
        # Comprobamos que este correcto y entramos en la partida
        the_game_starts = check_settings()
        if the_game_starts:
            # Se preparan las cosas para que empiece la partida
            SetRound_setting()

            # Guardamos datos de players que necesitamos del princio de la partida
            addDataToPlayerGame("beginning")

            # Bucle en el que se juegan las partidas
            round_loop()

            # Se guardan datos de partida y players que necesitamos del final de la partida
            addDataToCardGame("final")
            addDataToPlayerGame("final")

            # Funcion para mostrar ganadores
            checkWinner()
            print("*" * 95 + "\n" +
                  figlet_format(" " * 11 + "W i n n e r :", font="doom") +
                  figlet_format(" " * 11 + players[contextGame["players"][-1]]["name"], font="doom") +
                  "*" * 95 + "\n\n")

            input("Enter to continue")

            # En este momento se hacen los inserts
            addDataToCardGame("insert")
            addDataToPlayerGame("insert")
            addDataToPlayerGameRound("insert")

            # Se reinician todos los diccionarios y las variables
            resetDicts()

    elif opt == 4:
        menu04()

    elif opt == 5:
        menu05()

    elif opt == 6:
        leave = True
