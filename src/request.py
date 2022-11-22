
import logging
import requests
import main
import json


def send_request(c_shop,server_ip,port):
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
     

