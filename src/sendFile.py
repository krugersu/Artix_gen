
#import paramiko
import time
import shutil


host = '192.168.0.239'
user = 'administrator'
secret = 'adm@#747911ART'
port = 22



def sendFile(fileName,shopNumber,typeFile):
    
    nameFileDest = 'pos'
    # ssh = paramiko.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect(host, username=user, password=secret,timeout=4)
    # time.sleep(1)
    # ssh.connect('127.0.0.1', username='bat', 
    #     password='Uytplj12')
    # stdin, stdout, stderr =ssh.exec_command("uptime")
    # time.sleep(1)
    # stdout.readlines()
  #  ftp = ssh.open_sftp()
    if typeFile:
        #ftp.put(fileName, '/opt/OBMEN/dict/'+ shopNumber +'/' + 'pos'+ shopNumber+'.aif')
        #ftp.put('./upload/'+fileName.name, '/opt/OBMEN/dict/'+ shopNumber +'/' + 'pos'+ shopNumber+'.aif')
        shutil.copyfile('./upload/'+fileName.name, '/mnt/share/'+ shopNumber +'/' + 'pos'+ shopNumber+'.aif')
     #   time.sleep(5)
      #  print(fileName)
      #  print(shopNumber)
        print('Upload finished_1')
    else:    
        #ftp.put(fileName, '/opt/OBMEN/dict/'+ shopNumber +'/' + 'pos'+ shopNumber+'.flz')
     #   shutil.copyfile('./upload/'+fileName.name, '/mnt/share/'+ shopNumber +'/' + 'pos'+ shopNumber+'.flz')
     #   time.sleep(5)
        print('Upload finished_2')
    # ftp.close()
    # ssh.close()
    