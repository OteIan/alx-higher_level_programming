#!/usr/bin/python3
"""
Script that prints given state object
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_given_state_object(user, password, database, name_searched):
    """
    This lists the first State object from the database hbtn_0e_6_usa

    Args:
    - user (str): MySQL username
    - password (str): MySQL password
    - database (str): database name
    - name_searched (str): name to be searched for in the database
    """
    url = f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}"

    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name.like(name_searched)).first()

    if state:
        print(state.id)
    else:
        print("Not found")


if __name__ == "__main__":
    username, password, database, name_searched = sys.argv[1:5]
    list_given_state_object(username, password, database, name_searched)
