#!/usr/bin/python3
"""
model_city module definition
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class represents a city

    Attr
    - id (int): Primary key representing the city's unique identifier
    - name (str): The name of the city
    - state_id (int): Foreign key representing the id of the city's state
    """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'), nullable=False)
