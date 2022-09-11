#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_0_usa:3 arguments:
mysql username, mysql password & database name (no argument validation needed
(import MySQLdb),connect to a MySQL server running on localhost at port 3306
sorted in ascending order by cities.id,code shouldnt be executed when imported
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    """
    Access to the database and get the cities
    from the database.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
            FROM cities LEFT JOIN states\
            ON states.id = cities.state_id\
            ORDER BY cities.id ASC")
    row = cur.fetchall()

    for row in rows:
        print(row)
