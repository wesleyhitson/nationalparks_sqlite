import sqlite3
import json
import csv

def main():
    with open("parks.csv", "w", newline="", encoding="UTF-8") as csvfile:
        writer = csv.writer(csvfile, dialect="excel")

        with open("parks.json", "r", encoding="UTF-8") as f:
            data = json.load(f)

            for p in data["data"]:
                row = []
                row.append(p["name"])
                row.append(p["parkCode"])
                row.append(p["designation"])
                row.append(p["states"])
                row.append(p["latitude"])
                row.append(p["longitude"])
                writer.writerow(row)

    # con = sqlite3.connect("parks.db")
    # cur = con.cursor()

    # cur.execute("CREATE TABLE if not exists parks(id primary key, name, year_founded, visited tinyint default 0)")

main()