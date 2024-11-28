import sqlite3
import json
import csv

def main():
    # part 1, read the json file and generate csv
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


    # part 2, load csv data into the database
    # written in a way that part 1 is optional, as
    # long as the csv exists in the correct format
    con = sqlite3.connect("parks.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS parks")
    cur.execute("""CREATE TABLE IF NOT EXISTS parks(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                name, parkCode, designation, states, latitude, longitude, 
                visited TINYINE DEFAULT 0)""")
    
    # read csv and insert
    data = []
    with open("parks.csv", "r", encoding="UTF-8") as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

    cur.executemany("""INSERT INTO parks 
                        (name, parkCode, designation, states, latitude, longitude) 
                    VALUES (?, ?, ?, ?, ?, ?)""", 
                    data)
    con.commit()

    res = cur.execute("SELECT * FROM parks")
    for r in res:
        print(r)

main()