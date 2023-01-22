# Imports
from les_meves_funcions.funcions_menu import *
from les_meves_funcions.datos import *
import random


# Funcion de comprobaciones
def check_settings():
    try:
        if len(contextGame["players"]) < 2:
            raise ValueError("Select 2 players or more to start the game!")

        if contextGame["deck"] == "":
            raise ValueError("Select a card deck to start the game!")
        else:
            # Una vez sabemos que hay un mazo seleccionado y suficientes jugadores para empezar la partida,
            # guardamos la info inicial de la partida (mirar archivo funciones_consultasDB, funcion addDataToCardGame)
            # y hacemos una consulta en la DB para crear el mazo.
            addDataToCardGame("beginning")
            contextGame["deck"] = fetchCards(contextGame["deck"])

        if contextGame["maxRounds"] == 0:
            contextGame["maxRounds"] = 5

    except ValueError as fail:
        print(fail)
        return False

    return True


# Funcion para comprabarsi tiene que terminar la partida
def checkMinimun2PlayerInGame():
    count = 0
    for player_id in contextGame["players"]:
        if players[player_id]["points"] > 0:
            count += 1

    if count < 2:
        return False

    else:
        return True


# Funcion para robar cartas
def drawCard(deckList):
    # Se coje un numero aleatorio dentro de el rango de cartas que tenemos
    card = deckList[random.randint(0, len(deckList) - 1)]
    # Quitamos la carta de la deck list
    deckList.remove(card)
    # Hacemos un return con el nombre de la carta
    return card


# Funcion para ordenar jugadores.
# Se ordenan en una lista dentro de contextGame["players"] en orden ascendente para sinplificar el curso de la partida.
def orderPlayers():
    for pas in range(len(contextGame["players"]) - 1):
        # Esta variable sirve para no tener que hacer comprobaciones de mas
        listIsOrdered = True
        for i in range(len(contextGame["players"]) - 1 - pas):
            # Aqui se comprueba si la carta inicial del jugador i es mas alta que la de i + 1 y se cambia de puesto.
            if contextGame["deck"][players[contextGame["players"][i]]["initial_card"]]["value"] > contextGame["deck"][players[contextGame["players"][i + 1]]["initial_card"]]["value"]:
                changeBox = contextGame["players"][i]
                contextGame["players"][i] = contextGame["players"][i + 1]
                contextGame["players"][i + 1] = changeBox
                listIsOrdered = False

            # Si los dos jugadores sacan la misma cifra se comprueban las prioridades de las cartas.
            elif contextGame["deck"][players[contextGame["players"][i]]["initial_card"]]["value"] == contextGame["deck"][players[contextGame["players"][i + 1]]["initial_card"]]["value"]:
                if contextGame["deck"][players[contextGame["players"][i]]["initial_card"]]["priority"] > contextGame["deck"][players[contextGame["players"][i + 1]]["initial_card"]]["priority"]:
                    changeBox = contextGame["players"][i]
                    contextGame["players"][i] = contextGame["players"][i + 1]
                    contextGame["players"][i + 1] = changeBox
                    listIsOrdered = False

        # Se rompe el for por que ya esta all ordered
        if listIsOrdered:
            break


# Funcion general para llamar a las demas funciones y hacer los sets.
def SetRound_setting():
    # Ponemos los puntos iniciales
    Set_InitialPoints()
    # Definimos la prioridad de los jugadores
    SetPriority()


# Poner los puntos de inicio a cada jugador (20)
def Set_InitialPoints():
    # Accedemos a la lista de jugadores que van a participar
    # en la partida y les ponemos los puntos iterando en la lista.
    for player in contextGame["players"]:
        players[player]["points"] = 20


# Definir la prioridad de cada jugador antes de comenzar la partiad.
def SetPriority():
    # Se crea el mazo
    deck = list(contextGame["deck"].keys())
    # Se reparten cartas
    for player in contextGame["players"]:
        players[player]["initial_card"] = drawCard(deck)

    # Ordenamos a los players en funcion de la carta repartida
    orderPlayers()

    # Se les asigna la prioridad a los players
    for i in range(len(contextGame["players"])):
        players[contextGame["players"][i]]["priority"] = i + 1

    # Se le da banca al jugador con mas prioridad
    players[contextGame["players"][-1]]["bank"] = True
    # Se apunta ese jugador en contextGame["bank"]
    contextGame["bank"] = contextGame["players"][-1]


