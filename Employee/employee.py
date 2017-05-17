"""This shows inheritance from the parent class Person"""
class Person:
	def __init__(self,firstname, lastname, e_type,wants_accommodation):
		self.name= firstname + '' +lastname
		self.e_type=e_type
		self.wants_accommodation=wants_accommodation
class Staff(Person):
	def __init__(self,firstname,lastname,e_type,wants_accommodation):
		super(Staff,self).__init__(name,e_type="STAFF",wants_accommodation="N")

class Fellow(Person):
	def __init__(self,firstname,lastname,e_type,wants_accommodation):
		super(Fellow,self).__init__(name,firstname,lastname,e_type="FELLOW", wants_accommodation="Y" or "N")

