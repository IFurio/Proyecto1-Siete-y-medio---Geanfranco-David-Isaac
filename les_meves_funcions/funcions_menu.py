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

            headeractual = "*" * 95 + "\n" + figlet_format("".ljust(32) + "S H O W", font="doom") + "*" * 95 + "\n" \
                           + "ACTUAL PLAYERS IN GAME".center(95) + "\n"

            data = ""
            for player in contextGame["players"]:
                data += player.rjust(40) + " - " + players[player]["name"] + " - "
                if players[player]["human"]:
                    data += "human - "

                else:
                    data += "boot - "

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

            humans, boots = fetchPlayers()

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

            header = "*" * 95 + "\n" + figlet_format("".ljust(23) + "P l a y e r s", font="doom") + "*" * 95 + "\n"\
                     + "Add or remove players".center(95)

            while True:

                opt = getOpt(header, data + "=" * 95, "Option ( -id to remove player, id to add player, sh to show actual "
                                                      "players in game 'quit' to exit)\n", [], {}, dnis)

                if opt != "quit" and opt != "sh":
                    if opt[0] == "-":
                        opt = opt[1:]
                        if opt in contextGame["players"]:
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
                            print("This player is not in the game.")
                            input("Enter to continue")

                    elif opt not in contextGame["players"] and len(contextGame["players"]) < 6:
                        answer = input("Do you want to add " + opt + "?\nY/y = yes: ")
                        if answer == "y" or answer == "Y":
                            contextGame["players"].append(opt)
                            humans, boots = fetchPlayers("int")
                            for i in range(lenght):
                                if not len(boots) - 1 < i:
                                    if opt in boots[i]:
                                        players[opt] = {"name": boots[i][1], "human": boots[i][3], "bank": False,
                                                        "initial_card": "",
                                                        "priority": 0, "type": boots[i][2], "bet": 0, "points": 0,
                                                        "cards": [],
                                                        "round_points": 0}
                                if not len(humans) - 1 < i:
                                    if opt in humans[i]:
                                        players[opt] = {"name": humans[i][1], "human": humans[i][3], "bank": False,
                                                        "initial_card": "",
                                                        "priority": 0, "type": humans[i][2], "bet": 0, "points": 0,
                                                        "cards": [],
                                                        "round_points": 0}

                            print("Player has been added!!!")
                            input("Enter to continue")
                        else:
                            print("Player not added!!!")
                            input("Enter to continue")
                    else:
                        if opt in contextGame["players"]:
                            print("The player " + opt + " is in the game.")
                        else:
                            print("The game can only have six players.")
                        input("Enter to continue")

                elif opt == "sh":
                    datos = ""
                    for player in contextGame["players"]:
                        datos += player.rjust(40) + " - " + players[player]["name"] + " - "
                        if players[player]["human"]:
                            datos += "human - "

                        else:
                            datos += "boot - "

                        if players[player]["type"] == 30:
                            datos += "Cautious"

                        if players[player]["type"] == 40:
                            datos += "Moderated"

                        if players[player]["type"] == 50:
                            datos += "Bold"

                        datos += "\n"

                    print(headeractual, datos)
                    input("Enter to continue".center(95))

                else:
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
                rounds = input("How many rounds do you want to play? ")
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
            query = "select * from ranking order by gained_points desc"
            data_menu = SelectBBDD(query)
            ranking_1 = "\n" + "*" * 80 + "\n" + "Player ID".ljust(10) + " "*5 + "Earnings".ljust(25) + "Games played".rjust(15) + " "*5 + "Minutes Played".rjust(15) + "\n" + "*" * 80 + "\n"
            for i in data_menu:
                ranking_1 += str(i[0]).rjust(10) + " "*5 + str(i[1]).ljust(25) + str(i[2]).rjust(15) + " "*5 + str(i[3]).rjust(15) + "\n"
            print(ranking_1)
            input("Press enter to continue")
        elif opt == 2:
            query = "select * from ranking order by games_played desc"
            data_menu = SelectBBDD(query)
            ranking_2 = "\n" + "*" * 80 + "\n" + "Player ID".ljust(10) + " "*5 + "Earnings".ljust(25) + "Games played".rjust(15) + " "*5 + "Minutes Played".rjust(15) + "\n" + "*" * 80 + "\n"
            for i in data_menu:
                ranking_2 += str(i[0]).rjust(10) + " "*5 + str(i[1]).ljust(25) + str(i[2]).rjust(15) + " "*5 + str(i[3]).rjust(15) + "\n"
            print(ranking_2)
            input("Press enter to continue")
        elif opt == 3:
            query = "select * from ranking order by time_played desc"
            data_menu = SelectBBDD(query)
            ranking_3 = "\n" + "*" * 80 + "\n" + "Player ID".ljust(10) + " "*5 + "Earnings".ljust(25) + "Games played".rjust(15) + " "*5 + "Minutes Played".rjust(15) + "\n" + "*" * 80 + "\n"
            for i in data_menu:
                ranking_3 += str(i[0]).rjust(10) + " "*5 + str(i[1]).ljust(25) + str(i[2]).rjust(15) + " "*5 + str(i[3]).rjust(15) + "\n"
            print(ranking_3)
            input("Press enter to continue")
        else:
            break


