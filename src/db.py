
import json
import sqlite3
from datetime import datetime
from types import SimpleNamespace
from pathlib import Path  
import query

pathDB = Path("data", "myDB.sqlite") 
pathSqript = Path("data", "createDB.sql") 
all_db=sqlite3.connect(pathDB)
baseTableName = 'invent'


def saveDataDB(c_count):

    data = c_count

    createDB()
    recursive_items(data)
'''     jtopy=json.dumps(data) #json.dumps take a dictionary as input and returns a string as output.
    dict_json=json.loads(jtopy)
 '''

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
        addRecord(dictionary[i])
        ''' t = dictionary[i]
        print(dictionary[i])
        for key, value in recursive_itemsD(t):
            print(key, value) '''
        #recursive_itemsD(t)
        
        
        
def addRecord(item_position):
    
    ''' for key, value in item_position.items():
        if isinstance(value, dict):   
            pass
        else '''
    curVal =[]
    curVal.append(None) 
    curVal.append(int(item_position['options']['priceoptions']['enablepricemanual'])) 
    curVal.append(int(item_position['options']['priceoptions']['requirepricemanual'])) 
    curVal.append(int(item_position['options']['priceoptions']['requireselectprice'])) 
    curVal.append(int(item_position['options']['priceoptions']['requiredeferredprice'])) 
    curVal.append(int(item_position['options']['priceoptions']['enableexcisemarkprice'])) 
    
    
    cur = all_db.cursor()
    cur.execute(query.qrAddPriceoptions,curVal)
    all_db.commit() 

    curVal.clear()
    curVal.append(None) 
    curVal.append(int(item_position['options']['inventitemoptions']['disablebackinsale'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['disableinventshow'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['disableinventsale'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['disableinventback'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['requiredepartmentmanual']))     
    curVal.append(int(item_position['options']['inventitemoptions']['enabledepartmentmanual'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['enablebarcodemanual'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['enablebarcodescanner'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['visualverify'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['ageverify']))     
    curVal.append(int(item_position['options']['inventitemoptions']['requiresalerestrict'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['egaisverify'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['prepackaged'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['nopdfegaisverify'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['alcoset']))     
    curVal.append(int(item_position['options']['inventitemoptions']['freesale'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['rfidverify'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['lowweight'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['weightcontrolbypass'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['tobacco']))     
    curVal.append(int(item_position['options']['inventitemoptions']['shoes'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['fuzzyweight'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['ignoremarking'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['markdownverify'])) 
    
    
    cur = all_db.cursor()
    cur.execute(query.qrAddinventitemoptions,curVal)
    all_db.commit() 

def createDB():
        
    with open(pathSqript, 'r') as sql_file:
        sql_script = sql_file.read()
        
    cursor = all_db.cursor()
    cursor.executescript(sql_script)
    all_db.commit()
    #all_db.close()