
import random
import re

f = open("input.txt", "r")

output=[f.readline().strip().split(' ')]

class SpaceAllocation(object):
    def __init__(self):
        occupied_rooms=[]
        total_capacity = 10

    def add_person(self):
        try:
            offices=input("\n Create_room Office: ")
            print("An office called %s has been successfully created!" %(offices))
            livingspaces=input("\n Create_room  Living Space: ")
            print("A living space called %s has been successfully created!" %(livingspaces))
            staff_firstname= input("\n Add a Staff first name : ") 
            staff_fullname= input("\n Add a Staff full name: ")
            print("Staff %s has been successfully added. \n %s has been allocated the office %s" %(staff_fullname,staff_firstname,offices))
            fellow_firstname= input ("\n Add a Fellow first name: ")
            fellow_fullname= input ("\n Add a Fellow full name: ")
            wants_accomodation= ('Y','N')
            wants_accomodation = input ("\n Do you want accommodation? : ") 
            if wants_accomodation == 'Y':
                print("% s has been successfully added. \n %s has been allocated the office %s \n %s has been allocated the living space %s. " %(fellow_fullname,fellow_firstname,offices,fellow_firstname,livingspaces))
            elif wants_accomodation == 'N':
                print("% s has been successfully added. \n %s has been allocated the office %s ." % (fellow_fullname,fellow_firstname,offices))
            else:
                print(" Invalid Input.Enter either Y  or  N ") 
        except (RuntimeError, TypeError, NameError):
            pass
def main():
    my_class_instance=SpaceAllocation()
    my_class_instance.add_person()

    


if __name__ == '__main__':
    main()

