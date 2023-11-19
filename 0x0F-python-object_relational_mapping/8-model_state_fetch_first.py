#!/usr/bin/python3
"""
Script that prints the first State object
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_state_object(user, password, database):
    """
    This lists the first State object from the database hbtn_0e_6_usa

    Args:
    - user (str): MySQL username
    - password (str): MySQL password
    - database (str): database name
    """
    url = f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}"

    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()
    if state:
        print(state.id, state.name, sep=":")
    else:
        print("Nothing")


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    list_state_object(username, password, database)
