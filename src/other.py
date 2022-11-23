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