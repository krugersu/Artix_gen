  print(rc.get('artix','server_ip'))
    r = requests.get('http://192.168.252.250:8082/UNF_test/hs/test_s/V1/test')
    r.encoding = 'utf-8' 
    print(r.status_code)
    #print(r.json())    
    #print(r.text)    




    '''  for item in dict_json.items():
        # item — это кортеж (ключ, значение)
        print(item[0]) '''
    #iterate(dict_json)   
   # tableName = []
#    tableName = getTableName(dict_json,tableName)
#    iterate(dict_json)
 #   textQuery = createQuery(tableName) 
   # createTable(textQuery)
    #createFullDB(dict_json)
       
    # data = json.load(json_file)


# Parse JSON into an object with attributes corresponding to dict keys.
    #x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
  #  print(dict_json['invent']['price'],dict_json['invent']['options']['quantityoptions']['documentquantlimit'])
    
'''    with open('D:\Artix\Artix_gen\src\st.json', encoding='utf-8-sig') as json_file:
        json_data = json.loads(json_file.read())
    
    #Aim of this block is to get the list of the columns in the JSON file.
        columns = []
        column = []
        for data in json_data:
            column = list(data.keys())
            for col in column:
                if col not in columns:
                    columns.append(col)
                                
    #Here we get values of the columns in the JSON file in the right order.   
        value = []
        values = [] 
        for data in json_data:
            for i in columns:
                value.append(str(dict(data).get(i)))   
            values.append(list(value)) 
            value.clear()
        
    #Time to generate the create and insert queries and apply it to the sqlite3 database       
        create_query = "create table if not exists myTable ({0})".format(" text,".join(columns))
        insert_query = "insert into myTable ({0}) values (?{1})".format(",".join(columns), ",?" * (len(columns)-1))    
        print("insert has started at " + str(datetime.now()))  
        c = db.cursor()   
        c.execute(create_query)
        c.executemany(insert_query , values)
        values.clear()
        db.commit()
        c.close()
        print("insert has completed at " + str(datetime.now()))  '''
        
        
        
        #recursive function to iterate a nested dictionary      
''' def iterate(dictionary, indent=4):
  #  print('{')
    for key, value in dictionary.items():
        #recurse if the value is a dictionary
        if type(value) is dict:
         #   print('1 '*indent, key, ": ", end='')
            iterate(value, indent+4)
        else:
            
            print('2 '*indent, key, ": ", value)
            
   # print(' '*(indent-4), '}') '''
    
''' def getTableName(dictionary,tableName, indent=1):

    for key, value in dictionary.items():
        #recurse if the value is a dictionary
        if type(value) is dict:
            tableName.append(str(key))
            getTableName(value, tableName,indent)
        else:
            pass
   # print(tableName)
    return tableName


def createTable(textQuery):

    cur = all_db.cursor()
    cur.execute(textQuery)
    all_db.commit() 
     '''

''' def createQuery(tableName): 

    for table in tableName:
        users = table
        userid = table + 'id'
        textQuery =  f"""CREATE TABLE IF NOT EXISTS {users}( {userid} INT PRIMARY KEY );"""
        textQueryDelete =  f"""DROP TABLE IF EXISTS {users};"""
        deleteRecordTable(textQueryDelete)
        createTable(textQuery)
       # print (textQuery)
        
def createQueryColumn(tableName,colName): 

    textQuery =  f"""ALTER TABLE {tableName} ADD COLUMN {colName} 'TEXT'"""
    addColumn(textQuery)


def addColumn(textQuery):
    cur = all_db.cursor()
    cur.execute(textQuery)
    all_db.commit() 

def deleteRecordTable(textQuery):
    
    cur = all_db.cursor()
    cur.execute(textQuery)
    all_db.commit() 
    
    
# Попытка создать структуру БД при одном проходе структуры JSON    
def createFullDB(dictionary, indent=4):
    mTableName = ''
    for key, value in dictionary.items():
        #recurse if the value is a dictionary
        if type(value) is dict:
            mTableName = key
            #print(mTableName)
            print('1 '*indent, key, ": ", end='')
         #   createQuery(key)
         #   createFullDB(value, indent+4)
        else:
            #print(key)
          #  createQueryColumn(mTableName,key) 
            print('2 '*indent, key, ": ", value)
            


def saveDataDB(data):
    pass '''
    
    
    
'''     jtopy=json.dumps(data) #json.dumps take a dictionary as input and returns a string as output.
    dict_json=json.loads(jtopy)
 '''


