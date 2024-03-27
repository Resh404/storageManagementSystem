from storageManegementUILoops.main_UI_loop import UILoop
from storageManagementDatabase.main_database_creator import database_setup

''' This is the main script for the storage management system. database_setup prepares the database and
UILoop.main_loop runs the terminal which a user can interact with. '''

if __name__ == '__main__':
    # Need to have a MySQL local server running & edit the storageManagementDatabase -> connect_to_database.py
    # file to fit to your MySQL configration
    database_setup()

    # starts the user terminal
    UILoop.main_loop()