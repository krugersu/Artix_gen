
curVal = ''
addinvent = ''

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

qrAddBarcodes = '''INSERT INTO barcodes (barcodesid, additionalpricesid, aspectvaluesetcode, barcode, cquant, measurecode,
                            minprice, name, packingmeasure, packingprice, price, quantdefault, minretailprice, customsdeclarationnumber, tmctype, ntin)
                            VALUES
                            (:barcodesid, :additionalprices, :aspectvaluesetcode, :barcode, :cquant, :measurecode,
                            :minprice, :name, :packingmeasure, :packingprice, :price, :quantdefault, :minretailprice, :customsdeclarationnumber, :tmctype, :ntin );'''


qrAddSellrestrictperiods = '''INSERT INTO sellrestrictperiods (sellrestrictperiodsid, dateend, datestart, dayend, daystart, timeend,
                            timestart)
                            VALUES
                            (:sellrestrictperiodsid, :dateend, :datestart, :dayend, :daystart, :timeend,
                            :timestart);'''

qrAddPriceoptions = '''INSERT INTO priceoptions (priceoptionsid, enablepricemanual, requirepricemanual, requireselectprice, requiredeferredprice,enableexcisemarkprice)
                    VALUES 
                    (:priceoptionsid, :enablepricemanual, :requirepricemanual, :requireselectprice, :requiredeferredprice, :enableexcisemarkprice);'''




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
qrSelectBarcodes = 'SELECT * FROM barcodes where barcodesid = ?'


qrCalculatingTheAmount = '''UPDATE invent 
set remain  = sumItog.summItog 
FROM (
SELECT invent.inventcode, (SummIsParent.remain + invent.remain) as summItog FROM SummIsParent 
INNER JOIN
invent ON SummIsParent.isParent = invent.inventcode
) as sumItog
WHERE  invent.inventcode  = sumItog.inventcode'''