''' def recursive_itemsD(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
        
            yield (key, value)
            yield from recursive_items(value)
        else:
            yield (key, value)

 '''    
 
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
    
    
    
    
    ''' def getListPriceoptions(item_position):
    
    curVal =[]
    curVal.append(item_position['inventcode'].strip())
    curVal.append(int(item_position['enablepricemanual'])) 
    curVal.append(int(item_position['requirepricemanual'])) 
    curVal.append(int(item_position['requireselectprice'])) 
    curVal.append(int(item_position['requiredeferredprice'])) 
    curVal.append(int(item_position['enableexcisemarkprice'])) 
    
    return curVal


def getListadditionalprices(item_position):
    
    curVal =[]
    
    curVal.append(item_position['inventcode'].strip())
    curVal.append(int(item_position['additionalprices']['pricecode'])) 
    curVal.append(int(item_position['additionalprices']['price'])) 
    curVal.append(int(item_position['additionalprices']['price'])) 
    
    return curVal


def getListquantityoptions(item_position):
    
    curVal =[]
    
    curVal.append(item_position['inventcode'].strip())
    curVal.append(int(item_position['options']['quantityoptions']['enabledefaultquantity'])) 
    curVal.append(int(item_position['options']['quantityoptions']['enablequantitylimit'])) 
    curVal.append(int(item_position['options']['quantityoptions']['quantitylimit'])) 
    curVal.append(int(item_position['options']['quantityoptions']['enablequantityscales'])) 
    curVal.append(int(item_position['options']['quantityoptions']['enablequantitybarcode']))     
    curVal.append(int(item_position['options']['quantityoptions']['enablequantitymanual'])) 
    curVal.append(int(item_position['options']['quantityoptions']['requirequantitymanual'])) 
    curVal.append(int(item_position['options']['quantityoptions']['requirequantitybarcode'])) 
    curVal.append(int(item_position['options']['quantityoptions']['requirequantityscales'])) 
    curVal.append(int(item_position['options']['quantityoptions']['enabledocumentquantitylimit']))     
    curVal.append(int(item_position['options']['quantityoptions']['autogetquantityfromscales'])) 
    curVal.append((item_position['options']['quantityoptions']['documentquantlimit']))     
    
    return curVal

def getListinventitemoptions(item_position):
    
    curVal =[]

    curVal.append(item_position['inventcode'].strip())
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
    
    return curVal


def getListinvent(item_position):
    
    curVal =[]

    curVal.append(None) 
    curVal.append(item_position['inventcode'].strip()) 
    curVal.append(item_position['inventgroup']) 
    curVal.append(item_position['name']) 
    curVal.append(item_position['barcode'])
    curVal.append(item_position['inventcode']) 
    curVal.append(item_position['price']) 
    curVal.append(item_position['minprice']) 
    curVal.append(item_position['inventcode']) 
    curVal.append(item_position['inventcode']) 
    curVal.append(item_position['inventcode']) 
    curVal.append(item_position['extendedoptions']) 
    curVal.append(item_position['discautoscheme']) 
    curVal.append(item_position['deptcode']) 
    curVal.append(item_position['taxgroupcode']) 
    curVal.append(item_position['measurecode']) 
    curVal.append(item_position['remain']) 
    curVal.append(item_position['remaindate']) 
    curVal.append(item_position['articul']) 
    curVal.append(item_position['defaultquantity']) 
    curVal.append(item_position['taramode']) 
    curVal.append(item_position['taracapacity']) 
    curVal.append(item_position['aspectschemecode']) 
    curVal.append(item_position['aspectvaluesetcode']) 
    curVal.append(item_position['aspectusecase']) 
    curVal.append(item_position['aspectselectionrule']) 
    curVal.append(item_position['age']) 
    curVal.append(item_position['alcoholpercent']) 
    curVal.append(item_position['cquant']) 
    curVal.append(item_position['inn']) 
    curVal.append(item_position['kpp']) 
    curVal.append(item_position['alctypecode']) 
    curVal.append(item_position['paymentobject'])                   
    curVal.append(item_position['manufacturercountrycode']) 
    curVal.append(item_position['opmode']) 
    curVal.append(item_position['loyaltymode']) 
    curVal.append(item_position['minretailprice']) 
    curVal.append(item_position['Parent']) 
    curVal.append(item_position['isParent'].strip())                                                                                                                                                                                                                                           
    
    return curVal '''
    
    
    
    
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



''' c.execute('''WITH RECURSIVE parents AS (select * from invent
                    inner JOIN (SELECT *  FROM barcodes) as st
                    ON st.barcodesid  = invent.inventcode
                    )
                    SELECT *
                    FROM parents''') '''
                    
                    
                    
                            ''' while True:
            next_row = self._cursor.fetchone()
            if next_row:
                print(next_row)
            else:
                break '''