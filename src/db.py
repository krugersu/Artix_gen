
import json
#import sqlite3 
import pysqlite3
from datetime import datetime
from types import SimpleNamespace
from pathlib import Path  
import diff_data
import logging
import m_config
from datetime import datetime

#import MySQLdb
import pymysql
#import m_config
 


pathDB = Path("data", "myDB.sqlite") 
pathScript = Path("data", "createDB.sql") 

#all_db=sqlite3.connect(pathDB)




all_db=pysqlite3.connect(pathDB)
baseTableName = 'invent'


#server connection
''' mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd=""
)

  '''



def saveDataDB(c_count):

    

    m_conf = m_config.m_Config()   
    rc =  m_conf.loadConfig()
    mydb = pymysql.connect(host=rc._sections.artix.server_ip,
            database=rc._sections.artix.database,
            user=rc._sections.artix.user,
            passwd=rc._sections.artix.passwd)
    mycursor = mydb.cursor() #cursor created
    
    #work with the cursor
    res = "Select * from kkm;"

#executing the query
    mycursor.execute(res)

    rows = mycursor.fetchall()

    #showing the rows
    for row in rows:
        print(row)

    #closing the db
    # mydb.commit()
    mydb.close()
    
    
    createDB()
    recursive_items(c_count)
    CalculatingTheAmount()



def recursive_items(dictionary):
    """AI is creating summary for recursive_items

    Args:
        dictionary ([type]): [description]
    """
    
    logging.info('Start add DB from 1C')
    count = 0
    for i in range(len(dictionary)-1):
        addRecord(dictionary[i])
        count = i
        
    logging.info('End add DB from 1C')    
    logging.info('added - ' + str(count) + ' records')    
        
        
def addRecord(item_position):
    """AI is creating summary for addRecord

    Args:
        item_position ([type]): [description]
    """
    
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
    
        
    with open(pathScript, 'r') as sql_file:
        sql_script = sql_file.read()
        
    cursor = all_db.cursor()
    cursor.executescript(sql_script)
    all_db.commit()
    #all_db.close()
    
    
def CalculatingTheAmount():
    
    """AI is creating summary for 
    """
    
    pathScript = Path("data", "upd.sql") 
    with open(pathScript, 'r') as sql_file:
        sql_script = sql_file.read()
    cur = all_db.cursor()
    #cur.execute(diff_data.qrCalculatingTheAmount)
    cur.executescript(sql_script)
    logging.info('Summ analog calcalating')  
