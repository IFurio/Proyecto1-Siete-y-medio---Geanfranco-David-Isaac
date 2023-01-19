# Imports
import pymysql
import pymysql.cursors


# dicc = {"A": "KL", "B": "Kulo", "C": 3}
# prueba = "Select player_id from player"
# mysql4 = 'insert into countries (country_id, country_name, region_id) Values ("{}","{}",{})'.format(dicc["A"],dicc["B"],dicc["C"])


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


def fetchPlayers():
    humanList = []
    bootList = []

    fetch = SelectBBDD("select * from player")

    for user in fetch:
        user = list(user)
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
