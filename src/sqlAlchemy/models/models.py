"""
    Models for ORM
"""
from sqlalchemy import Column, Integer, String, ForeignKey, \
    Float, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlAlchemy.models.base import Base

class City(Base):
    """
    Class to model for City Table ORM
    """
    __tablename__ = "city"
    __table_args__ = {"schema": "weather_data"}

    id = Column(Integer, primary_key = True)
    name = Column(String)
    admin_name = Column(String)
    long_lat = Column(String)
    children = relationship("Weather")

class Weather(Base):
    """
    Class to model for Weather Table ORM
    """
    __tablename__ = "weather"
    __table_args__ = {"schema": "weather_data"}

    record_id = Column(Integer, primary_key = True)
    city_id = Column(Integer, ForeignKey(City.id))
    time = Column(DateTime)
    temp_c = Column(Float)
    is_day = Column(Boolean)
    wind_kph = Column(Float)
    wind_degree = Column(Integer)
    precip_in = Column(Float)
    pressure_in = Column(Float)
    humidity = Column(Integer)
    cloud = Column(Integer)
    will_it_rain = Column(Integer)
    chance_of_rain = Column(Integer)
    will_it_snow = Column(Integer)
    chance_of_snow = Column(Integer)
