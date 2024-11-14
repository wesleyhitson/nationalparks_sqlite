import sqlite3

def main():
    con = sqlite3.connect("parks.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE if not exists parks(id primary key, name, year_founded, visited tinyint default 0)")

main()