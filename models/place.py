#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, Integer, ForeignKey
from sqlalchemy.orm import relationship
import models

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"), nullable=False),
                      Column("amenity_id", String(60), ForeignKey("amenities.id"),
                             nullable=False))
class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = "places"
    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False, back_populates("place_amenities"))
    @property
    def amenities(self):
        objlist=[]
        for amenity in self.amenity_ids:
            amenityObj = models.storage.all().get("Amenity.{}".format(amenity))
            if amenityObj:
                objlist.append(amenityObj)
        return objlist

    @amenities.setter(self, obj):
        if type(obj) is Amenity:
            self.amenity_ids.append(obj.id)
