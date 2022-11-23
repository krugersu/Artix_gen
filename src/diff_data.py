
curVal = ''
addinvent = ''

qrAddPriceoptions = 'INSERT INTO priceoptions VALUES (?, ?, ?, ?, ?,?);'
qrAddinventitemoptions = 'INSERT INTO inventitemoptions VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'
qrAddquantityoptions = 'INSERT INTO quantityoptions VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?);'
qrAddadditionalprices = 'INSERT INTO additionalprices VALUES (?, ?, ?, ?);'


def getListPriceoptions(item_position):
    
    curVal =[]
    curVal.append(None) 
    curVal.append(int(item_position['options']['priceoptions']['enablepricemanual'])) 
    curVal.append(int(item_position['options']['priceoptions']['requirepricemanual'])) 
    curVal.append(int(item_position['options']['priceoptions']['requireselectprice'])) 
    curVal.append(int(item_position['options']['priceoptions']['requiredeferredprice'])) 
    curVal.append(int(item_position['options']['priceoptions']['enableexcisemarkprice'])) 
    
    return curVal


def getListadditionalprices(item_position):
    
    curVal =[]
    
    curVal.append(None) 
    curVal.append(int(item_position['additionalprices']['pricecode'])) 
    curVal.append(int(item_position['additionalprices']['price'])) 
    curVal.append(int(item_position['additionalprices']['price'])) 
    
    return curVal


def getListquantityoptions(item_position):
    
    curVal =[]
    
    curVal.append(None) 
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
    
    return curVal