# Funcion para saber el ganador de la partida
def checkWinner():
    for pas in range(len(contextGame["players"]) - 1):
        # Variable para dejar de comprobar cuando ya esta ordenado
        listIsOrdered = True
        for i in range(len(contextGame["players"]) - 1 - pas):
            # Ordenamos los players en funcion de sus puntos
            if players[contextGame["players"][i]]["points"] > players[contextGame["players"][i + 1]]["points"]:
                changeBox = contextGame["players"][i]
                contextGame["players"][i] = contextGame["players"][i + 1]
                contextGame["players"][i + 1] = changeBox
                listIsOrdered = False

            # Si empatan a puntos se hace el desempate por prioridad
            elif players[contextGame["players"][i]]["points"] == players[contextGame["players"][i + 1]]["points"]:
                if players[contextGame["players"][i]]["priority"] > players[contextGame["players"][i + 1]]["priority"]:
                    changeBox = contextGame["players"][i]
                    contextGame["players"][i] = contextGame["players"][i + 1]
                    contextGame["players"][i + 1] = changeBox
                    listIsOrdered = False

        # Si listIsOrdered es True es que ya no queda nada por ordenar, termina de iterar
        if listIsOrdered:
            break


# Funcion para apuestas
def setPlayersBet():
    for player in contextGame["players"]:
        # Si el jugador no es banca se hacen apuestas
        if not players[player]["bank"]:
            # Si el jugador es humano se le pregunta si quiere apostar a mano o automaticamente
            if players[player]["human"]:
                if players[player]["points"] <= 5:
                    opt = getOpt("\n" + "Elige tu apuesta " + player + ":",
                                 "\nBank points: " + str(players[contextGame["bank"]]["points"]) +
                                 "\nYour points: " + str(players[player]["points"]) + "\n" +
                                 "\n1)Automatic - " + str(players[player]["points"]) +
                                 "\n2)Manual", "Option:\n", [1, 2], {}, [])
                else:
                    opt = getOpt("\n" + "Elige tu apuesta " + player + ":",
                                 "\nBank points: " + str(players[contextGame["bank"]]["points"]) +
                                 "\nYour points: " + str(players[player]["points"]) + "\n" +
                                 "\n1)Automatic - " + str((players[player]["type"] * players[player]["points"]) // 100) +
                                 "\n2)Manual", "Option:\n", [1, 2], {}, [])
                # Modo automatico
                if opt == 1:
                    if players[player]["points"] <= 5:
                        bet = players[player]["points"]
                        if bet > players[contextGame["bank"]]["points"]:
                            bet = players[contextGame["bank"]]["points"]
                            players[player]["bet"] = bet
                        else:
                            players[player]["bet"] = bet
                    else:
                        bet = (players[player]["type"] * players[player]["points"]) // 100
                        if bet > players[contextGame["bank"]]["points"]:
                            bet = players[contextGame["bank"]]["points"]
                            players[player]["bet"] = bet
                        else:
                            players[player]["bet"] = bet

                # Modo manual
                else:
                    while True:
                        # Le pedimos al jugador la apuesta.
                        print("Select your bet " + player + ":")
                        bet = input("Bet: \n")
                        # Miramos si es un numero.
                        if not bet.isdigit():
                            print("The bet need to be numeric.")
                        # Le impedimos que apueste mas que sus puntos.
                        elif int(bet) > players[player]["points"]:
                            print("Your bet can't be more than your points.")
                        # Le impedimos que apueste mas que los puntos de la banca.
                        elif int(bet) > players[contextGame["bank"]]["points"]:
                            print("Caution this be is highest than the bank points.")
                        elif int(bet) <= 0:
                            print("Your bet cant be 0.")
                        else:
                            players[player]["bet"] = int(bet)
                            break

            # A los boots se les apuesta automaticamente
            else:
                if players[player]["points"] <= 5:
                    bet = players[player]["points"]
                    if bet > players[contextGame["bank"]]["points"]:
                        bet = players[contextGame["bank"]]["points"]
                        players[player]["bet"] = bet
                    else:
                        players[player]["bet"] = bet
                else:
                    bet = (players[player]["type"] * players[player]["points"]) // 100
                    if bet > players[contextGame["bank"]]["points"]:
                        bet = players[contextGame["bank"]]["points"]
                        players[player]["bet"] = bet
                    else:
                        players[player]["bet"] = bet


# Funcion para pagar y cobrar apuestas y guardar los candidatos a banca
def pointsDistribution(bank, candidates):
    # Recorremos la lista de final a principio, para que la banca pague en orden de prioridad
    for i in range(len(contextGame["players"]) - 2, -1, -1):
        # En este if se entra si la banca le a ganado la ronda a este jugador
        if players[contextGame["players"][i]]["round_points"] <= players[bank]["round_points"]:
            # Comprobamos que la banca no se haya pasado de siete y medio y entonces se hacen los pagos.
            if players[bank]["round_points"] != -1:
                # El jugador paga a la banca lo que haya apostado
                players[contextGame["players"][i]]["points"] -= players[contextGame["players"][i]]["bet"]
                players[bank]["points"] += players[contextGame["players"][i]]["bet"]

        # En este else se entre si el jugador gana la ronda a la banca
        else:
            # If para saber si el jugador a sacado 7.5 y por lo tanto hay que pagarle doble
            if players[contextGame["players"][i]]["round_points"] == 7.5:
                # Si a sacado 7.5 lo añadimos a banc candidates.
                candidates.append(contextGame["players"][i])
                # Comprobamos si la banca tiene suficientes puntos para pagar esta apuesta.
                if players[contextGame["players"][i]]["bet"] * 2 > players[bank]["points"]:
                    # Si no tenia sufuciente la banca paga todos los puntos que le queden y termina de pagar apuestas.
                    players[contextGame["players"][i]]["points"] += players[bank]["points"]
                    players[bank]["points"] = 0
                    break
                else:
                    # Si tiene suficiente le paga lo que le debe
                    players[contextGame["players"][i]]["points"] += (players[contextGame["players"][i]]["bet"] * 2)
                    players[bank]["points"] -= (players[contextGame["players"][i]]["bet"] * 2)

            # Aqui entra para pagar normal
            else:
                # Comprobamos si la banca tiene suficientes puntos para pagar esta apuesta.
                if players[contextGame["players"][i]]["bet"] > players[bank]["points"]:
                    # Si no tenia sufuciente la banca paga todos los puntos que le queden y termina de pagar apuestas.
                    players[contextGame["players"][i]]["points"] += players[bank]["points"]
                    players[bank]["points"] = 0
                    break
                else:
                    # Si tiene suficiente le paga lo que le debe
                    players[contextGame["players"][i]]["points"] += players[contextGame["players"][i]]["bet"]
                    players[bank]["points"] -= players[contextGame["players"][i]]["bet"]


# Funcion calculo de probabilidad de pasar 7 y medio
def probToPass(points, deckList):
    # Este count sirve para saber cuantas cartas hacen que te pases de 7 y medio
    count = 0
    for card in deckList:
        if contextGame["deck"][card]["realValue"] + points > 7.5:
            count += 1

    # Cuando ya tenemos todas las cartas que nos hacen pasarnos hacemos el calculo y lo devolvemos
    return (count * 100) / len(deckList)


# Funcion para saber cuantos jugadores ganan a la banca y cuanto es el total a pagar
def playersWinningBank(bank):
    count = 0
    points = 0
    for player in contextGame["players"]:
        if not players[player]["bank"]:
            if players[bank]["round_points"] < players[player]["round_points"]:
                count += 1
                points += players[player]["bet"]
    return count, points


# Funcion loop de las rondas
def round_loop():
    # La partida se juega mientras las rondas no pasan del maximo o mientras haya un minimo de dos jugadores con puntos
    while checkMinimun2PlayerInGame() and contextGame["round"] <= contextGame["maxRounds"]:
        # Se devuelven las cartas al mazo, se ponen los puntos a cero y se resetean los candidatos a la banca
        bankCandidates = []
        for player in contextGame["players"]:
            players[player]["cards"] = []
            players[player]["round_points"] = 0
        deck = list(contextGame["deck"].keys())

        # Se hacen las apuestas
        setPlayersBet()

        # Se introducen datos en player_game_round
        addDataToPlayerGameRound("beginning")

        # Loop para que cada jugador juegue su turno
        for player in contextGame["players"]:
            # La variable automatic sirve para que los humanos puedan jugar como bots
            automatic = False

            # Sin preguntar al jugador lo primero que hacemos es darle una carta para robar. (de esta no se libran)
            card = drawCard(deck)
            players[player]["cards"].append(card)
            players[player]["round_points"] += contextGame["deck"][card]["realValue"]

            # Si el player es humano entra en este menu
            if players[player]["human"]:
                # Lo primero que hacemos al entrar es enseñarle la carta que le acabamos de dar.
                print("Hi player " + player + " you had drawn " + card)
                input("Press ENTER to start your round")

                while True:
                    opt = getOpt(menus["game"]["header"],
                                 "Your hand: " + str(players[player]["cards"]) + "\n" +
                                 "Your points: " + str(players[player]["round_points"]) + "\n" +
                                 menus["game"]["textOpts"],
                                 menus["game"]["inputOptText"],
                                 menus["game"]["rangeList"], {}, [])

                    # La primera opcion del menu es draw a card
                    if opt == 1:
                        # Solo le repartimos carta si tiene menos de siete y medio
                        if players[player]["round_points"] < 7.5:
                            # Cuando pide carta le enseñamos la probabilidad que tiene de pasarse
                            print("Your probability to pass seven and half is " +
                                  str(probToPass(players[player]["round_points"], deck)))

                            # Le preguntamos si aun quiere la carta
                            while True:
                                draw = input("Are you sure to draw a card? Y/N\n")
                                if not draw.isalpha():
                                    print("You need to insert a letter.")
                                elif not draw.upper() in ("Y", "N"):
                                    print("The letter need to be '{}' or '{}'".format("Y", "N"))
                                else:
                                    break

                            # Si dice que si le hacemos el robo
                            if draw.upper() == "Y":
                                card = drawCard(deck)
                                players[player]["cards"].append(card)
                                players[player]["round_points"] += contextGame["deck"][card]["realValue"]
                                print("You had drawn " + card)
                                input("Press ENTER to start your round")

                        # Si no le repartimos carta miramos los puntos que tiene y le avisamos de lo que pasa
                        elif players[player]["round_points"] == 7.5:
                            print("You already have Seven and Half.")
                        else:
                            print("You have exceeded Seven and Half.")

                    elif opt == 2:
                        # Menu que printa las estadisticas del jugador humano
                        print("\n" + "Stats of player " + player + " in the actual round:\n")
                        print("Cards in hand:", players[player]["cards"])
                        print("Cards points: " + str(players[player]["round_points"]))
                        print("ProbToPass: " +
                              str(probToPass(players[player]["round_points"], deck)) + "\n")
                        print("Bet: " + str(players[player]["bet"]))
                        print("Player points: " + str(players[player]["points"]) + "\n")
                        input("INTRO CONTINUE")

                    elif opt == 3:
                        # Menu para que el humano vea las estadisticas de la partida
                        print("Round: " + str(contextGame["round"]) + " of " + str(contextGame["maxRounds"]) + "\n")
                        statsList = ["id", "name", "human", "type", "bank", "initial_card",
                                     "priority", "bet", "points", "round_points", "cards"]

                        # Utilizamos el dict players para que los jugadores derrotados tambien aparezcan
                        userList = contextGame["players"]

                        # Quisimos dibidir la tabla en dos por eso las dos variables para guardar las strings
                        top = ""
                        bottom = ""

                        # Para hacer una linea por stat iteramos sobre la statsList
                        for stat in statsList:
                            # Para printar una linea del stat actual para cada jugador isteramos sobre userList
                            for i in range(len(userList)):
                                # Este condicional lo utilizamos para hacer la division de la tabla,
                                # en caso de que i sea mayor que dos (lo que significaria que ya ha guardado 3 users),
                                # pasamos a guardar los datos en bottom
                                if i < 3:
                                    if stat == "id":
                                        top += "Player: ".ljust(15) + userList[i].ljust(40)
                                    elif stat == "round_points":
                                        top += "Round points: ".ljust(15) + \
                                                 str(players[userList[i]][stat]).ljust(40)
                                    elif stat == "initial_card":
                                        top += "Initial card: ".ljust(15) + players[userList[i]][stat].ljust(40)
                                    elif stat == "cards":
                                        top += "Cards: " + str(players[userList[i]][stat]).ljust(48)
                                    else:
                                        top += "{}: ".format(stat).ljust(15) + \
                                                 str(players[userList[i]][stat]).ljust(40)

                                else:
                                    # Para guardar los datos de bottom iteramos desde i hasta el final de la lista,
                                    # ya que i sera el cuarto jugador que es por el que queremos empezar.
                                    # Al terminar de iterar hacemos un break para no volver a iterar sobre la i, y asi
                                    # evitar datos replicados
                                    for j in range(i, len(userList)):
                                        if stat == "id":
                                            bottom += "Player: ".ljust(15) + userList[j].ljust(40)
                                        elif stat == "round_points":
                                            bottom += "Round points: ".ljust(15) + \
                                                     str(players[userList[j]][stat]).ljust(40)
                                        elif stat == "initial_card":
                                            bottom += "Initial card: ".ljust(15) + players[userList[j]][stat].ljust(40)
                                        elif stat == "cards":
                                            bottom += "Cards: " + str(players[userList[j]][stat]).ljust(48)
                                        else:
                                            bottom += "{}: ".format(stat).ljust(15) + \
                                                     str(players[userList[j]][stat]).ljust(40)

                                    bottom += "\n"
                                    break

                            top += "\n"

                        print(top)
                        print(bottom)

                    # La opcion cuatro se utiliza para jugar automaticamente,
                    # ponemos automatic a True y hacemos un break.
                    elif opt == 4:
                        automatic = True
                        break

                    # La ultima opcion es para dejar de pedir, hacemos un break y pasa de turno
                    else:
                        # Este if se utiliza para que si te pasas de 7.5 tu apuesta sea negativa
                        if players[player]["round_points"] > 7.5:
                            players[player]["round_points"] = -1
                        break

            # Aqui juegan los boots, o en caso de haber activado automatic tambien juegan los humanos
            if not players[player]["human"] or automatic:
                # Aqui juegan los jugadores normales automaticamente
                if not players[player]["bank"]:
                    # Se les da cartas en funcion de si nivel de riesgo
                    while players[player]["type"] >= probToPass(players[player]["round_points"], deck):
                        card = drawCard(deck)
                        players[player]["cards"].append(card)
                        players[player]["round_points"] += contextGame["deck"][card]["realValue"]

                    # Este if se utiliza para que si te pasas de 7.5 tu apuesta sea negativa
                    if players[player]["round_points"] > 7.5:
                        players[player]["round_points"] = -1

                # Aqui juega la banca
                else:
                    while True:
                        # Guardamos en count la cantidad de jugadores que nos superan
                        # y en points los puntos que pagaremos
                        count, points = playersWinningBank(player)

                        # Si la banca gana a todos los jugadores se planta
                        if count == 0:
                            break

                        # En esta comparacion la banca pide como un jugador normal
                        elif players[player]["type"] >= probToPass(players[player]["round_points"], deck):
                            card = drawCard(deck)
                            players[player]["cards"].append(card)
                            players[player]["round_points"] += contextGame["deck"][card]["realValue"]

                        # Aqui comprovamos si la banca se quedara sin puntos o si todos los jugadores ganan a la banca
                        elif count == len(contextGame["players"]) - 1 or points >= players[player]["points"]:
                            card = drawCard(deck)
                            players[player]["cards"].append(card)
                            players[player]["round_points"] += contextGame["deck"][card]["realValue"]

                        # En caso de que su nivel de riesgo se pase se planta
                        else:
                            break

                    # Este if se utiliza para que si te pasas de 7.5 tu apuesta sea negativa
                    if players[player]["round_points"] > 7.5:
                        players[player]["round_points"] = -1

        # Utilizamos esta variable para repartir los puntos en orden de prioridad y se apuntan candidatos a bank
        pointsDistribution(contextGame["bank"], bankCandidates)

        # Hueco para insert de ronda
        addDataToPlayerGameRound("final")

        # Printamos la tabla de jugadores
        print("Round: " + str(contextGame["round"]) + " of " + str(contextGame["maxRounds"]) + "\n")
        statsList = ["id", "name", "human", "type", "bank", "initial_card",
                     "priority", "bet", "points", "round_points", "cards"]

        # Utilizamos el dict players para que los jugadores derrotados tambien aparezcan
        userList = contextGame["players"]

        # Quisimos dividir la tabla en dos por eso las dos variables para guardar las strings
        top = ""
        bottom = ""

        # Para hacer una linea por stat iteramos sobre la statsList
        for stat in statsList:
            # Para printar una linea del stat actual para cada jugador iteramos sobre userList
            for i in range(len(userList)):
                # Este condicional lo utilizamos para hacer la division de la tabla,
                # en caso de que i sea mayor que dos (lo que significaria que ya ha guardado 3 users),
                # pasamos a guardar los datos en bottom
                if i < 3:
                    if stat == "id":
                        top += "Player: ".ljust(15) + userList[i].ljust(40)
                    elif stat == "round_points":
                        top += "Round points: ".ljust(15) + \
                               str(players[userList[i]][stat]).ljust(40)
                    elif stat == "initial_card":
                        top += "Initial card: ".ljust(15) + players[userList[i]][stat].ljust(40)
                    elif stat == "cards":
                        top += "Cards: " + str(players[userList[i]][stat]).ljust(48)
                    else:
                        top += "{}: ".format(stat).ljust(15) + \
                               str(players[userList[i]][stat]).ljust(40)

                else:
                    # Para guardar los datos de bottom iteramos desde i hasta el final de la lista,
                    # ya que i sera el cuarto jugador que es por el que queremos empezar.
                    # Al terminar de iterar hacemos un break para no volver a iterar sobre la i, y asi
                    # evitar datos replicados
                    for j in range(i, len(userList)):
                        if stat == "id":
                            bottom += "Player: ".ljust(15) + userList[j].ljust(40)
                        elif stat == "round_points":
                            bottom += "Round points: ".ljust(15) + \
                                      str(players[userList[j]][stat]).ljust(40)
                        elif stat == "initial_card":
                            bottom += "Initial card: ".ljust(15) + players[userList[j]][stat].ljust(40)
                        elif stat == "cards":
                            bottom += "Cards: " + str(players[userList[j]][stat]).ljust(48)
                        else:
                            bottom += "{}: ".format(stat).ljust(15) + \
                                      str(players[userList[j]][stat]).ljust(40)

                    bottom += "\n"
                    break

            top += "\n"

        print(top)
        print(bottom)

        input("Press enter to continue")

        removedPlayers = []
        # Apuntamos los jugadores que queremos eliminar
        for player in contextGame["players"]:
            if players[player]["points"] == 0:
                removedPlayers.append(player)

        # Eliminamos a los jugadores
        for player in removedPlayers:
            contextGame["players"].remove(player)

        # Miramos si tenemos que hacer cambio de banca con los candidatos a banca
        if len(bankCandidates) > 0:
            players[contextGame["bank"]]["bank"] = False
            players[bankCandidates[0]]["bank"] = True
            contextGame["bank"] = bankCandidates[0]

        # Si no hay candidatos a banca miramos si la banca no tiene puntos y la cambiamos por el siguiente
        # en la lista de prioridad.
        elif players[contextGame["bank"]]["points"] == 0:
            players[contextGame["bank"]]["bank"] = False
            players[contextGame["players"][len(contextGame["players"]) - 1]]["bank"] = True
            contextGame["bank"] = contextGame["players"][len(contextGame["players"]) - 1]

        # Ordenamos los jugadores por prioridad
        for pas in range(len(contextGame["players"]) - 1):
            # Variable para saber cuando esta ordenada la lista
            listIsOrdered = True
            for i in range(len(contextGame["players"]) - 1 - pas):

                # Este if es para que si el jugador es banca pase para delante
                if players[contextGame["players"][i]]["bank"]:
                    changeBox = contextGame["players"][i]
                    contextGame["players"][i] = contextGame["players"][i + 1]
                    contextGame["players"][i + 1] = changeBox
                    listIsOrdered = False

                # Este if es para pasar delante al jugador con mas prioridad a no ser que i + 1 sea bank
                if players[contextGame["players"][i]]["priority"] > players[contextGame["players"][i + 1]]["priority"]:
                    if not players[contextGame["players"][i + 1]]["bank"]:
                        changeBox = contextGame["players"][i]
                        contextGame["players"][i] = contextGame["players"][i + 1]
                        contextGame["players"][i + 1] = changeBox
                        listIsOrdered = False

            # Si la lista ya esta ordena se rompe el bucle
            if listIsOrdered:
                break

        # Al terminar la ronda le sumamos 1
        contextGame["round"] += 1
