#!/usr/bin/python3
"""
Module that connects to the database and querries it
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_state_objects(user, password, db):
    """
    Lists all state objects from the database hbtn_0e_6_usa

    Args:
    - user (str): MySQL username
    - password (str): MySQL password
    - db (str): MySQL database name
    """
    # Constructing the database URL
    url = f"mysql+mysqldb://{user}:{password}@localhost:3306/{db}"

    # Creating an SQLAlchemy engine
    engine = create_engine(url, pool_pre_ping=True)

    # Creating the database tables
    Base.metadata.create_all(engine)

    # Creating an SQLAlchemy session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying all state objects and printing their information
    states = session.query(State).order_by(State.id)
    for state in states:
        print(state.id, state.name, sep=": ")


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    list_state_objects(username, password, database)
