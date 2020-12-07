from cliff.command import Command

import json
from io import StringIO
from cliff.show import ShowOne
import sqlite3

class Add(Command):
    "Add a task"
    def get_parser(self, prog_name):
        parser = super(Add, self).get_parser(prog_name)
        parser.add_argument('task_name')
        return parser
    def take_action(self, parsed_args):
        #with open('data/tasks.json','r+') as json_file:
        #    tasks = json.loads(json_file.read()) 
        #    json_file.close()
        # print(tasks)
        # tasks[parsed_args.task_name] = 0 
        # print(tasks)
        # json_str = json.dumps(tasks)
#        with open('data/tasks.json','w') as json_file:
#            json_file.write(json_str)    
#            json_file.close()
        conn = sqlite3.connect('data/daily.db')
        c = conn.cursor()
#        print('''
#              INSERT INTO tasks(\'tasks_name\', create_date) VALUES(%s,date(\'now\'));
#              ''' % parsed_args.task_name)
        c.execute('''
                  INSERT INTO tasks (\'task_name\', create_date) 
                  VALUES(\'%s\',date(\'now\'));
                  ''' % parsed_args.task_name
        ) 
        conn.commit()
        conn.close()
