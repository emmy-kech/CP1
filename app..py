

"""
    Commands:
        create_room <room_name>
        allocate_room_type <room_name> <room_type>
        add_person <firstname> <lastname> <e_type> <accomodation>
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
import sys

from docopt import docopt, DocoptExit
from pyfiglet import figlet_format
from termcolor import cprint
class Amity():
	def __init__(self):

	def app_exec(func):
	"""
	Decorator definition for the app.
	"""
	def fn(self, arg):
		try:
			opt = docopt(fn.__doc__, arg)
		except DocoptExit as e:
			msg = "Invalid command! See help."
			print(msg)
			print(e)
			return

		except SystemExit:
			return

		return func(self, opt)

	fn.__name__ = func.__name__
	fn.__doc__ = func.__doc__
	fn.__dict__.update(func.__dict__)

	return fn

def fetch data(self):
	f = open("input.txt", "r")
	result = f.readline().strip()

	output=[]
	for i in result:
		output.append(f.readline().strip().split(' '))
	f.close()
	print (output)

