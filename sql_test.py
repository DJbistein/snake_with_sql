import pymssql

def add_new_score(sqlline):
    server = "192.168.15.15\IT22"
    username = "sa"
    pw = "123QWEr"
    db = "db_jj_1im"

    conn = pymssql.connect(server, username, pw)
    conn.autocommit(True)
    usedb = f"USE {db}"
    cursor = conn.cursor()
    cursor.execute(usedb)
    cursor.execute(sqlline)

    conn.close()



name = "oter"
score = 999
sqlline = f"insert into snake_hs (score, playername) values ({score}, '{name}')"

add_new_score(sqlline)