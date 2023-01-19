# Imports
import pymysql
from datetime import *
from les_meves_funcions.datos import *
from les_meves_funcions.funcions_joc import *
import pymysql.cursors


# dicc = {"A": "KL", "B": "Kulo", "C": 3}
# prueba = "Select player_id from player"
# mysql4 = 'insert into countries (country_id, country_name, region_id) Values ("{}","{}",{})'.format(dicc["A"],dicc["B"],dicc["C"])

# Usando el modulo datetime (importado) pedimos la hora local actual
def Set_GameTime():
    hora_local = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return hora_local

def SelectBBDD(query):
    conn = pymysql.connect(
        host="sieteymedio2023.mysql.database.azure.com", port=3306,
        user="local", passwd="Los_Cactus_Pinchan1",
        charset='utf8mb4',
        db="sieteymedio"  # , cursorclass= pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()

    cursor.execute(query)
    resultado = cursor.fetchall()

    conn.close()
    return resultado


def InputBBDD(query):
    conn = pymysql.connect(
        host="sieteymedio2023.mysql.database.azure.com", port=3306,
        user="local", passwd="Los_Cactus_Pinchan1",
        charset='utf8mb4',
        db="sieteymedio"  # , cursorclass= pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()

    cursor.execute(query)
    conn.commit()

    conn.close()


#print(cursor.description[0][0])
#resultado = cursor.fetchall()
#print(resultado)
# resultado = SelectBBDD("Select player_id from player")
# exist_id = []
# for i in range(len(resultado)):
#     print(resultado[i][0])
#query = "'insert into player_game_round values ( "{}",{},"{}",{},{},{},{},{})'".format(cardgame_id,round_num,player_id,player_game_round[round_num][player_id]["is_bank"],player_game_round[round_num][player_id]["bet_points"] , player_game_round[round_num][player_id]["cards_value"],player_game_round[round_num][player_id]["starting_round_points"],player_game_round[round_num][player_id]["ending_round_points"])


def fetchPlayers(type="str"):
    humanList = []
    bootList = []

    fetch = SelectBBDD("select * from player")

    for user in fetch:
        user = list(user)
        if type == "str":
            if user[2] == 30:
                user[2] = "Cautious"
            if user[2] == 40:
                user[2] = "Moderated"
            if user[2] == 50:
                user[2] = "Bold"

        if user[3]:
            humanList.append(user)
        else:
            bootList.append(user)

    return humanList, bootList


def fetchCards(deck):
    cardsDict = {}

    fetch = SelectBBDD("select * from card where deck_id = '{}'".format(deck))
    for card in fetch:
        cardsDict[card[0]] = {"literal": card[1], "value": card[4], "priority": card[3], "realValue": card[2]}

    return cardsDict


def addDataToCardGame(moment):
    ultimoID = SelectBBDD("select max(cardgame_id) from cardgame")
    if moment == "beginning":
        cardgame[ultimoID + 1] = {"playersNum": len(contextGame["players"]),
                                  "startHour": Set_GameTime(), "deckID": contextGame["deck"]}
    else:
        cardgame[ultimoID + 1]["endHour"] = Set_GameTime()
        cardgame[ultimoID + 1]["totalRounds"] = contextGame["rounds"]


def addDataToPlayerGame(moment):
    ultimoID = SelectBBDD("select max(cardgame_id) from cardgame")
    if moment == "beginning":
        for player in contextGame["players"]:
            player_game[ultimoID + 1][player] = {"initial_card": players[player]["initial_card"],
                                                 "initial_points": players[player]["points"],
                                                 "final_points": 0}
    else:
        for player in contextGame["players"]:
            player_game[ultimoID + 1][player]["final_points"] = players[player]["points"]


def addDataToPlayerGameRound(moment):
    ultimoID = SelectBBDD("select max(cardgame_id) from cardgame")
    if moment == "beginning":
        player_game_round[ultimoID + 1] = {contextGame["round"]: {}}
        for player in contextGame["players"]:
            player_game_round[ultimoID + 1][contextGame["round"]][player] = {"bank": players[player]["bank"],
                                                                             "bet": players[player]["bet"],
                                                                             "initial_points": players[player]["points"]}
    else:
        for player in contextGame["players"]:
            player_game_round[ultimoID + 1][contextGame["round"]][player]["cards_value"] = players[player]["round_points"]
            player_game_round[ultimoID + 1][contextGame["round"]][player]["final_points"] = players[player]["points"]
