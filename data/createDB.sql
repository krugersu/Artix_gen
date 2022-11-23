
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;


DROP TABLE IF EXISTS additionalprices;

CREATE TABLE additionalprices (
    additionalpricesid INTEGER      PRIMARY KEY AUTOINCREMENT,
    pricecode          INTEGER (11),
    price              REAL (13, 2),
    name               TEXT (40) 
);



DROP TABLE IF EXISTS barcodes;

CREATE TABLE barcodes (
    barcodesid               INTEGER      PRIMARY KEY AUTOINCREMENT,
    additionalpricesid       INTEGER,
    aspectvaluesetcode       INTEGER (11),
    barcode                  TEXT (100),
    cquant                   REAL (13, 3),
    measurecode              INTEGER (11),
    minprice                 REAL (13, 3),
    name                     TEXT (200),
    packingmeasure           INTEGER (11),
    packingprice             REAL (15, 2),
    price                    REAL (15, 2),
    quantdefault             REAL (13, 3),
    minretailprice           REAL (13, 2),
    customsdeclarationnumber TEXT (32),
    tmctype                  INTEGER (11),
    ntin                     TEXT (255) 
);



DROP TABLE IF EXISTS invent;

CREATE TABLE invent (
    inventid                INT          PRIMARY KEY,
    inventcode              TEXT (20),
    inventgroup             TEXT (100),
    name                    TEXT (200),
    barcode                 TEXT (100),
    barcodesid              INTEGER,
    price                   REAL (13, 2),
    minprice                REAL (13, 2),
    additionalpricesid      INTEGER,
    options                 INTEGER,
    sellrestrictperiodsid   INTEGER,
    extendedoptions         TEXT,
    discautoscheme          INTEGER,
    deptcode                INTEGER,
    taxgroupcode            INTEGER,
    measurecode             INTEGER,
    remain                  REAL (13, 4),
    remaindate              DATETIME,
    articul                 TEXT (200),
    defaultquantity         REAL (13, 3),
    taramode                INTEGER (11),
    taracapacity            REAL (13, 3),
    aspectschemecode        INTEGER (11),
    aspectvaluesetcode      INTEGER (11),
    aspectusecase           INTEGER (11),
    aspectselectionrule     INTEGER (11),
    age                     INTEGER (11),
    [alcoholpercent ]       REAL (4, 2),
    cquant                  REAL (13, 3),
    inn                     TEXT (20),
    kpp                     TEXT (20),
    alctypecode             INTEGER (11),
    paymentobject           INTEGER (11),
    manufacturercountrycode INTEGER (11),
    opmode                  INTEGER (11),
    loyaltymode             INTEGER (11),
    minretailprice          REAL (13, 2),
    Parent                  BOOLEAN,
    isParent                TEXT (20) 
);



DROP TABLE IF EXISTS inventitemoptions;

CREATE TABLE inventitemoptions (
    inventitemoptionsid     INTEGER     PRIMARY KEY AUTOINCREMENT,
    disablebackinsale       INTEGER (1),
    disableinventshow       INTEGER (1),
    disableinventsale       INTEGER (1),
    disableinventback       INTEGER (1),
    requiredepartmentmanual INTEGER (1),
    enabledepartmentmanual  INTEGER (1),
    enablebarcodemanual     INTEGER (1),
    enablebarcodescanner    INTEGER (1),
    visualverify            INTEGER (1),
    ageverify               INTEGER (1),
    requiresalerestrict     INTEGER (1),
    egaisverify             INTEGER (1),
    prepackaged             INTEGER (1),
    nopdfegaisverify        INTEGER (1),
    alcoset                 INTEGER (1),
    freesale                INTEGER (1),
    rfidverify              INTEGER (1),
    lowweight               INTEGER (1),
    weightcontrolbypass     INTEGER (1),
    tobacco                 INTEGER (1),
    shoes                   INTEGER (1),
    fuzzyweight             INTEGER (1),
    ignoremarking           INTEGER (1),
    markdownverify          INTEGER (1) 
);



DROP TABLE IF EXISTS options;

CREATE TABLE options (
    optionsidid         INTEGER PRIMARY KEY AUTOINCREMENT,
    inventitemoptionsid INTEGER,
    priceoptionsid      INTEGER,
    quantityoptionsid   INTEGER,
    remainsoptionsid    INTEGER
);



DROP TABLE IF EXISTS priceoptions;

CREATE TABLE priceoptions (
    priceoptionsid        INTEGER     PRIMARY KEY AUTOINCREMENT,
    enablepricemanual     INTEGER (1),
    requirepricemanual    INTEGER (1),
    requireselectprice    INTEGER (1),
    requiredeferredprice  INTEGER (1),
    enableexcisemarkprice INTEGER (1) 
);



DROP TABLE IF EXISTS quantityoptions;

CREATE TABLE quantityoptions (
    quantityoptionsid           INTEGER      PRIMARY KEY AUTOINCREMENT,
    enabledefaultquantity       INTEGER (1),
    enablequantitylimit         INTEGER (1),
    quantitylimit               REAL (13, 3),
    enablequantityscales        INTEGER (1),
    enablequantitybarcode       INTEGER (1),
    enablequantitymanual        INTEGER (1),
    requirequantitymanual       INTEGER (1),
    requirequantitybarcode      INTEGER (1),
    requirequantityscales       INTEGER (1),
    enabledocumentquantitylimit INTEGER (1),
    autogetquantityfromscales   INTEGER (1),
    documentquantlimit          REAL (13, 3) 
);



DROP TABLE IF EXISTS remainsoptions;

CREATE TABLE remainsoptions (
    remainsoptionsid INTEGER PRIMARY KEY AUTOINCREMENT
);



DROP TABLE IF EXISTS sellrestrictperiods;

CREATE TABLE sellrestrictperiods (
    sellrestrictperiodsid INTEGER      PRIMARY KEY AUTOINCREMENT,
    dateend               DATE,
    datestart             DATE,
    dayend                INTEGER (11),
    daystart              INTEGER (11),
    timeend               TIME,
    timestart             TIME
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
