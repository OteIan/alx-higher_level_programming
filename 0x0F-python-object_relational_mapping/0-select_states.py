#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def list_states(username, password, database):
    """
    This function lists the states from a database
    """
    # Connection details
    host = 'localhost'
    port = 3306

    # Connection establishment
    connection = MySQLdb.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=database
            )

    # Create a cursor object
    cursor = connection.cursor()

    # Query
    query = "SELECT * FROM states ORDER BY id"

    # Execute the query
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    list_states(username, password, database)
