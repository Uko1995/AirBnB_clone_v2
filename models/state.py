#!/usr/bin/python3
'''
    Implementation of the State class
'''
from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import models

class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        FLcity = models.storage.all("City").values()
        return [city for city in FLcity if city.state_id == self.id]
