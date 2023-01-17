# Imports
import pymysql
import pymysql.cursors


conn = pymysql.connect(
    host="localhost", port=3306,
    user="root", passwd="1234",
    db="hr"#, cursorclass= pymysql.cursors.DictCursor
)

cursor = conn.cursor()

cursor.execute(

)
