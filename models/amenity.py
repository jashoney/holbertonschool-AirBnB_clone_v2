#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import place_amenity
import OS


class Amenity(BaseModel, Base):
    """Amenities of the place to stay"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenities = relationship('Place', secondary=place_amenity)
