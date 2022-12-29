
curVal = ''
addinvent = ''

# заполнить таблицу иначе она пустая и некоторые сложности при добавлении записи, поом переделать
qrAddOptions = '''insert into optionsa  (inventitemoptions,priceoptions,quantityoptions, remainsoptions)
                    SELECT inventcode,inventcode, inventcode, inventcode FROM invent'''

qrAddPriceoptions = '''INSERT INTO priceoptions (priceoptionsid, enablepricemanual, requirepricemanual, requireselectprice, requiredeferredprice,enableexcisemarkprice)
                    VALUES 
                    (:priceoptionsid, :enablepricemanual, :requirepricemanual, :requireselectprice, :requiredeferredprice, :enableexcisemarkprice);'''

qrAddinventitemoptions = '''INSERT INTO inventitemoptions (inventitemoptionsid, disablebackinsale, disableinventshow, disableinventsale, disableinventback, requiredepartmentmanual,
                                    enabledepartmentmanual, enablebarcodemanual, enablebarcodescanner, visualverify, ageverify, requiresalerestrict, egaisverify, 
                                    prepackaged, nopdfegaisverify, alcoset, freesale, rfidverify, lowweight, weightcontrolbypass, tobacco, shoes, fuzzyweight, 
                                    ignoremarking, markdownverify)
                                    VALUES 
                                    (:inventitemoptionsid,:disablebackinsale, :disableinventshow, :disableinventsale, :disableinventback, :requiredepartmentmanual, 
                                    :enabledepartmentmanual, :enablebarcodemanual, :enablebarcodescanner, :visualverify, :ageverify, :requiresalerestrict, :egaisverify, 
                                    :prepackaged, :nopdfegaisverify, :alcoset, :freesale, :rfidverify, :lowweight, :weightcontrolbypass, :tobacco, :shoes, :fuzzyweight, 
                                    :ignoremarking, :markdownverify);'''
                                    
qrAddquantityoptions = '''INSERT INTO quantityoptions (quantityoptionsid, enabledefaultquantity, enablequantitylimit, quantitylimit, enablequantityscales, enablequantitybarcode,
                                    enablequantitymanual, requirequantitymanual, requirequantitybarcode, requirequantityscales, enabledocumentquantitylimit, autogetquantityfromscales,
                                    documentquantlimit)
                                    VALUES (:quantityoptionsid, :enabledefaultquantity, :enablequantitylimit, :quantitylimit, :enablequantityscales, :enablequantitybarcode, 
                                    :enablequantitymanual, :requirequantitymanual, :requirequantitybarcode, :requirequantityscales, :enabledocumentquantitylimit, 
                                    :autogetquantityfromscales, :documentquantlimit) ;'''

qrAddadditionalprices = 'INSERT INTO additionalprices (additionalpricesid, pricecode, price, name) VALUES (:additionalpricesid, :pricecode, :price, :name);'

# qrAddBarcodes = '''INSERT INTO barcodes (barcodesid, additionalpricesid, aspectvaluesetcode, barcode, cquant, measurecode,
#                             minprice, name, packingmeasure, packingprice, price, quantdefault, minretailprice, customsdeclarationnumber, tmctype, ntin)
#                             VALUES
#                             (:barcodesid, :additionalprices, :aspectvaluesetcode, :barcode, :cquant, :measurecode,
#                             :minprice, :name, :packingmeasure, :packingprice, :price, :quantdefault, :minretailprice, :customsdeclarationnumber, :tmctype, :ntin );'''

qrAddBarcodes = '''INSERT INTO barcodes (barcodesid, additionalpricesid, aspectvaluesetcode, barcode, cquant, measurecode,
                                name, packingmeasure, packingprice, quantdefault, minretailprice, customsdeclarationnumber, tmctype, ntin)
                            VALUES
                            (:barcodesid, :additionalprices, :aspectvaluesetcode, :barcode, :cquant, :measurecode,
                                :name, :packingmeasure, :packingprice, :quantdefault, :minretailprice, :customsdeclarationnumber, :tmctype, :ntin );'''



qrAddSellrestrictperiods = '''INSERT INTO sellrestrictperiods (sellrestrictperiodsid, dateend, datestart, dayend, daystart, timeend,
                            timestart)
                            VALUES
                            (:sellrestrictperiodsid, :dateend, :datestart, :dayend, :daystart, :timeend,
                            :timestart);'''

qrAddPriceoptions = '''INSERT INTO priceoptions (priceoptionsid, enablepricemanual, requirepricemanual, requireselectprice, requiredeferredprice,enableexcisemarkprice)
                    VALUES 
                    (:priceoptionsid, :enablepricemanual, :requirepricemanual, :requireselectprice, :requiredeferredprice, :enableexcisemarkprice);'''




