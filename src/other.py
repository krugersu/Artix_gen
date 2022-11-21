  print(rc.get('artix','server_ip'))
    r = requests.get('http://192.168.252.250:8082/UNF_test/hs/test_s/V1/test')
    r.encoding = 'utf-8' 
    print(r.status_code)
    #print(r.json())    
    print(r.text)    




