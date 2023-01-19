# Imports
from les_meves_funcions.funcions_menu import *
from les_meves_funcions.datos import *
import random


# Funcion de comprovaciones
def check_settings():
    try:
        if len(contextGame["players"]) < 2:
            raise ValueError("Select 2 players or more to start the game!")

        if contextGame["deck"] == "":
            raise ValueError("Select a card deck to start the game!")
        else:
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


# Funcion para ordenar jugadores
def orderPlayers(deck):
    for pas in range(len(contextGame["players"]) - 1):
        # Esta variable sirve para no tener que hacer comprovaciones de mas
        listIsOrdered = True
        for i in range(len(contextGame["players"]) - 1 - pas):
            # Aqui se comprueba si la carta inicial del jugador i es mas alta que la de i + 1 y se cambia de puesto,
            # tambien se comprueba si el jugador i + 1 es banca para no hacer el cambio en ese caso
            if contextGame["deck"][players[contextGame["players"][i]]["initial_card"]]["value"] > contextGame["deck"][players[contextGame["players"][i + 1]]["initial_card"]]["value"]:
                changeBox = contextGame["players"][i]
                contextGame["players"][i] = contextGame["players"][i + 1]
                contextGame["players"][i + 1] = changeBox
                listIsOrdered = False

            # Si los dos jugadores sacan la misma cifra se comprueban prioridades, tambien se vuelve a comprobar si
            # i + 1 es banca para no hacer el cambio.
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
    # Definimos la hora de inicio
    Set_GameTime()
    # Definimos la prioridad de los jugadores
    SetPriority()
    return


# Poner los puntos de inicio a cada jugador (20)
def Set_InitialPoints():
    # Accedemos a la lista de jugadores que van a participar en la partida y les ponemos los puntos iterando en la lista.
    for player in contextGame["players"]:
        players[player]["points"] = 20
    return


# Definir la prioridad de cada jugador antes de comenzar la partiad.
def SetPriority():
    deck = list(contextGame["deck"].keys())
    for player in contextGame["players"]:
        players[player]["initial_card"] = drawCard(deck)
    orderPlayers(contextGame["deck"])
    players[contextGame["players"][-1]]["bank"] = True
    contextGame["bank"] = contextGame["players"][-1]
    return


# Funcion para comprabarsi tiene que terminar la partida
def checkMinimun2PlayerWithPoints():
    count = 0
    for player_id in contextGame["players"]:
        if players[player_id]["points"] > 0:
            count += 1

    if count < 2:
        return False

    else:
        return True


# Funcion para apuestas
def setPlayersBet(bank):
    for player in contextGame["players"]:
        # Si el jugador no es banca se hacen apuestas
        if player != bank:

            # Si el jugador es humano se le pregunta si quiere apostar a mano o automaticamente
            if players[player]["human"]:
                opt = getOpt("Elige tu apuesta " + player + ":", "\n1)Automatica\n2)Manual", "Option:\n", [1, 2], {}, [])

                # Modo automatico
                if opt == 1:
                    bet = (players[player]["type"] * players[player]["points"]) // 100
                    if bet > players[bank]["points"]:
                        bet = players[bank]["points"]
                        players[player]["bet"] = bet
                    else:
                        players[player]["bet"] = bet

                # Modo manual
                else:
                    while True:
                        print("Select your bet " + player + ":")
                        bet = input("Bet: \n")
                        if not bet.isdigit():
                            print("¡¡¡¡ERROR!!!!")
                        elif int(bet) > players[player]["points"]:
                            print("¡¡¡¡ERROR!!!!")
                        elif int(bet) > players[bank]["points"]:
                            print("¡¡¡¡ERROR!!!!")
                        else:
                            players[player]["bet"] = int(bet)
                            break

            # A los boots se les apuesta automaticamente
            else:
                bet = (players[player]["type"] * players[player]["points"]) // 100
                if bet > players[bank]["points"]:
                    bet = players[bank]["points"]
                    players[player]["bet"] = bet
                else:
                    players[player]["bet"] = bet


