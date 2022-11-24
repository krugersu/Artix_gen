
import json
import sqlite3
from datetime import datetime
from types import SimpleNamespace
from pathlib import Path  
import diff_data
import logging
import main
from datetime import datetime


pathDB = Path("data", "myDB.sqlite") 
pathSqript = Path("data", "createDB.sql") 

all_db=sqlite3.connect(pathDB)
baseTableName = 'invent'


def saveDataDB(c_count):

    

    createDB()
    recursive_items(c_count)



def recursive_items(dictionary):
    logging.info('Start add DB from 1C - ' + str(datetime.now()))
    for i in range(len(dictionary)-1):
        addRecord(dictionary[i])
        
    logging.info('End add DB from 1C - ' + str(datetime.now()))    
    logging.info('added - ' + str(i) + ' reords')    
        
        
def addRecord(item_position):
    
    curVal = [] 
    cur = all_db.cursor()
    cur.execute('PRAGMA synchronous = OFF')
    #LiteConnection1.ExecSQL
    
    if len (item_position['options']['priceoptions']) > 0:
        curVal = diff_data.getListPriceoptions(item_position)
        cur.execute(diff_data.qrAddPriceoptions,curVal)
    

    
    if len (item_position['options']['quantityoptions']) > 0:
        curVal.clear()
        curVal = diff_data.getListquantityoptions(item_position)
        cur.execute(diff_data.qrAddquantityoptions,curVal)
    
    
    if len (item_position['additionalprices']) > 0:
        curVal.clear()
        curVal = diff_data.getListadditionalprices(item_position)
        cur.execute(diff_data.qrAddadditionalprices,curVal)

    
    if len (item_position['options']['inventitemoptions']) > 0:
        curVal.clear()
        curVal = diff_data.getListinventitemoptions(item_position)
        cur.execute(diff_data.qrAddinventitemoptions,curVal)    
        
    
        curVal.clear()
        curVal = diff_data.getListinvent(item_position)
        cur.execute(diff_data.qrAddinvent,curVal)    
    
    
    all_db.commit() 

    
    
    
    
def createDB():
        
    with open(pathSqript, 'r') as sql_file:
        sql_script = sql_file.read()
        
    cursor = all_db.cursor()
    cursor.executescript(sql_script)
    all_db.commit()
    #all_db.close()