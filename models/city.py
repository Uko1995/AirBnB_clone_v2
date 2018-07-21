#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import Basemodel, Base
from models.state import State
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128),nullable=False)
