# Imports
from les_meves_funcions.datos import *
import random


# Funcion de comprovaciones
def check_settings():
    try:
        if len(contextGame["players"]) < 2:
            raise ValueError("Select 2 players or more to start the game!")

        if contextGame["deck"] == "":
            raise ValueError("Select a card deck to start the game!")

        if contextGame["maxRounds"] < 5:
            contextGame["maxRounds"] = 5

    except ValueError as fail:
        print(fail)
        return False

    return True


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


# Funcion para robar cartas
def drawCard(deckList):
    while True:
        # Se coje un numero aleatorio dentro de el rango de cartas que tenemos
        card = deckList[random.randint(0, len(deckList) - 1)]
        # Quitamos la carta de la deck list
        deckList.remove(card)
        # Hacemos un return con el nombre de la carta
        return card


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
        if cartas[deckName][card]["realValue"] + points > 7.5:
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
    while checkMinimun2PlayerWithPoints() and contextGame["round"] < contextGame["maxRounds"]:
        # Se devuelven las cartas al mazo, se ponen los puntos a cero y se resetean los candidatos a la banca
        bankCandidates = []
        deck = list(cartas[contextGame["deck"]].keys())
        for player in contextGame["players"]:
            players[player]["cards"] = []
            players[player]["round_points"] = 0

        # Loop para que cada jugador juegue su turno
        for player in contextGame["players"]:
            # Aqui juegan los jugadores normales
            if not players[player]["bank"] and players[player]["points"] > 0:
                while players[player]["type"] >= probToPass(players[player]["round_points"], contextGame["deck"], deck):
                    card = drawCard(deck)
                    players[player]["cards"].append(card)
                    players[player]["round_points"] += cartas[contextGame["deck"]][card]["realValue"]
                # Este if se utiliza para que si te pasas de 7.5 tu apuesta sea negativa
                if players[player]["round_points"] > 7.5:
                    players[player]["round_points"] = -1

            # Aqui juega la banca y al terminar de pedir se reparten los puntos
            else:
                while True:
                    # Guardamos en count la cantidad de jugadores que nos superan y en points los puntos que pagaremos
                    count, points = playersWinningBank(player)
                    # Aqui comprovamos si la banca se quedara sin puntos o si todos los jugadores ganan a la banca
                    if count == len(contextGame["players"]) - 1 or points >= players[player]["points"]:
                        card = drawCard(deck)
                        players[player]["cards"].append(card)
                        players[player]["round_points"] += cartas[contextGame["deck"]][card]["realValue"]
                    # Si la banca gana a todos los jugadores se planta
                    elif count == 0:
                        break
                    # En esta comparacion la banca pide como un jugador normal
                    elif players[player]["type"] >= \
                            probToPass(players[player]["round_points"], contextGame["deck"], deck):
                        card = drawCard(deck)
                        players[player]["cards"].append(card)
                        players[player]["round_points"] += cartas[contextGame["deck"]][card]["realValue"]
                    else:
                        break

                # Este if se utiliza para que si te pasas de 7.5 tu apuesta sea negativa
                if players[player]["round_points"] > 7.5:
                    players[player]["round_points"] = -1

                # Utilizamos esta variable para repartir los puntos en orden de prioridad y se apuntan candidatos a bank
                pointsDistribution(player, bankCandidates)

                # ¡¡¡REVISAR!!!
                # Miramos si tenemos que hacer cambio de banca
                if len(bankCandidates) > 0:
                    players[player]["bank"] = False
                    players[bankCandidates[len(bankCandidates) - 1]]["bank"] = True

                elif players[player]["points"] == 0:
                    players[player]["bank"] = False
                    players[contextGame["players"][len(contextGame) - 2]]["bank"] = True

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
