#!/usr/bin/python3
'''
    Implementation of the Review class
'''
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base

class Review(BaseModel, Base):
    '''
        Implementation for the Review.
    '''
    __tablename__ = "reviews"
    place_id = Column(String(60), nullable=False, ForeignKey('places.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    text = Column(String(1024), nullable=False)
