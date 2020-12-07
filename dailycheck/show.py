import logging
import os

from cliff.lister import Lister
import json
from io import StringIO
import sqlite3

class Show(Lister):
    "Show details about a task"

    log = logging.getLogger(__name__)

#    print(os.path.abspath('.'))
#    with open('data/tasks.json', 'r') as tasks_file:
#        tasks_json = json.loads(tasks_file.read())
#        tasks_file.close()
	
    def take_action(self, parsed_args):
 
#        with open('data/tasks.json', 'r') as tasks_file:
#            tasks_json = json.loads(tasks_file.read())
#            tasks_file.close()
        conn = sqlite3.connect('data/daily.db')
        c = conn.cursor()
        c.execute("SELECT * FROM tasks;")
        result = c.fetchall()
        #result = c.fetchone()
        #print(result)
        #print(c.description)
        columns  = list(map(lambda x: x[0], c.description))
        

        data = tuple((task[0],task[1],task[2]) for task in result)
        return (columns, data)
