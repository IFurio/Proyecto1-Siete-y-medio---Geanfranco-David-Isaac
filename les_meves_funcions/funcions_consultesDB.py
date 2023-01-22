# Imports
import pymysql
from datetime import *
from les_meves_funcions.datos import *
import pymysql.cursors


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


def fetchPlayers(ret="str"):
    humanList = []
    bootList = []

    fetch = SelectBBDD("select * from player")

    for user in fetch:
        user = list(user)
        if ret == "str":
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
    hora_local = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if moment == "beginning":
        player_game[0] = {}
        player_game_round[0] = {}
        cardgame[0] = {"players_num": len(contextGame["players"]),
                       "start_hour": hora_local, "deck_id": contextGame["deck"]}

    elif moment == "final":
        cardgame[0]["end_hour"] = hora_local
        cardgame[0]["total_rounds"] = contextGame["round"]

    elif moment == "insert":
        InputBBDD(
            "insert into cardgame ( players, rounds, start_hour, end_hour, deck_id )"
            "values ( {}, {}, '{}', '{}', '{}' )".format(cardgame[0]["players_num"],
                                                         cardgame[0]["total_rounds"],
                                                         cardgame[0]["start_hour"],
                                                         cardgame[0]["end_hour"],
                                                         cardgame[0]["deck_id"]))


def addDataToPlayerGame(moment):

    if moment == "beginning":
        for player in contextGame["players"]:
            player_game[0][player] = {"initial_card": players[player]["initial_card"],
                                      "initial_points": players[player]["points"],
                                      "final_points": 0}
    elif moment == "final":
        for player in contextGame["players"]:
            player_game[0][player]["final_points"] = players[player]["points"]

    elif moment == "insert":
        ultimoID = SelectBBDD("select max(cardgame_id) from cardgame")
        ultimoID = ultimoID[0][0]
        for player in player_game[0].keys():
            InputBBDD(
                "insert into player_game "
                "values ( {}, '{}', '{}', {}, {} )".format(ultimoID,
                                                           player,
                                                           player_game[0][player]["initial_card"],
                                                           player_game[0][player]["initial_points"],
                                                           player_game[0][player]["final_points"],))


def addDataToPlayerGameRound(moment):

    if moment == "beginning":
        player_game_round[0][contextGame["round"]] = {}
        for player in contextGame["players"]:
            player_game_round[0][contextGame["round"]][player] = {"bank": players[player]["bank"],
                                                                  "bet": players[player]["bet"],
                                                                  "initial_points": players[player]["points"]}
    elif moment == "final":
        for player in contextGame["players"]:
            player_game_round[0][contextGame["round"]][player]["cards_value"] = players[player]["round_points"]
            player_game_round[0][contextGame["round"]][player]["final_points"] = players[player]["points"]

    elif moment == "insert":
        ultimoID = SelectBBDD("select max(cardgame_id) from cardgame")
        ultimoID = ultimoID[0][0]
        for round in player_game_round[0].keys():
            for player in player_game_round[0][round].keys():
                InputBBDD(
                    "insert into player_game_round "
                    "values ( {}, {}, '{}', {}, {}, {}, {}, {} )".format(ultimoID,
                                                                         round,
                                                                         player,
                                                                         player_game_round[0][round][player]["bank"],
                                                                         player_game_round[0][round][player]["bet"],
                                                                         player_game_round[0][round][player]["cards_value"],
                                                                         player_game_round[0][round][player]["initial_points"],
                                                                         player_game_round[0][round][player]["final_points"])
                )
