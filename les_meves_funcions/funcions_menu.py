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

            users = humans + boots
            dnis = ["quit"]

            for user in users:
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
            humans, boots = fetchPlayers()

            headeractual = "*" * 95 + "\n" + figlet_format("".ljust(32) + "S H O W", font="doom") + "*" * 95 + "\n" \
                           + "ACTUAL PLAYERS IN GAME".center(95) + "\n"

            data = ""
            print(contextGame["players"])
            for player in contextGame["players"]:
                data += player + " " + players[player]["name"] + " "
                if players[player]["human"]:
                    data += "human"

                else:
                    data += "boot"

                if players[player]["type"] == 30:
                    data += "Cautious"

                if players[player]["type"] == 40:
                    data += "Moderated"

                if players[player]["type"] == 50:
                    data += "Bold"

                data += "\n"

            print(headeractual, data)
            input("Enter to continue".center(95))

            data = "=" * 95 + "\n" + "Boots".rjust(24) + "||".center(46) + "Humans\n" + "*" * 95 + "\n" + \
                   "ID".ljust(15) + "Name".ljust(20) + "Profile".ljust(11) + "||".ljust(4) + \
                    "ID".ljust(15) + "Name".ljust(20) + "Profile".ljust(11) + "\n" + "*" * 95 + "\n"

            if len(humans) > len(boots):
                lenght = len(humans)
            else:
                lenght = len(boots)

            for i in range(lenght):
                if len(boots) - 1 < i:
                    data += " " * 46 + "||".ljust(4)
                else:
                    data += boots[i][0].ljust(15) + boots[i][1].ljust(20) + boots[i][2].ljust(11) + "||".ljust(4)
                if len(humans) - 1 < i:
                    data += " " * 46 + "\n"
                else:
                    data += humans[i][0].ljust(15) + humans[i][1].ljust(20) + humans[i][2].ljust(11) + "\n"

            users = humans + boots
            dnis = ["quit", "sh"]

            for user in users:
                dnis.append("-" + user[0])
                dnis.append(user[0])

            header = "*" * 95 + "\n" + figlet_format("".ljust(23) + "P l a y e r s", font="doom") + "*" * 95 + "\n" \
                     + "Add or remove players".center(95)

            opt = getOpt(header, data + "=" * 95, "Option ( -id to remove player, id to add player, sh to show actual "
                                                  "players in game 'quit' to exit)\n", [], {}, dnis)

            if opt != "quit" and opt != "sh":
                if opt[0] == "-":
                    opt = opt[1:]
                    answer = input("Do you want to remove " + opt + "?\nY/y = yes: ")
                    if answer == "y" or answer == "Y":
                        contextGame["players"].remove(opt)
                        players.pop(opt)
                        print("Player has been removed!!!")
                        input("Enter to continue")
                    else:
                        print("Player not removed!!!")
                        input("Enter to continue")

                else:
                    answer = input("Do you want to add " + opt + "?\nY/y = yes: ")
                    if answer == "y" or answer == "Y":
                        contextGame["players"].append(opt)
                        humans, boots = fetchPlayers("int")
                        for i in range(lenght):
                            if not len(boots) - 1 < i:
                                if opt in boots[i]:
                                    players[opt] = {"name": boots[i][1], "human": boots[i][3], "bank": False, "initial_card": "",
                                                    "priority": 0, "type": boots[i][2], "bet": 0, "points": 0, "cards": [],
                                                    "round_points": 0}
                            if not len(humans) - 1 < i:
                                data += " " * 46 + "\n"

                        print("Player has been added!!!")
                        input("Enter to continue")
                    else:
                        print("Player not added!!!")
                        input("Enter to continue")

            elif opt == "sh":
                print("lista de actual players")

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
