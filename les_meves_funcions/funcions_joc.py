# Imports
from datos import *
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


# Funcion calculo de probabilidad de pasar 7 y medio
def probToPass(points, deckName, deckList):
    # Este count sirve para saber cuantas cartas hacen que te pases de 7 y medio
    count = 0
    for card in deckList:
        if cartas[deckName][card]["realValue"] + points > 7.5:
            count += 1

    # Cuando ya tenemos todas las cartas que nos hacen pasarnos hacemos el calculo y lo devolvemos
    return (count * 100) / len(deckList)


# Funcion para robar cartas
def drawCard(deckList):
    while True:
        # Se coje un numero aleatorio dentro de el rango de cartas que tenemos
        card = random.randint(0, len(deckList) - 1)
        # Metemos la carta en la usedCardsList
        deckList.append(deckList[card])
        # Hacemos un return con el nombre de la carta
        return deckList[card]


# Funcion loop de las rondas
def round_loop():
    while True:
        # Se devuelven las cartas al mazo
        deck = list(cartas[contextGame["deck"]].keys())
        for player in contextGame["players"]:
            players[player]["cards"] = []
        used_cards_list = []

        for player in contextGame["players"]:
            if players[player]["bank"]:
                print()
            else:
                while players[player]["type"] <= probToPass(players[player]["round_points"], contextGame["deck"], deck):
                    card = drawCard(deck)
                    used_cards_list.append(card)
                    players[player]["cards"].append(card)
                    players[player]["round_points"] += cartas[contextGame["deck"]]["realValue"]

