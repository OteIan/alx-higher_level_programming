#!/usr/bin/python3
"""
Script that adds State object to the database
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def add_state_object(user, password, database):
    """
    This adds the State object "Louisiana" to the database hbtn_0e_6_usa

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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    filtered_states = session.query(State).filter(State.name.like('Louisiana')).all()
    
    if filtered_states:
        for state in filtered_states:
            print(state.id)

    print(state.id)


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    add_state_object(username, password, database)
