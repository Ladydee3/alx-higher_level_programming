#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
            user=sys.argv[1],
                            passwd=sys.argv[2],
db =sys.argv[3], port=330)
    cur = db.cursor()
    cur.exacute("""SELECT cities. id, cities.name, states.name FROM
    cities INNER JOIN states ON
 states.id=cities.states_id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        cur.close()
        db.close()
