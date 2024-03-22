from storageManegementUILoops.main_UI_loop import UILoop
from storageManagementDatabase.main_database_creator import database_setup

''' This is the main script for the storage management system. database_setup prepares the database and
UILoop.main_loop runs the terminal which a user can interact with. '''

if __name__ == '__main__':
    # database_setup()
    UILoop.main_loop()
