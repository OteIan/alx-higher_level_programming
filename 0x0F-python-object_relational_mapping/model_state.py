#!/usr/bin/python3
"""
model_state module definition
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    State class represents a state

    Attributes:
    - id (int): The primary key representing the state's unique identifier
    - name(str): The name of the state
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=True, unique=True)
    name = Column(String(128), nullable=False)
