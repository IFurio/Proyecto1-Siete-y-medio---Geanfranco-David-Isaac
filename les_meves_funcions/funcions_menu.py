# Imports
from les_meves_funcions.funcions_generals import *


# Funciones de menus
def getOpt(header, textOpts, inputOptText, rangeList, dictionary, exceptions):
    while True:
        # Imprime la cabecera
        print(header)
        # Imprime las opciones
        print(textOpts)
        # Le pide al usuario la opcion
        opt = input(inputOptText)
        # Intenta pasar la opcion del usuario a int, si puede comprueba si la opt esta en alguno de los parametros
        try:
            opt = int(opt)
            if opt in rangeList:
                return opt

            elif opt in dictionary:
                return opt

            elif opt in exceptions:
                return opt

            # Si la opt no esta en ningun parametro anterior envia un mensaje de error
            else:
                print("Invalid option".center(100, "="))
                input("Enter to continue".center(100))

        # Si no puede pasar la opt a int, captura el error y comprueba si la opt esta en alguno de los parametros pero
        # Esta vez como str
        except ValueError:
            if opt in exceptions:
                return opt

            elif opt in dictionary:
                return opt

            # Si no encuentra la opt en ninguno de los parametros anteriores imprime un mensaje de error
            else:
                print("Invalid option".center(100, "="))
                input("Enter to continue".center(100))


def menu01():
    while True:
        opt = getOpt(menus["01"]["header"],
                     menus["01"]["textOpts"],
                     menus["01"]["inputOptText"],
                     menus["01"]["rangeList"], {}, [])
        if opt == 1:
            newPlayer_human()
        elif opt == 2:
            newPlayer_boot()
        elif opt == 3:
            humans, boots = fetchPlayers()

            if len(humans) > len(boots):
                lenght = len(humans)
            else:
                lenght = len(boots)

            data = "=" * 95 + "\n" + "Boots".rjust(24) + "||".center(46) + "Humans\n" + "*" * 95 + "\n" + \
                   "ID".ljust(15) + "Name".ljust(20) + "Profile".ljust(11) + "||".ljust(4) + \
                   "ID".ljust(15) + "Name".ljust(20) + "Profile".ljust(11) + "\n" + "*" * 95 + "\n"
            for i in range(lenght):
                if len(boots) - 1 < i:
                    data += " " * 46 + "||".ljust(4)
                else:
                    data += boots[i][0].ljust(15) + boots[i][1].ljust(20) + boots[i][2].ljust(11) + "||".ljust(4)
                if len(humans) - 1 < i:
                    data += " " * 46 + "\n"
                else:
                    data += humans[i][0].ljust(15) + humans[i][1].ljust(20) + humans[i][2].ljust(11) + "\n"

            #######################################
            ########## REVISAR IMPORTANTE #########
            #######################################
            players = humans + boots
            dnis = ["quit"]

            for user in players:
                dnis.append("-" + user[0])

            header = "*" * 95 + "\n" + figlet_format("".ljust(23) + "P l a y e r s", font="doom") + "*" * 95 + "\n" \
                     + "Show or remove players".center(94)

            opt = getOpt(header, data + "=" * 95, "Option ( -id to remove player, 'quit' to exit)\n", [], {}, dnis)

            if opt != "quit":
                opt = opt[1:]
                answer = input("Do you want to remove " + opt + "?\nY/y = yes: ")
                if answer == "y" or answer == "Y":
                    query = "Delete from player where player_id = '{}'".format(opt)
                    InputBBDD(query)
                    print("Player has been removed!!!")
                else:
                    print("Player not removed!!!")
                    input("Enter to continue")

        else:
            break


def menu02():
    while True:
        opt = getOpt(menus["02"]["header"],
                     menus["02"]["textOpts"],
                     menus["02"]["inputOptText"],
                     menus["02"]["rangeList"], {}, [])
        if opt == 1:
            humans, boots = fetchPlayers("int")

            if len(humans) > len(boots):
                lenght = len(humans)
            else:
                lenght = len(boots)

            for i in range(lenght):
                if len(boots) - 1 >= i:
                    players[boots[i][0]] = {"name": boots[i][1], "human": boots[i][3], "type": boots[i][2],
                                            "bank": False, "initial_card": "", "priority": 0, "bet": 0, "points": 0,
                                            "cards": [], "round_points": 0}

                    contextGame["players"].append(boots[i][0])

                if len(humans) - 1 >= i:
                    players[humans[i][0]] = {"name": humans[i][1], "human": humans[i][3], "type": humans[i][2],
                                             "bank": False, "initial_card": "", "priority": 0, "bet": 0, "points": 0,
                                             "cards": [], "round_points": 0}

                    contextGame["players"].append(humans[i][0])
                if i == 2:
                    break

        elif opt == 2:
            opt = getOpt(menus["02"]["header"],
                         "1)Spanish deck\n2)Poker deck\n3)Go out",
                         menus["02"]["inputOptText"],
                         [1, 2, 3], {}, [])
            if opt == 1:
                contextGame["deck"] = "ESP"
            elif opt == 2:
                contextGame["deck"] = "POK"

        elif opt == 3:
            while True:
                print(menuRounds)
                rounds = input("1"
                               "How many rounds do you want to play? ")
                if not rounds.isdigit():
                    print("Only numbers accepted")
                elif int(rounds) > 30 or int(rounds) < 5:
                    print("Number of rounds has to be between 5 and 30")
                else:
                    contextGame["maxRounds"] = int(rounds)
                    break

        else:
            break


def menu04():
    while True:
        opt = getOpt(menus["04"]["header"],
                     menus["04"]["textOpts"],
                     menus["04"]["inputOptText"],
                     menus["04"]["rangeList"], {}, [])
        if opt == 1:
            print()
        elif opt == 2:
            print()
        elif opt == 3:
            print()
        else:
            break


def menu05():
    while True:
        opt = getOpt(menus["05"]["header"],
                     menus["05"]["textOpts"],
                     menus["05"]["inputOptText"],
                     menus["05"]["rangeList"], {}, [])
        if opt == 1:
            print()
        elif opt == 2:
            print()
        elif opt == 3:
            print()
        elif opt == 4:
            print()
        elif opt == 5:
            print()
        elif opt == 6:
            print()
        elif opt == 7:
            print()
        elif opt == 8:
            print()
        elif opt == 9:
            print()
        elif opt == 10:
            print()
        else:
            break
