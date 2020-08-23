#分析服务器发送来的PORT信息，和服务器的port建立数据连接。
#!/usr/bin/python
# -*- coding: utf-8 -*-
import ftplib
import os
import socket
import sys

HOST = '125.62.27.92'
DIRN = '/'
FILE = 'put.txt'
host1 = '11.25.45.26'
port1 = 15245


def main():
    try:
         f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror):
        print('ERROR:cannot reach " %s"' %HOST)
        return
    print('*** Connected to host "%s"' %HOST)

    try:
        f.login('mgtv', 'mgtv123456')
    except ftplib.error_perm:
        print('ERROR: cannot login FTP' )
        f.quit()
        return
    print('*** Logged in as "FTP"')
    print(f.getwelcome())

    try:
        f.sendcmd('SYST')
        f.sendcmd('PWD')
        f.sendcmd('CWD /')
        f.sendcmd('PWD')
        f.sendcmd('TYPE I')
        str1= f.sendcmd('PASV')

        print(str1)
        str2=str1.split(',')
        print("str2")
        print(str2)
        print(str2[4])
        str3=str2[5].split(')')
        print(str3)
        print(str3[0])
        port = int(str2[4])*256+int(str3[0])
        print(port)

    except ftplib.error_perm:
        print('ERROR:error with putcmd')
        f.quit()
        return
    print('***putcmd successfully')

     #To establish a TCP connection
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print('Failed to create socket.Error code:'+str(msg[0])+',Error message'+msg[1])
        sys.exit()
    print('Socket Create')

    s.connect((HOST,port))
    print('Socket connect!')
    print(f.sendcmd('LIST'))
    print(s.recv(10240))

    #print(f.retrlines('LIST'))
    #get file from ftp and print in screen
    #print f.sendcmd('RETR wordless10m.docx')    　　　　　
    # #print s.recv(1024)    　　　　
    #print 'translate successfully!'

    f.quit()
    return
if __name__ == '__main__':
     main()