#!/usr/bin/python3
"""
script that takes in an argument & display all values in the states table where
name matches arg from the database hbtn_0e_0_usa:arguments(state name searched,
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
                         passwd=argv[2], db=argv[3], charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (argv[4],))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
