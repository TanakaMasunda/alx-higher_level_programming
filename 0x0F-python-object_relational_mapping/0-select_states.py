#!/usr/bin/python3

"""
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
            sswd=argv[2], db=argv[3])
    
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
