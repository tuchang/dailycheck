from cliff.command import Command

#import json
import sqlite3

from io import StringIO
from cliff.show import ShowOne

class Remove(Command):
    "Remove a task"
    def get_parser(self, prog_name):
        parser = super(Remove, self).get_parser(prog_name)
        parser.add_argument('task_name')
        return parser
    def take_action(self, parsed_args):
#        with open('data/tasks.json','r+') as json_file:
#            tasks = json.loads(json_file.read()) 
#            json_file.close()
        # print(tasks)
#        tasks.pop(parsed_args.task_name, None) 
#        print(tasks)
#        json_str = json.dumps(tasks)
#        with open('data/tasks.json','w') as json_file:
#            json_file.write(json_str)    
#            json_file.close()
        conn = sqlite3.connect('data/daily.db')
        c = conn.cursor()
        c.execute("DELETE FROM tasks where task_name=\'%s\';" % parsed_args.task_name)
        conn.commit()
        conn.close()

