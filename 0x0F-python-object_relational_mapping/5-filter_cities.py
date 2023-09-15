#!/usr/bin/python3
"""
This script lists all states from the database 'hbtn_0e_0_usa'.
Usage: ./script.py <username> <password> <database>
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    username, password, database = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %(name)s
    ORDER BY cities.id ASC
    """

    cur = db.cursor()
    cur.execute(query, {'name': argv[4]})
    res = cur.fetchall()

    print(", ".join([row[1]for row in res]))
