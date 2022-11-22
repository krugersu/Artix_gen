
import json
import sqlite3
from datetime import datetime
from types import SimpleNamespace
from pathlib import Path  


pathDB = Path("data", "myDB.sqlite") 
all_db=sqlite3.connect(pathDB)

def testdb():

    pathJSON = Path("src", "st.json")     
    
# pass
    data = json.load(open(pathJSON,'r', encoding='utf-8'))
    ''' print(data.keys())
    for k in data:
        print(k) '''
    
    for key, value in recursive_items(data):
        print(key, value)
    
    
    jtopy=json.dumps(data) #json.dumps take a dictionary as input and returns a string as output.
    dict_json=json.loads(jtopy)


def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, value)
            yield from recursive_items(value)
        else:
            yield (key, value)