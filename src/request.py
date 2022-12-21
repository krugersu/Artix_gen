
import logging
import requests
import main
import json
import os
import pathlib
from pathlib import Path


class req1C:
     def __init__(self, nConfig):
          self.mConfig = nConfig
          
     def __enter__(self):
          return self

     def __exit__(self):
          self.close()
          
     def exeQuery(self,c_shop):
          try:
               r = requests.get('http://' + self.mConfig._sections.one_C.server_ip + ':' 
                                   + self.mConfig._sections.one_C.port 
                                   + self.mConfig._sections.one_C.lquery)
# ?  r = requests.get('http://192.168.252.250:8082/UNF_test/hs/test_s/V1/test')
               r.encoding = 'utf-8' 
               print(r.status_code)
               c_count = r.json()
               return c_count
          except Exception as e:
               logging.exception(e, exc_info=False)
          return None
     
     
     
     
     def getQueryShop(self):
          
          try:
               r = requests.get('http://' + self.mConfig._sections.one_C.server_ip + ':' 
                                   + self.mConfig._sections.one_C.port 
                                   + self.mConfig._sections.one_C.shopquery)

               print(r.url)     
               r.encoding = 'utf-8' 
               print(r.status_code)
               c_count = r.json()
               listShop = self._getDirM(c_count)
            #   print(listShop)
               return listShop  # c_count
          except Exception as e:
               logging.exception(e, exc_info=False)
          return None     

     def shopForNumber(self,c_shop):
          
          mPar = {"number":str(c_shop)}
          print(mPar) 
          try:
               r = requests.get('http://' + self.mConfig._sections.one_C.server_ip + ':' 
                                   + self.mConfig._sections.one_C.port 
                                   + self.mConfig._sections.one_C.lquery, params=mPar)
               print(r.url)     
# ?  r = requests.get('http://192.168.252.250:8082/UNF_test/hs/test_s/V1/test_1')
               r.encoding = 'utf-8' 
               print(r.status_code)
               c_count = r.json()
            #   print(c_count)
               return c_count
          except Exception as e:
               logging.exception(e, exc_info=False)
          return None



     def _getDirM(self,listPath):
          
          listShop = []
          
          for curPath in listPath:
               curPath.replace('\\\\', '//')
               curPath = pathlib.PureWindowsPath(curPath)
               listShop.append(Path(curPath).parts[-1])
               listShop = list(set(listShop))
          return listShop
          


''' def send_request(c_shop,server_ip,port):
     # print(main.rc.get('artix','server_ip'))
     try:
         
          r = requests.get('http://' +server_ip + ':' + port + '/UNF_test/hs/test_s/V1/test')
          #r = requests.get('http://192.168.252.250:8082/UNF_test/hs/test_s/V1/test')
          r.encoding = 'utf-8' 
          print(r.status_code)
          c_count = r.json()
          #c_count = json.loads(r.text)
         # print(c_count)    
          return c_count
     except Exception as e:
          logging.exception(e, exc_info=False)
          return None
     

 '''