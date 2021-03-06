# 分析服务器发送来的PORT信息，和服务器的port建立数据连接。
# !/usr/bin/python3
# -*- coding: utf-8 -*-
import ftplib
import os
import socket
import sys
import json
import time

HOST = '125.62.27.92'
DIRN = '/'
FILE = 'put.txt'
host1 = '11.25.45.26'
port1 = 15245


def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror):
        print('ERROR:cannot reach " %s"' % HOST)
        return
    print('*** Connected to host "%s"' % HOST)

    try:
        f.login('mgtv', 'mgtv123456')
    except ftplib.error_perm:
        print('ERROR: cannot login FTP')
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
        str1 = f.sendcmd('PASV')

        print(str1)
        str2 = str1.split(',')
        print("str2")
        print(str2)
        print(str2[4])
        str3 = str2[5].split(')')
        print(str3)
        print(str3[0])
        port = int(str2[4]) * 256 + int(str3[0])
        print(port)

    except ftplib.error_perm:
        print('ERROR:error with putcmd')
        f.quit()
        return
    print('***putcmd successfully')

    # To establish a TCP connection
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print('Failed to create socket.Error code:' + str(msg[0]) + ',Error message' + msg[1])
        sys.exit()
    print('Socket Create')

    s.connect((HOST, port))
    print('Socket connect!')
    print(f.sendcmd('LIST'))
    print(s.recv(1024))
    # f.retrlines('DIR')
    # print(s.recv(1024))
    # file_handler = open('1.ts', 'wb').write

    # f.retrbinary('RETR 1.ts', file_handler)
    # s.send('1.ts'.encode('utf-8'))

    while True:
        filename = input(">>:").strip().encode("utf-8")
        s.send(filename)
        # s_size = int(s.recv(1024).decode())
        s_size = len(s.recv(1024))
        recive_size = 0
        date = ""
        while recive_size < s_size:
            date += date
            date = s.recv(1024).decode("utf-8")
            recive_size += len(date)
        print(s_size, recive_size)
        print(date)
    '''count = 0
    with open("[new]1.ts", "wb") as file:
        while count < 10:
            print("count",count)

            data = s.recv(1024)
            print(len(data))
            file.write(data)
            count += 1
            time.sleep(0.5)
    '''

    # print(f.retrlines('LIST'))
    # print(s.recv(1024))
    # get file from ftp and print in screen
    # print(f.sendcmd('RETR 1.ts'))     　　　　　
    # print(s.recv(1024))  　　
    # s.close()
    '''s.send('1.ts'.encode('utf-8'))
    ts_header = s.recv(500)
    header = json.loads(ts_header.decode('utf-8'))
    #filename = header['filename']
    filesize = header['size']
    file = open('1.ts', 'wb')
    recvsize = 0
    while recvsize < filesize:
        if filesize - recvsize < 1024:
            data = s.recv(filesize - recvsize)
        else:
            data = s.recv(1024)
        recvsize += len(data)
        file.write(data)
    else:
        file.close()
    '''
    print('translate successfully!')

    f.quit()
    return


if __name__ == '__main__':
    main()

# filename = '1.ts'
# bufsize = 1024
# file_handler = open('1.ts', 'wb').write  # 以写模式在本地打开文件
# f.retrbinary('RETR %s' % filename, file_handler, bufsize)
