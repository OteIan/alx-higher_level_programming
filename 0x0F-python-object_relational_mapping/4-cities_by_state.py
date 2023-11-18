#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def list_cities(username, password, database):
    """
    Lists all cities from the database hbtn_0e_4_usa
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

    query1 = "SELECT cities.id, cities.name, states.name "
    query2 = "FROM cities "
    query3 = "JOIN states ON cities.state_id = states.id "
    query4 = "ORDER BY id ASC"

    query = query1 + query2 + query3 + query4

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connect.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    list_cities(username, password, database)
