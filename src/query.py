curVal = ''
addinvent = ''
#qrAddPriceoptions = f"""INSERT INTO priceoptions (priceoptionsid, enablepricemanual, requirepricemanual, requireselectprice, requiredeferredprice,enableexcisemarkprice) VALUES {curVal}"""
qrAddPriceoptions = 'INSERT INTO priceoptions VALUES (?, ?, ?, ?, ?,?);'

qrAddinventitemoptions = 'INSERT INTO inventitemoptions VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'