#!/usr/bin/python3
"""
script to be printed should only start with N(in caps only)
script that lists all states from the database hbtn_0e_0_usa:3 arguments:
mysql username, mysql password & database name (no argument validation needed
(import MySQLdb),connect to a MySQL server running on localhost at port 3306
sorted in ascending order by state,code shouldnt be executed when imported
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    """
    Access to the database and get the states
    from the database.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()

    filtered = []

    for state in states:
        if state startwith N:
            filtered.append(state)

    print(filtered)
