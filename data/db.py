import sqlite3 as sql



def create_bd():
    with sql.connect("data/dictionary.sqlite3") as con:
        cur = con.cursor()

        cur.execute(""" CREATE TABLE IF NOT EXISTS slovar(
            id INTEGER,
            rus TEXT,
            eng TEXT);
            """)

        cur.execute(""" CREATE TABLE IF NOT EXISTS users(
            user_id TEXT,
            lang TEXT);
                    """)


        con.commit()


def get_text(id, language):
    with sql.connect("data/dictionary.sqlite3") as bd:
        cur = bd.cursor()

        res = cur.execute("""SELECT rus, eng FROM slovar WHERE id == ?""", (id,))
        if language == "ru":
            return list(res)[0][0]
        elif language == "en":
            return list(res)[0][1]


def add_result(id, rus, eng):
    with sql.connect("data/dictionary.sqlite3") as bd:
        cr = bd.cursor()

    cr.execute("""INSERT INTO slovar VALUES (?, ?, ?)""",
               (id, rus, eng))

    bd.commit()
