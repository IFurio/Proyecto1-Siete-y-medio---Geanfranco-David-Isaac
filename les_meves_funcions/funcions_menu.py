# Imports
from les_meves_funcions.funcions_generals import *
from les_meves_funcions.datos import *


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
            print()
        elif opt == 2:
            print()
        elif opt == 3:
            humans, boots = fetchPlayers()

            if len(humans) > len(boots):
                lenght = len(humans)
            else:
                lenght = len(boots)

            data = ""
            for i in range(lenght):
                if len(boots) - 1 < i:
                    data += " " * 20 + "|| "
                else:
                    data += boots[i][0] + " " + boots[i][1] + " " + boots[i][2] + " || "
                if len(humans) - 1 < i:
                    data += " " * 20 + "\n"
                else:
                    data += humans[i][0] + " " + humans[i][1] + " " + humans[i][2] + "\n"

            print(data)

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
                rounds = input("How much rounds you want to play? ")
                if not rounds.isdigit():
                    print("¡ERROR!")
                elif int(rounds) > 30 or int(rounds) < 5:
                    print("¡ERROR!")
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
