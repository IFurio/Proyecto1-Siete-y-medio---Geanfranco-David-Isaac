# Funcion de comprovaciones
from les_meves_funcions.datos import *
def check_settings():
    if len(contextGame["players"]) < 2:
        check = False
        return check, print("Select 2 players or more to start the game!")

    if contextGame["deck"] == "":
        check = False
        return check, print("Select a card deck to start the game!")

    if contextGame["round"] < 5:
        contextGame["round"] = 5

    check = True
    return check

