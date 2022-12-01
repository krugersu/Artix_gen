
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
 


#pathDB = Path("data", "myDB.sqlite") 
#pathScript = Path("data", "createDB.sql") 

#all_db=sqlite3.connect(pathDB)
#all_db=pysqlite3.connect(pathDB)
#baseTableName = 'invent'


#server connection
''' mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd=""
)

  '''


class workDb:
    def __init__(self,rc, c_count = None):
        pysqlite3.paramstyle = 'named'        
        self.pathDB = Path("data", "myDB.sqlite") 
        self.pathScript = Path("data", "createDB.sql") 
        self._all_db = pysqlite3.connect(self.pathDB)
 #       self._all_db = sqlite3.connect(self.pathDB)
        self._cursor = self._all_db.cursor()
        self.baseTableName = 'invent'
        
        self.c_count = c_count
        
        self.mydb = pymysql.connect(host=rc._sections.artix.server_ip,
            database=rc._sections.artix.database,
            user=rc._sections.artix.user,
            passwd=rc._sections.artix.passwd)
        self._mycursor = self.mydb.cursor() #cursor created

        
    def __enter__(self):
        
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        
        self.close()
        
    @property
    def connection(self):
        
        return self._conn
    
    @property
    def cursor(self):
        
        return self._cursor
    
    def commit(self):
        self.connection.commit()
    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
    def fetchall(self):
        return self.cursor.fetchall()
    def fetchone(self):
        return self.cursor.fetchone()
    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def querySales(self):

        #executing the query
        self._mycursor.execute(diff_data.qrSimpleSelectSale)

        x = []
        rows = self._mycursor.fetchall()
        #rows = self._mycursor.fetchmany(1)
        
        #showing the rows
        for row in rows:
        #    print(row)
            x.append(row)
        print(x)    
            #c.executemany('INSERT INTO students VALUES(?,?,?);',records);
        self._cursor.executemany('INSERT INTO goodsitem VALUES(?,?,?)',x)    
        
        #closing the db
       #self.mydb.commit()
        self._all_db.commit() 
        self.mydb.close()
 
        
    def createDB(self):
        
        with open(self.pathScript, 'r') as sql_file:
            sql_script = sql_file.read()
        
        #self.cursor = self._all_db.cursor()
        self.cursor.executescript(sql_script)
        self._all_db.commit()
    #all_db.close()
    def uploadData(self,c_count):
        
        self.createDB()
        self.recursive_items(c_count)
       # self.CalculatingTheAmount()
       # self.querySales()
        
    def recursive_items(self,dictionary):
        logging.info('Start add DB from 1C')
        count = 0
        for key  in dictionary:
            print(key)
        
            self.addRecord(dictionary[key],key)
            
            ++ count 
            x = []
                

#            self.addRecord(x)
        
        logging.info('End add DB from 1C')    
        logging.info('added - ' + str(count) + ' records')    


    def CalculatingTheAmount(self):
    
        pathScript = Path("data", "upd.sql") 
        with open(pathScript, 'r') as sql_file:
            sql_script = sql_file.read()
        
        #cur.execute(diff_data.qrCalculatingTheAmount)
        self._cursor.executescript(sql_script)
        logging.info('Summ analog calcalating')  

    def addRecord(self,item_position,key):
       
        self._cursor.execute('PRAGMA synchronous = OFF')
       
        curQuery = {
                'invent': 10**-3,
                'additionalprices': 'qrAddinvent',
                'barcodes': 10**-1,
                'inventitemoptions': 1,
                'priceoptions': 10**3,
                'quantityoptions': 1,
                'sellrestrictperiods': 10**3
            }
        if key == 'invent':
            self._cursor.executemany(diff_data.qrAddinvent, item_position,)
        elif key == 'additionalprices':
            self._cursor.executemany(diff_data.qrAddadditionalprices, item_position,)   
        elif key == 'barcodes':
            self._cursor.executemany(diff_data.qrAddBarcodes, item_position,)   
        elif key == 'inventitemoptions':
            self._cursor.executemany(diff_data.qrAddinventitemoptions, item_position,)       
        elif key == 'priceoptions':
            self._cursor.executemany(diff_data.qrAddPriceoptions, item_position,)                   
            
            
        '''   
        if len (item_position['priceoptions']) > 0:
            curVal = diff_data.getListPriceoptions(item_position)
            self._cursor.execute(diff_data.qrAddPriceoptions,curVal) '''
    
        ''' if len (item_position['options']['quantityoptions']) > 0:
            curVal.clear()
            curVal = diff_data.getListquantityoptions(item_position)
            self._cursor.execute(diff_data.qrAddquantityoptions,curVal)
    
        if len (item_position['additionalprices']) > 0:
            curVal.clear()
            curVal = diff_data.getListadditionalprices(item_position)
            self._cursor.execute(diff_data.qrAddadditionalprices,curVal)
    
        if len (item_position['options']['inventitemoptions']) > 0:
            curVal.clear()
            curVal = diff_data.getListinventitemoptions(item_position)
            self._cursor.execute(diff_data.qrAddinventitemoptions,curVal)    
    
            curVal.clear()
            curVal = diff_data.getListinvent(item_position)
            self._cursor.execute(diff_data.qrAddinvent,curVal)     '''
    
        self._all_db.commit() 






