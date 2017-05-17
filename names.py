
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
import cmd

from docopt import docopt
from dojo import SpaceAllocation


