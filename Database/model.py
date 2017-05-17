
import os
import sys 
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table,Column,Integer, String
from sqlalchemy.orm import relationship,sessionmaker

Base=declarative_base() #creating the base class

class Employee(Base):
    """Create Employee class """
    __tablename__='employee' #defining columns from table employee
    id = Column(Integer,primary_key=True,autoincrement=True)
    firstname = Column(String,unique=True)
    lastname = Column (String, unique=True)
    employee_type= Column (String)
    accommodation=Column(String(30))

class Room(Base):
    """ Creat Room class"""
    __tablename__='room'
    id=Column(Integer,primary_key=True,autoincrement=True)
    room_name=Column(String(30),nullable=False)
    room_type=Column(String(30),nullable=False)
    total_members=Column(Integer,nullable=False)

class OfficeAvailable(Base):
    """Create OfficeAvailable class"""
    __tablename__='office_available'
    id=Column(Integer,primary_key=True,autoincrement=True)
    room_name=Column(String(30),nullable=False)
    occupants=Column(String(30))

class LivingSpacesAvailable(Base):
    """Create LivingSpaceAvailable class"""
    __tablename__='livingspace_available'
    id = Column(Integer,primary_key=True,autoincrement=True)
    room_name=Column(String(30),nullable=False)
    occupants=Column(String(30))

""" """
engine=create_engine('sqlite:///amity.db')
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
    # def create_db(self,db_name=None):
    #     if db_name:
    #         self.db_name=db_name
    # # Create an engine that stores data in the local directory's
    #     self.engine = create_engine('sqlite:///' + db_name, echo=True)
    # # Create tables in database
    #     self.Base.metadata.create_all(self.engine)
    #     self.sessionmaker(bind=self.engine)
