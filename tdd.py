"""
    Commands:
        create_room <room_name>
        allocate_room_type <room_name> <room_type>
        add_person <first_name> <last_name> <job_type> <accomodation>
        reallocate_person <person_id> <room_name>
        load_people <filename>
        print_allocations [--o=filename]
        print_unallocated [--o=filename]
        print_room <room_name>
        save_state [--db=sqlitedb]
        load_state <sqlite_db>
        quit
    Options:
        -h, --help  Show this screen and exit
        -o filename  Specify filename
        --db  Name of SQLite DB
        --accomodation - prompt on whether one wants or doesn't want accomodation [default='N']
"""
# from docopt import docopt
# import cmd

import unittest
from dojo import SpaceAllocation 
# docopt(doc, argv=None, help=True, version=None, options_first=False)

class TestCreateRoom(unittest.TestCase):

    def test_create_room_successfully(self):
        my_class_instance=SpaceAllocation()
        initial_room_count=len(my_class_instance.create_room())
        zeus_office=my_class_instance.create_room("zeus","office")
        self.assertTrue(zeus_office)
        new_room_count = len(my_class_instance.create_room())
        self.assertEqual(new_room_count - initial_room_count,1)
        loki_livingspace=my_class_instance.create_room("loki","livingspace")
        self.assertTrue(loki_livingspace)
        self.assertEqual(new_room_count - initial_room_count,2)

    def allocate_person_room(self):
        my_class_instance=SpaceAllocation()
        andela_employees=my_class_instance.add_person("fellow","staff")




    
if __name__ == '__main__':
    unittest.main()