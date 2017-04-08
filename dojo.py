
import random
import re

class SpaceAllocation(object):
    def __init__(self):
        self.offices=[]
        self.livingspaces=[]
        self.fellow_name=[]
        self.staff_name=[]
        # room=['offices','livingspaces']
        # office= ["zeus","lantern","megamind","archulis"]
        # livingspace=["thor","loki","hades","titans","cronus","pocahunters"]
        occupied_rooms=[]
        total_capacity = 10

    # def space_to_allocate(self):
    #     offices = input("\n Create an office room: ")
    #     livingspaces= input("\n Create a living space: ")
    #     return offices
    #     return livingspaces

    # def person(self):
    #     fellow_name= input("\n Enter Fellow name: ")
    #     staff_name= input("\n Enter Staff name: ")
    #     return fellow_name
    #     return staff_name

    def create_room(self,offices='',livingspaces='',occupied_rooms=[],total_capacity=10):
        rooms=['offices','livingspaces']
        offices=4
        livingspaces=6
        if len(occupied_rooms) <total_capacity:
            occupied_rooms += rooms
            return (occupied_rooms)
        elif offices<4:
            offices += staff_name
            offices += fellow_name
            return offices
        
        elif livingspaces< 6:
            livingspaces+=fellow_name
            return livingspaces
        else:
            if len(occupied_rooms) == total_capacity:
                return "All room spaces are occupied"
        #     print("The Dojo room does not exist")
        #     print("The person mentioned is not an employee!Try Again.")
    # def employees(self,fellow_name='',staff_name=''):
    #     fellow_name=self.person()
    #     staff_name=self.person()


def main():
    my_class_instance=SpaceAllocation()
    my_class_instance.create_room()

    


if __name__ == '__main__':
    main()