# qrAddinvent = '''INSERT INTO invent (inventcode, inventgroup, name, barcode, barcodes, price, minprice, additionalprices, options, 
#                                 sellrestrictperiods, extendedoptions, discautoscheme, deptcode, taxgroupcode, measurecode, remain, remaindate, articul,
#                                 defaultquantity, taramode, taracapacity, aspectschemecode, aspectvaluesetcode, aspectusecase, aspectselectionrule, age, 
#                                 alcoholpercent, cquant, inn, kpp, alctypecode, paymentobject, manufacturercountrycode, opmode, loyaltymode, minretailprice, 
#                                 isParent, Parent)
#                                 VALUES
#                                 (:inventcode,:inventgroup,:name,:barcode,:barcodes,:price,:minprice,:additionalprices,:options,:sellrestrictperiods,
#                                 :extendedoptions,:discautoscheme,:deptcode,:taxgroupcode,:measurecode,:remain,:remaindate,:articul,:defaultquantity,
#                                 :taramode,:taracapacity,:aspectschemecode,:aspectvaluesetcode,:aspectusecase,:aspectselectionrule,:age,:alcoholpercent,
#                                 :cquant,:inn,:kpp,:alctypecode,:paymentobject,:manufacturercountrycode,:opmode,:loyaltymode,:minretailprice,:isParent,:Parent);'''


qrAddinvent = '''INSERT INTO invent (inventcode,  name,  barcodes, price, minprice, additionalprices, options, 
                                sellrestrictperiods, extendedoptions, discautoscheme, deptcode, taxgroupcode, measurecode, remain, remaindate, articul,
                                defaultquantity, taramode, taracapacity,  aspectusecase, aspectselectionrule, age, 
                                alcoholpercent, cquant, inn, kpp, alctypecode, paymentobject, manufacturercountrycode, opmode, loyaltymode, minretailprice, 
                                isParent, Parent)
                                VALUES
                                (:inventcode,:name,:barcodes,:price,:minprice,:additionalprices,:options,:sellrestrictperiods,
                                :extendedoptions,:discautoscheme,:deptcode,:taxgroupcode,:measurecode,:remain,:remaindate,:articul,:defaultquantity,
                                :taramode,:taracapacity,:aspectusecase,:aspectselectionrule,:age,:alcoholpercent,
                                :cquant,:inn,:kpp,:alctypecode,:paymentobject,:manufacturercountrycode,:opmode,:loyaltymode,:minretailprice,:isParent,:Parent);'''


qrSelectSales = 'SELECT goodsitemid, documentid, ttime, opcode,  cquant, code From goodsitem'
qrSimpleSelectSale =  'SELECT code, opcode,  CAST(cquant AS CHAR) AS cquant  From goodsitem'
qrSelectBarcodes = 'SELECT * FROM barcodes where barcodesid = ?'


qrCalculatingTheAmount = '''UPDATE invent 
set remain  = sumItog.summItog 
FROM (
SELECT invent.inventcode, (SummIsParent.remain + invent.remain) as summItog FROM SummIsParent 
INNER JOIN
invent ON SummIsParent.isParent = invent.inventcode
) as sumItog
WHERE  invent.inventcode  = sumItog.inventcode'''


# Work file

header = "### data begin ###"
footer = "### data end ###"
separator = "---"
#addInventItem = str({"command": "addInventItem" }) # Команда addInventItem добавляет товар в справочник товаров. 
clearInventory = {"command":"clearInventory"} # Команда clearInventory очищает справочник товаров со всеми зависимыми записями. 
clearTmcScale = {"command":"clearTmcScale"}  # Команда clearTmcScale очищает справочник товаров для прогрузки на весы
addInventItem = {"command":"addInventItem"}  # Команда addInventItem добавляет товар в справочник товаров. Атрибуты товара задаются обязательным параметром invent.  
clearAspectValueSet  = {"command": "clearAspectValueSet"} #Команда clearAspectValueSet очищает справочник значений разрезов



# Запросы для формирования файла

qrAdditionalprices = '''SELECT pricecode, price, name FROM additionalprices where additionalpricesid = ?'''
qrBarcodes = '''SELECT aspectvaluesetcode, barcode, cquant, measurecode,
                            minprice, name, packingmeasure, packingprice, price, quantdefault, minretailprice, customsdeclarationnumber, tmctype, ntin 
                            FROM barcodes where barcodesid = ?'''
                            
qrsellrestrictperiods = '''SELECT dateend, datestart, dayend, daystart, timeend, timestart
                            FROM sellrestrictperiods where sellrestrictperiodsid = ?'''
qrinventitemoptions = '''SELECT disablebackinsale, disableinventshow, disableinventsale, disableinventback, requiredepartmentmanual,
                                    enabledepartmentmanual, enablebarcodemanual, enablebarcodescanner, visualverify, ageverify, requiresalerestrict, egaisverify, 
                                    prepackaged, nopdfegaisverify, alcoset, freesale, rfidverify, lowweight, weightcontrolbypass, tobacco, shoes, fuzzyweight, 
                                    ignoremarking, markdownverify
                                    FROM inventitemoptions where inventitemoptionsid = ?'''

qrpriceoptions =  '''SELECT enablepricemanual, requirepricemanual, requireselectprice, requiredeferredprice,enableexcisemarkprice
                        FROM priceoptions where priceoptionsid = ?'''                           

qrquantityoptions = '''SELECT enabledefaultquantity, enablequantitylimit, quantitylimit, enablequantityscales, enablequantitybarcode,
                                    enablequantitymanual, requirequantitymanual, requirequantitybarcode, requirequantityscales, enabledocumentquantitylimit, autogetquantityfromscales,
                                    documentquantlimit
                        FROM quantityoptions where quantityoptionsid = ?'''

qrremainsoptions = '''SELECT * FROM remainsoptions where remainsoptionsid = ?'''

