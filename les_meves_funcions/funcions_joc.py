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

        if contextGame["round"] < 5:
            contextGame["round"] = 5

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
        card = random.randint(0, len(deckList) - 1)
        # Quitamos la carta de la deck list
        deckList.remove(card)
        # Hacemos un return con el nombre de la carta
        return deckList[card]


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
    while checkMinimun2PlayerWithPoints() and contextGame["round"] <= contextGame["maxRounds"]:
        # Se devuelven las cartas al mazo y se ponen los puntos a cero
        deck = list(cartas[contextGame["deck"]].keys())
        for player in contextGame["players"]:
            players[player]["cards"] = []
            players[player]["round_points"] = 0

        # Loop para que cada jugador juegue su turno
        for player in contextGame["players"]:
            # En este IF juega la banca
            if players[player]["bank"]:
                while True:
                    count, points = playersWinningBank(player)
                    # Aqui comprovamos si la banca se quedara sin puntos o si todos los jugadores ganan a la banca
                    if count == len(contextGame["players"] - 1) or points >= players[player]["points"]:
                        card = drawCard(deck)
                        players[player]["cards"].append(card)
                        players[player]["round_points"] += cartas[contextGame["deck"]][card]["realValue"]
                    # Si la banca gana a todos los jugadores se planta
                    elif count == 0:
                        break
                    # En esta comparacion la banca pide como un jugador normal
                    elif players[player]["type"] <= probToPass(players[player]["round_points"],
                                                               contextGame["deck"], deck):
                        card = drawCard(deck)
                        players[player]["cards"].append(card)
                        players[player]["round_points"] += cartas[contextGame["deck"]][card]["realValue"]
                    else:
                        break

            # Aqui juegan el resto de jugadores
            else:
                while players[player]["type"] <= probToPass(players[player]["round_points"], contextGame["deck"], deck):
                    card = drawCard(deck)
                    players[player]["cards"].append(card)
                    players[player]["round_points"] += cartas[contextGame["deck"]][card]["realValue"]
