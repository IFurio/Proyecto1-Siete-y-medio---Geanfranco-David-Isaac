# Imports
import pymysql
import pymysql.cursors


conn = pymysql.connect(
    host="sieteymedio2023.mysql.database.azure.com", port=3306,
    user="local", passwd="Los_Cactus_Pinchan1",
    charset='utf8mb4',
    db="sieteymedio"#, cursorclass= pymysql.cursors.DictCursor
)
cursor = conn.cursor()

# dicc = {"A": "KL", "B": "Kulo", "C": 3}
# prueba = "Select player_id from player"
# mysql4 = 'insert into countries (country_id, country_name, region_id) Values ("{}","{}",{})'.format(dicc["A"],dicc["B"],dicc["C"])

def SelectBBDD(query):
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado
def InputBBDD(query):
    cursor.execute(query)
    conn.commit()
    return

#print(cursor.description[0][0])
#resultado = cursor.fetchall()
#print(resultado)
# resultado = SelectBBDD("Select player_id from player")
# exist_id = []
# for i in range(len(resultado)):
#     print(resultado[i][0])
#query = "'insert into player_game_round values ( "{}",{},"{}",{},{},{},{},{})'".format(cardgame_id,round_num,player_id,player_game_round[round_num][player_id]["is_bank"],player_game_round[round_num][player_id]["bet_points"] , player_game_round[round_num][player_id]["cards_value"],player_game_round[round_num][player_id]["starting_round_points"],player_game_round[round_num][player_id]["ending_round_points"])