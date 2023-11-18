#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys


def list_specific_state(username, password, database, name_searched):
    """
    Displays all values in the states table where name matches the argument
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

    query1 = "SELECT * FROM states WHERE name "

    query2 = "LIKE BINARY '{}' ORDER BY id ASC".format(name_searched)

    query = query1 + query2

    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connect.close()


if __name__ == "__main__":
    username, password, database, name_searched = sys.argv[1:5]

    list_specific_state(username, password, database, name_searched)
