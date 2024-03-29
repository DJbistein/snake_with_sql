import pymssql
from sqlvar import server, username, pw, db

def get_highscore():
    conn = pymssql.connect(server, username, pw, db)
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute(f"USE {db}")
    sqlline = "SELECT * FROM snake_hs"

    score = conn.cursor(as_dict = True)
    score.execute(sqlline)

    for s in score:
        print(s)

    conn.close()

get_highscore()