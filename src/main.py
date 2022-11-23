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


logger = app_logger.get_logger(__name__)
# TODO Читать настройки в класс
# TODO Чтение файла конфигурации в попытку



def main():

   
   path = Path("config", "config.ini") 
   #path = './config/config.ini'
  # db.testdb()

   logger.info("Программа стартует")
   f = '*flg'
   #print(rc._sections.one_C.cat_skl)
   
   catalog = rc._sections.one_C.cat_skl
   server_ip = rc._sections.one_C.server_ip
   port = rc._sections.one_C.port
   
   # Анализ в каких магазинах изменения
   c_shop = file_wr.find_change(catalog, f)
   # Запрос по магазинам с изменениями
   
   c_count = request.send_request(c_shop,str(server_ip),str(port))
  # print(c_shop)
   
   
   db.saveDataDB(c_count)
   #logging.info('Finished')
   logger.info(u'Программа завершила работу')   




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
