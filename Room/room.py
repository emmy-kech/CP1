class Room:
	def __init__(self,room_name,room_type,capacity):
		self.room_name=room_name
		self.room_type=room_type
		self.capacity= capacity

class Office(Room):
	def __init__(self,room_name,room_type,capacity):
		super(Office,self).__init__(room_name,room_type="OFFICE",capacity=6)
		

class LivingSpace(Room):
	def __init__(self,room_name,room_type,capacity):
		super(LivingSpace,self).__init__(room_name,room_type="LIVINGSPACE",capacity=4)