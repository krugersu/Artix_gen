// Собрали продажи по позициям которые пришли из 1С
SELECT * FROM CountSummAnalog 
inner JOIN (SELECT code , opcode , SUM(cquant)  FROM goodsitem  
Group by code) as st
ON st.code  = CountSummAnalog.inventcode 