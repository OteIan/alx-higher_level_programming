#!/usr/bin/python3
"""
Script that lists all states with a name starting with N
"""
import MySQLdb
import sys


def list_states(username, password, database):
    """
    This function lists all states with a name starting with N
    """
    host = 'localhost'
    port = 3306

    connect = MySQLdb.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=database
            )

    cursor = connect.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%';"

    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connect.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    list_states(username, password, database)
