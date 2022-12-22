#/usr/bin/env python3.11
"""Example Python program with Sphinx style comments.
Description
-----------
Example Python program with Sphinx style (reStructuredText) comments.
Libraries/Modules
-----------------
- time standard library (https://docs.python.org/3/library/time.html)
    - Access to sleep function.
- sensors module (local)
    - Access to Sensor and TempSensor classes.
Notes
-----
- Comments are Sphinx (reStructuredText) compatible.
TODO
----
- None.
Author(s)
---------
- Created by John Woolsey on 05/27/2020.
- Modified by John Woolsey on 07/02/2020.
Copyright (c) 2020 Woolsey Workshop.  All rights reserved.
Members
-------
"""
# Imports
import os
import sys
import configparser
import m_config
from requests.exceptions import HTTPError
import schedule, time
import file_wr, request
import app_logger
import db
import pathlib
from pathlib import Path 
import workDB
import tlgrm
import create_aif

#: Global Constants
logger = app_logger.get_logger(__name__)
"""Для логирования событий"""




# TODO Чтение файла конфигурации в попытку
# ! Посмотреть как работает sqlite с json https://habr.com/ru/post/528882/
# ! Подумать о хранении таблиц БД в памяти
# ! Что делать если таблица рухнет в процессе расчета?


# Functions
def main():
   """ Main program entry. """
   
   path = Path("config", "config.ini") 
   
   logger.info("Start programs")
   f = '*flg'
   #tlgrm.send_telegram("Start programs")
   
   catalog = rc._sections.one_C.cat_skl
   
   
   #c_shop = file_wr.find_change(catalog, f)
   #c_shop = []
   # Apoc по магазинам с изменения
   
   mCount = request.req1C(rc)
   # Анализ в каких магазинах изменения
   c_shop = mCount.getQueryShop()
   #print(c_shop)
   # Обработка данных по магазинам
   for curShop in c_shop:
   #   print(curShop)    
      c_count = mCount.shopForNumber(curShop)
      if not c_count == None:  
         tData = db.workDb(rc)
         tData.uploadData(c_count, curShop)

   logger.info(u'End programs')   




#schedule.every(10).seconds.do(job1, p='Через 10 секунд')



if __name__ == "__main__":

   # schedule.every(1).minutes.do(main)
   m_conf = m_config.m_Config()   
   rc =  m_conf.loadConfig()
   if not rc == None:
      main()
   else:
      logger.info(u'Программа завершила работу')                                      
      
   #while True:
   #    schedule.run_pending()
   #    time.sleep(1)
