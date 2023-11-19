#!/usr/bin/python3
"""
Script that updates State object
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def add_state_object(user, password, database):
    """
    This updates the name of a State object form the hbtn_0e_6_usa database

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

    state = session.query(State).filter_by(id=2).first()

    if state:
        state.name = "New Mexico"
        session.commit()


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    add_state_object(username, password, database)
