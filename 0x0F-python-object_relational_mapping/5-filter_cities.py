#!/usr/bin/python3
"""
Lists all cities of a given state
"""
import MySQLdb
import sys


def list_cities(username, password, database, state_name):
    """
    Takes in the name of a state as an argument and lists all cities of that
    state using the database hbtn_0e_4_usa
    """
    host = "localhost"
    port = 3306

    connect = MySQLdb.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=database
            )

    cursor = connect.cursor()

    query1 = "SELECT name FROM cities WHERE state_id IN "
    query2 = "(SELECT id FROM states WHERE name LIKE BINARY %s) "
    query3 = "ORDER BY id ASC"

    query = query1 + query2 + query3

    cursor.execute(query, (state_name + '%',))

    i = 0
    for row in cursor.fetchall():
        if i > 0:
            print(", ", end="")
        print(f"{row[0]}", end="")
        i += 1
    print()

    cursor.close()
    connect.close()


if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:5]
    list_cities(username, password, database, state_name)