# Funcion para pagar y cobrar apuestas y guardar los candidatos a banca
def pointsDistribution(bank, candidates):
    for i in range(len(contextGame["players"]) - 2, -1, -1):
        # En este if se entra si la banca le a ganado la ronda a este jugador
        if players[contextGame["players"][i]]["round_points"] <= players[bank]["round_points"]:
            players[contextGame["players"][i]]["points"] -= players[contextGame["players"][i]]["bet"]
            players[bank]["points"] += players[contextGame["players"][i]]["bet"]

        # En este else se entre si el jugador gana la ronda a la banca
        else:
            # If para saber si el jugador a sacado 7.5 y por lo tanto hay que pagarle doble
            if players[contextGame["players"][i]]["round_points"] == 7.5:
                candidates.append(contextGame["players"][i])
                if players[contextGame["players"][i]]["bet"] * 2 > players[bank]["points"]:
                    players[contextGame["players"][i]]["points"] += players[bank]["points"]
                    players[bank]["points"] = 0
                    break
                else:
                    players[contextGame["players"][i]]["points"] += (players[contextGame["players"][i]]["bet"] * 2)
                    players[bank]["points"] -= (players[contextGame["players"][i]]["bet"] * 2)

            # Aqui entra para pagar normal
            else:
                if players[contextGame["players"][i]]["bet"] > players[bank]["points"]:
                    players[contextGame["players"][i]]["points"] += players[bank]["points"]
                    players[bank]["points"] = 0
                    break
                else:
                    players[contextGame["players"][i]]["points"] += players[contextGame["players"][i]]["bet"]
                    players[bank]["points"] -= players[contextGame["players"][i]]["bet"]


# Funcion calculo de probabilidad de pasar 7 y medio
def probToPass(points, deckName, deckList):
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
    while checkMinimun2PlayerInGame() and contextGame["round"] <= contextGame["maxRounds"]:
        # Se devuelven las cartas al mazo, se ponen los puntos a cero y se resetean los candidatos a la banca
        bankCandidates = []
        for player in contextGame["players"]:
            players[player]["cards"] = []
            players[player]["round_points"] = 0
        deck = list(contextGame["deck"].keys())
        addDataToPlayerGameRound("beginning")

        # Se hacen las apuestas
        setPlayersBet(contextGame["bank"])

        # Loop para que cada jugador juegue su turno
        for player in contextGame["players"]:
            card = drawCard(deck)
            players[player]["cards"].append(card)
            players[player]["round_points"] += contextGame["deck"][card]["realValue"]
            # Aqui juegan los jugadores normales
            if not players[player]["bank"]:
                while players[player]["type"] >= probToPass(players[player]["round_points"], contextGame["deck"], deck):
                    card = drawCard(deck)
                    players[player]["cards"].append(card)
                    players[player]["round_points"] += contextGame["deck"][card]["realValue"]

                # Este if se utiliza para que si te pasas de 7.5 tu apuesta sea negativa
                if players[player]["round_points"] > 7.5:
                    players[player]["round_points"] = -1

            # Aqui juega la banca y al terminar de pedir se reparten los puntos, se cambia de banca y se ordenan players
            else:
                while True:
                    # Guardamos en count la cantidad de jugadores que nos superan y en points los puntos que pagaremos
                    count, points = playersWinningBank(player)

                    # Si la banca gana a todos los jugadores se planta
                    if count == 0:
                        break

                    # En esta comparacion la banca pide como un jugador normal
                    elif players[player]["type"] >= probToPass(players[player]["round_points"], contextGame["deck"], deck):
                        card = drawCard(deck)
                        players[player]["cards"].append(card)
                        players[player]["round_points"] += contextGame["deck"][card]["realValue"]

                    # Aqui comprovamos si la banca se quedara sin puntos o si todos los jugadores ganan a la banca
                    elif count == len(contextGame["players"]) - 1 or points >= players[player]["points"]:
                        card = drawCard(deck)
                        players[player]["cards"].append(card)
                        players[player]["round_points"] += contextGame["deck"][card]["realValue"]

                    # En caso de que su nivel de resiesgo se pase se planta
                    else:
                        break

                # Este if se utiliza para que si te pasas de 7.5 tu apuesta sea negativa
                if players[player]["round_points"] > 7.5:
                    players[player]["round_points"] = -1

        # Utilizamos esta variable para repartir los puntos en orden de prioridad y se apuntan candidatos a bank
        pointsDistribution(contextGame["bank"], bankCandidates)

        # Hueco para insert de ronda
        addDataToPlayerGameRound("")

        # Prints para hacer pruebas de funcionamiento
        print("Ronda: " + str(contextGame["round"]) + "\n")
        for player in contextGame["players"]:
            print(player + " " + str(players[player]["bank"]) + ":")
            print("Cartas en mano:", players[player]["cards"])
            print("Bet: " + str(players[player]["bet"]))
            print("Round points: " + str(players[player]["round_points"]))
            print("Player points: " + str(players[player]["points"]))
            print("ProbToPass: " + str(probToPass(players[player]["round_points"], contextGame["deck"], deck)) + "\n")
        input("Pulsa la intro")
        contextGame["round"] += 1

        # Eliminamos jugadores sin puntos
        for player in contextGame["players"]:
            if players[player]["points"] == 0:
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

        # Ordenamos los jugadores
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
