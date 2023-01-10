from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from app import app, db

Base = db.Model

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    phone_number = Column(String)
    password = Column(String)


class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    station_id = Column(Integer)
    status = Column(String)

class VehicleStation(Base):
    __tablename__ = 'vehicle_stations'
    id = Column(Integer, primary_key=True)
    location = Column(String)
