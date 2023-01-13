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
        else:
            if contextGame["deck"] == "baraja_esp":
                deck = ("baraja_esp", deck_esp_list)
            else:
                deck = ("baraja_poker", deck_pok_list)

        if contextGame["round"] < 5:
            contextGame["round"] = 5

    except ValueError as fail:
        print(fail)
        return False

    return True


# Funcion calculo de probabilidad de pasar 7 y medio
def probToPass(points, deckList, deckName):
    not_used_cards_list = []

    # For para guardar todas las cartas que quedan en el mazo en una variable
    for i in range(len(deckList)):
        if not deckList[i] in used_cards_list:
            not_used_cards_list.append(deckList[i])

    # Este count sirve para saber cuantas cartas hacen que te pases de 7 y medio
    count = 0
    for card in not_used_cards_list:
        if cartas[deckName][card]["realValue"] + points > 7.5:
            count += 1

    # Cuando ya tenemos todas las cartas que nos hacen pasarnos hacemos el calculo y lo devolvemos
    return (count * 100) // len(not_used_cards_list)


# Funcion para robar cartas
def drawCard(deckList):
    while True:
        # Se coje un numero aleatorio dentro de el rango de cartas que tenemos
        card = random.randint(0, len(deckList) - 1)
        # Miramos si la carta asignada a ese numero no esta en usedCardsList
        if not deckList[card] in used_cards_list:
            # Metemos la carta en la usedCardsList
            used_cards_list.append(deckList[card])
            # Hacemos un return con el nombre de la carta
            return deckList[card]


# Funcion loop de las rondas
def round_loop():
    used_cards_list = []


def checkMinimun2PlayerWithPoints():
    count = 0
    for player_id in contextGame["players"]:
        if players[player_id]["points"] > 0:
            count += 1

    if count < 2:
        return False

    else:
        return True
