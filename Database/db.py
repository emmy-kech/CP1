
import os
import random

# from model import *
from tabulate import tabulate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import (Base,Employee,Room,OfficeAvailale,LivingSpacesAvailable)


engine= create_engine('sqlite:///amity.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind=engine)
session=DBSession()

Employee= open("input.txt", "r")
result = Employee.readline().strip()
output=[]
for i in result:
	output.append(Employee.readline().strip().split(' '))
sessiom.add(Employee)
session.commit()

newroom=Room(room_name='Bugundry',romm_type='Office')
session.add(newroom)
session.commit ()

# class Database:
#     def __init__(self,amity.db):
