#!/usr/bin/python3
"""
Script that lists the State objects containing 'a'
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_a_state_objects(user, password, database):
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

    states = session.query(State).filter(State.name.like("%a%"))

    for state in states.order_by(State.id):
        print(state.id, state.name, sep=":")


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    list_a_state_objects(username, password, database)
