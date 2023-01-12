# Funcion de comprovaciones
from datos import *
def check_settings():
    if contextGame["players"] < 2:
        return print("Select 2 players or more to start the game!")

    elif contextGame["deck"] == "":
        return print("Select a card deck to start the game!")

    elif contextGame["round"] < 5:
        return print("Select 5 round or more!")

    else:
