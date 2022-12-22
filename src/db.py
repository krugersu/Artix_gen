
import sys
import json
import shutil
import sendFile
from datetime import datetime
from types import SimpleNamespace
from pathlib import Path  
import diff_data
import logging
import m_config
from datetime import datetime
from pprint import pprint

#import MySQLdb
import pymysql
#import m_config
import codecs


if sys.platform.startswith("linux"):  # could be "linux", "linux2", "linux3", ...
    import pysqlite3
elif sys.platform == "darwin":
    pass
elif sys.platform == "win32":
   import sqlite3


class workDb:
    def __init__(self,rc, c_count = None):
        
        self.pathDB = Path("data", "myDB.sqlite")
        
        if sys.platform.startswith("linux"):  # could be "linux", "linux2", "linux3", ...
                pysqlite3.paramstyle = 'named'
                self._all_db = pysqlite3.connect(self.pathDB)
        elif sys.platform == "darwin":
            pass
        elif sys.platform == "win32":
            sqlite3.paramstyle = 'named'
            self._all_db = sqlite3.connect(self.pathDB)
        

        self.pathScript = Path("data", "createDB.sql") 
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
        #print(x)    
            #c.executemany('INSERT INTO students VALUES(?,?,?);',records);
        self._cursor.executemany('INSERT INTO goodsitem VALUES(?,?,?)',x)    
        self._all_db.commit() 
        self.mydb.close()
 
        
    def createDB(self):
        """AI is creating summary for createDB
        """        
        with open(self.pathScript, 'r') as sql_file:
            sql_script = sql_file.read()

        self.cursor.executescript(sql_script)
        self._all_db.commit()
    #all_db.close()
    
    
    def uploadData(self,c_count, shop_Number):
                
        self.createDB()
        self.recursive_items(c_count)
        self.CalculatingTheAmount()
        self.querySales()
        self.calculateSales()
        self.testDB(shop_Number)
        
    def recursive_items(self,dictionary):
        
        logging.info('Start add DB from 1C')
        count = 0
        for key  in dictionary:
          #  print(key)
            self.addRecord(dictionary[key],key)
            count = count + len(dictionary[key])
        
        logging.info('End add DB from 1C')    
        logging.info('added - ' + str(count) + ' records')    


    def CalculatingTheAmount(self):
        """Запускает SQL скрипт, который переносит количество с аналагов пива на головную номенклатуру"""        
        pathScript = Path("data", "upd.sql") 
        with open(pathScript, 'r') as sql_file:
            sql_script = sql_file.read()
        self._cursor.executescript(sql_script)
        logging.info('Summ analog calcalating')  

    def addRecord(self,item_position,key):

        self._cursor.execute('PRAGMA synchronous = OFF')

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
        elif key == 'quantityoptions':
            self._cursor.executemany(diff_data.qrAddquantityoptions, item_position,)                               
        elif key == 'sellrestrictperiods':
            self._cursor.executemany(diff_data.qrAddSellrestrictperiods, item_position,)                                           

        self._cursor.execute(diff_data.qrAddOptions)
        
        self._all_db.commit() 
        
        
    def calculateSales(self):
        """Запускает SQL скрипт, который отнимает проданное от пришедшего товара"""        
        pathScript = Path("data", "updateprod.sql") 
        with open(pathScript, 'r') as sql_file:
            sql_script = sql_file.read()
        self._cursor.executescript(sql_script)
        logging.info('Sales calcalating')              
        
        
    def testDB(self,shop_Number):
        """Maps a number from one range to another.
    :param number:  The input number to map.
    :param in_min:  The minimum value of an input number.
    :param in_max:  The maximum value of an input number.
    :param out_min: The minimum value of an output number.
    :param out_max: The maximum value of an output number.
    :return: The mapped number.
    """
    
        #self._cursor.execute("select * from invent")
        #sql - это ваш cursor
        #massive = self._cursor.fetchone()#этот метод вернет вам один кортеж с только одной строкой из базы
        #  massive_big = self._cursor.fetchall()#этот метод вернет вам все элементы в одном кортеже. Данные из строк будут представлены как вложенные кортежи
        #перебираем обычный кортеж, просто печатаем элементы кортежа
        #for i in range(len(massive)):
        #    print(massive[i])
        
        if sys.platform.startswith("linux"):  # could be "linux", "linux2", "linux3", ...
                self._all_db.row_factory = pysqlite3.Row # Позволяет работать с возвращаемым результатам с обращением к столбцам по имени
        elif sys.platform == "darwin":
            pass
        elif sys.platform == "win32":
            self._all_db.row_factory = sqlite3.Row
        
        #outfile = open('tData.aif', 'w',encoding='utf-8')  
        curFileName = 'pos' + str(shop_Number) + '.aif'
        pathAif = Path("upload", curFileName) 
        outfile = open(pathAif, 'w',encoding='utf-8')  
        outfile.writelines(diff_data.header+ '\n')
        outfile.writelines(json.dumps(diff_data.clearInventory)+ '\n')
        
        outfile.writelines(diff_data.separator+ '\n')
        outfile.writelines(json.dumps(diff_data.clearTmcScale)+ '\n')    
        outfile.writelines(diff_data.separator+ '\n')
        
        dictForArtix = {}
        c = self._all_db.cursor()
        
        c.execute('SELECT * FROM invent')                          
        
        while True:
            invent=c.fetchone()
            if invent:

        # Add Barcodes
                cBar = self._all_db.cursor()
#                nDict = dict(diff_data.addInventItem) 
#                tCommand = diff_data.addInventItem      
                
                nDict = (dict(invent))
#               nCommand = {}
#              tCommand.update(nDict)
                
                tCode = ((nDict['inventcode']))


                cBar.execute(diff_data.qrBarcodes,(tCode,))
                                        
                tBarcodes = dict(invent)
                barcodes = cBar.fetchall()  
                allBarcodes = []
                for itm in barcodes:
                    allBarcodes.append((dict(itm)) )
                
                #nDict['barcodes'] = allBarcodes
                
                # Add sellrestrictperiods Массив ограничений продаж по времени, пока не заполняем, нам без надобности
                cSellPeriod = self._all_db.cursor()       
                cSellPeriod.execute(diff_data.qrsellrestrictperiods,(tCode,))
                sellrestrictperiods = cSellPeriod.fetchall()  
                allSellrestrictperiods = []
                for itm in sellrestrictperiods:
                    allSellrestrictperiods.append((dict(itm)) )


                # Add Additionalprices  Массив дополнительных цен
                cAdditionalprices = self._all_db.cursor()       
                cAdditionalprices.execute(diff_data.qrAdditionalprices,(tCode,))
                additionalpricesid = cAdditionalprices.fetchall()  
                alladditionalpricesid = []
                for itm in additionalpricesid:
                    alladditionalpricesid.append((dict(itm)) )



                # Add inventitemoptions Опции товара
                cinventitemoptions = self._all_db.cursor()       
                cinventitemoptions.execute(diff_data.qrinventitemoptions,(tCode,))
                inventitemoptions = cinventitemoptions.fetchall()  
                # allinventitemoptions = {}
                for itm in inventitemoptions:
                    # allinventitemoptions.append((dict(itm)) )
                    allinventitemoptions = (dict(itm))

                # Add priceoptions Опции цены
                cpriceoptions = self._all_db.cursor()       
                cpriceoptions.execute(diff_data.qrpriceoptions,(tCode,))
                priceoptions = cpriceoptions.fetchall()  
                # allpriceoptions = []
                for itm in priceoptions:
                    allpriceoptions = (dict(itm)) 
        


                # Add quantityoptions Опции количества
                cquantityoptions = self._all_db.cursor()       
                cquantityoptions.execute(diff_data.qrquantityoptions,(tCode,))
                quantityoptions = cquantityoptions.fetchall()  
                #allquantityoptions = []
                for itm in quantityoptions:
                    allquantityoptions = (dict(itm))



                # Add quantityoptions Опции количества
                cremainsoptions = self._all_db.cursor()       
                cremainsoptions.execute(diff_data.qrremainsoptions,(tCode,))
                remainsoptions = cremainsoptions.fetchall()  
                #allremainsoptions = []
                for itm in remainsoptions:
                    allremainsoptions = (dict(itm))

        
##########################################################################################
                # Add options Опции товара
                '''   coptions = self._all_db.cursor()       
                coptions.execute("SELECT * FROM options where optionsidid = ?",(tCode,))
                options = coptions.fetchall()   '''
                alloptions = {}
                alloptions['inventitemoptions'] = allinventitemoptions
                alloptions['priceoptions'] = allpriceoptions
                alloptions['quantityoptions'] = allquantityoptions   
                #alloptions['remainsoptions'] = allremainsoptions   Опции учета остатков, пока ни как не реализованы, оставлены на будущее          
                
                ''' for itm in options:
                    alloptions.append((dict(itm)) ) '''
###########################################################################################



                    
                nDict['options'] = alloptions                        
                nDict['sellrestrictperiods'] = allSellrestrictperiods                    
                nDict['additionalprices'] = alladditionalpricesid                    
                nDict['barcodes'] = allBarcodes
                
                tCommand = diff_data.addInventItem      
                comDict = (dict(tCommand))
                nCommand = {}
                nCommand['invent'] = nDict
                comDict.update(nCommand)
                
                
                #pprint(nDict)
                
                dictForArtix.update(comDict)
                
                #outfile.writelines(str(nDict))
                #outfile.writelines(diff_data.separator)
                
                json.dump(dictForArtix, outfile,  indent=2,  ensure_ascii=False )
                
                outfile.write('\n' + diff_data.separator + '\n')    
            else:
                break    
        outfile.write(diff_data.footer)  
        
        #pathAif
        sendFile.sendFile(pathAif,shop_Number)
        # src =  pathAif
        # dst = '//192.168.0.239/obmen/dict/'+ curFileName
        # shutil.copyfile(src, dst)
        #перебираем кортеж с кортежами внутри, также печатаем элементы
        #for z in range(len(massive_big)):
        #    print(massive_big[z])        
        #{"command":"addInventItem",