#!/usr/bin/python3
"""
Script that prints all City objects
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def print_city_objects(user, password, database):
    """
    Function that prints all the City objects from the hbtn_0e_14_usa dtaabase

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

    cities = session.query(City).order_by(City.id)

    for city in cities:
        state = session.query(State).filter_by(id=city.state_id).first()
        print(f"{state.name}: ({city.id}) {city.name}")


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    print_city_objects(username, password, database)
