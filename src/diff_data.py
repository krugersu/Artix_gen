
curVal = ''
addinvent = ''

qrAddPriceoptions = 'INSERT INTO priceoptions VALUES (?, ?, ?, ?, ?,?);'
qrAddinventitemoptions = 'INSERT INTO inventitemoptions VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'
qrAddquantityoptions = 'INSERT INTO quantityoptions VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?);'
qrAddadditionalprices = 'INSERT INTO additionalprices (additionalpricesid, pricecode, price, name) VALUES (:additionalpricesid, :pricecode, :price, :name);'

qrBarcodes = '''INSERT INTO barcodes (barcodesid, additionalpricesid, aspectvaluesetcode, barcode, cquant, measurecode,
                            minprice, name, packingmeasure, packingprice, price, quantdefault, minretailprice, customsdeclarationnumber, tmctype, ntin)
                            VALUES
                            (:barcodesid, :additionalprices, :aspectvaluesetcode, :barcode, :cquant, :measurecode,
                            :minprice, :name, :packingmeasure, :packingprice, :price, :quantdefault, :minretailprice, :customsdeclarationnumber, :tmctype, :ntin );'''


qrAddinvent = '''INSERT INTO invent (inventcode, inventgroup, name, barcode, barcodesid, price, minprice, additionalpricesid, options, 
                                sellrestrictperiodsid, extendedoptions, discautoscheme, deptcode, taxgroupcode, measurecode, remain, remaindate, articul,
                                defaultquantity, taramode, taracapacity, aspectschemecode, aspectvaluesetcode, aspectusecase, aspectselectionrule, age, 
                                alcoholpercent, cquant, inn, kpp, alctypecode, paymentobject, manufacturercountrycode, opmode, loyaltymode, minretailprice, 
                                isParent, Parent)
                                VALUES
                                (:inventcode,:inventgroup,:name,:barcode,:barcodes,:price,:minprice,:additionalprices,:options,:sellrestrictperiods,
                                :extendedoptions,:discautoscheme,:deptcode,:taxgroupcode,:measurecode,:remain,:remaindate,:articul,:defaultquantity,
                                :taramode,:taracapacity,:aspectschemecode,:aspectvaluesetcode,:aspectusecase,:aspectselectionrule,:age,:alcoholpercent,
                                :cquant,:inn,:kpp,:alctypecode,:paymentobject,:manufacturercountrycode,:opmode,:loyaltymode,:minretailprice,:isParent,:Parent);'''


qrSelectSales = 'SELECT goodsitemid, documentid, ttime, opcode,  cquant, code From goodsitem'
qrSimpleSelectSale =  'SELECT code, opcode,  CAST(cquant AS CHAR) AS cquant  From goodsitem'


qrCalculatingTheAmount = '''UPDATE invent 
set remain  = sumItog.summItog 
FROM (
SELECT invent.inventcode, (SummIsParent.remain + invent.remain) as summItog FROM SummIsParent 
INNER JOIN
invent ON SummIsParent.isParent = invent.inventcode
) as sumItog
WHERE  invent.inventcode  = sumItog.inventcode'''


def getListPriceoptions(item_position):
    
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
    
    return curVal