def menu05():
    while True:
        opt = getOpt(menus["05"]["header"],
                     menus["05"]["textOpts"],
                     menus["05"]["inputOptText"],
                     menus["05"]["rangeList"], {}, [])
        if opt == 1:
            print("No implementado")
            input("ENTER TO CONTINUE")
        elif opt == 2:
            query = "SELECT player_game.cardgame_id, player_game_round.player_id, MAX(player_game_round.bet_points) as 'max_bet' FROM player_game_round INNER JOIN (SELECT cardgame_id, MAX(bet_points) as max_bet FROM player_game_round WHERE bet_points > 0 GROUP BY cardgame_id) as max_bet ON player_game_round.cardgame_id = max_bet.cardgame_id AND player_game_round.bet_points = max_bet.max_bet INNER JOIN player_game ON player_game.cardgame_id = player_game_round.cardgame_id GROUP BY player_game.cardgame_id, player_game_round.player_id ORDER BY MAX(player_game_round.bet_points) DESC;"
            data = SelectBBDD(query)
            report3 = "Max bet in every game".center(62, "*") + "\n" + "Card game ID".ljust(28) + "Player ID".ljust(24) + "Max Bet\n" + "=" * 62 + "\n"
            for game in data:
                report3 += str(game[0]).rjust(7) + str(game[1]).rjust(30) + str(game[2]).rjust(20) + "\n"
            print(report3 + "=" * 62)
            input("Enter to continue\n")

        elif opt == 3:
            query = "SELECT player_game.cardgame_id, player_game_round.player_id, MIN(player_game_round.bet_points) as 'lowest_bet' FROM player_game_round INNER JOIN (SELECT cardgame_id, MIN(bet_points) as lowest_bet FROM player_game_round WHERE bet_points > 0 GROUP BY cardgame_id) as lowest_bets ON player_game_round.cardgame_id = lowest_bets.cardgame_id AND player_game_round.bet_points = lowest_bets.lowest_bet INNER JOIN player_game ON player_game.cardgame_id = player_game_round.cardgame_id GROUP BY player_game.cardgame_id, player_game_round.player_id ORDER BY MIN(player_game_round.bet_points) ASC;"
            data = SelectBBDD(query)
            report3 = "Lowest bet in every game".center(62, "*") + "\n" + "Card game ID".ljust(28) + "Player ID".ljust(24) + "Lowest Bet\n" + "=" * 62 + "\n"
            for game in data:
                report3 += str(game[0]).rjust(7) + str(game[1]).rjust(30) + str(game[2]).rjust(20) + "\n"
            print(report3 + "=" * 62)
            input("Enter to continue\n")

        elif opt == 4:
            print("No implementado")
            input("ENTER TO CONTINUE")
        elif opt == 5:
            print("No implementado")
            input("ENTER TO CONTINUE")
        elif opt == 6:
            print("No implementado")
            input("ENTER TO CONTINUE")
        elif opt == 7:
            query = "select cardgame_id, count(is_bank) as bank_players from player_game_round where is_bank=1 group by cardgame_id"
            data_menu = SelectBBDD(query)
            report_7 = "\n" + "*" * 40 + "\n" + "ID Game".ljust(10) + "Users who have been bank".rjust(25) + "\n" + "*" * 40 + "\n"
            for i in data_menu:
                report_7 += str(i[0]).rjust(7) + str(i[1]).rjust(25) + "\n"
            print(report_7)
            input("Press enter to continue")
        elif opt == 8:
            query = "select cardgame_id, avg(bet_points) from player_game_round group by cardgame_id"
            data_menu = SelectBBDD(query)
            report_8 = "\n" + "*" * 40 + "\n" + "ID Game".ljust(10) + "Average bet".rjust(
                25) + "\n" + "*" * 40 + "\n"
            for i in data_menu:
                report_8 += str(i[0]).rjust(7) + str(i[1]).rjust(25) + "\n"
            print(report_8)
            input("Press enter to continue")
        elif opt == 9:
            query = "select cardgame_id, avg(bet_points) as avg_bet, round_num from player_game_round where bet_points != 0 and round_num = 1 group by cardgame_id, round_num"
            data_menu = SelectBBDD(query)
            report_8 = "\n" + "*" * 40 + "\n" + "ID Game".ljust(10) + "Average bet 1st round".rjust(
                25) + "\n" + "*" * 40 + "\n"
            for i in data_menu:
                report_8 += str(i[0]).rjust(7) + str(i[1]).rjust(25) + "\n"
            print(report_8)
            input("Press enter to continue")
        elif opt == 10:
            print("No implementado")
            input("ENTER TO CONTINUE")
        else:
            break
