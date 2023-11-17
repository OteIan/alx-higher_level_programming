#!/usr/bin/python3
import MySQLdb
import sys
"""
Script that lists all states from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    # Retrieve MySQL credentials from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost"
            port=3306
            user=mysql_username
            passwd=mysql_password
            db=database_name
            )
    cursor = db.cursor()

    # Execute the SQL query
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
