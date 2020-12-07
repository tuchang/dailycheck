import sqlite3
from cliff.command import Command

class Init(Command):
    "Initialize the database"
    def take_action(self, parsed_args):
        conn = sqlite3.connect('data/daily.db')

        c = conn.cursor()
        c.execute(''' CREATE TABLE IF NOT EXISTS 
                  tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, task_name TEXT NOT NULL, create_date TEXT NOT NULL);
          ''')
        c.execute(''' CREATE TABLE IF NOT EXISTS
          checks(id INTEGER PRIMARY KEY AUTOINCREMENT, task_id NOT NULL, check_time TEXT NOT NULL);
          ''')
        
