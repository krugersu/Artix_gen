
import json
import sqlite3
from datetime import datetime
from types import SimpleNamespace
from pathlib import Path  


pathDB = Path("data", "myDB.sqlite") 
all_db=sqlite3.connect(pathDB)

def testdb(c_count):

    pathJSON = Path("src", "st.json")     
    
# pass
    #data = json.load(open(pathJSON,'r', encoding='utf-8'))
   # data = json.loads(c_count)
    data = c_count
    ''' print(data.keys())
    for k in data:
        print(k) '''
    
    ''' for key, value in recursive_items(data):
        print(key, value)
     '''
    recursive_items(data)
    jtopy=json.dumps(data) #json.dumps take a dictionary as input and returns a string as output.
    dict_json=json.loads(jtopy)


def recursive_itemsD(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
        
            yield (key, value)
            yield from recursive_items(value)
        else:
            yield (key, value)

 # ! Список словарей           
def recursive_items(dictionary):            
    for i in range(len(dictionary)-1):
       # print(i)
       # print(type(dictionary[i]))
        t = dictionary[i]
        print(dictionary[i])
        for key, value in recursive_itemsD(t):
            print(key, value)
        #recursive_itemsD(t)
        