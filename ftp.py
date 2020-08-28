import ftplib
ftp = ftplib.FTP()                         #设置变量
ftp.set_debuglevel(2)             #打开调试级别2，显示详细信息
ftp.connect('125.62.27.92', 21)          #连接的ftp sever和端口
ftp.login("mgtv", "mgtv123456")      #连接的用户名，密码
print(ftp.getwelcome())
#ftp.set_pasv(1)
ftp.sendcmd('PASV')
#print(ftp.dir('/'))
pwd_path = ftp.pwd()
ftp.sendcmd('LIST')
#ftp.set_pasv(False)
ftp.encoding = "utf-8"
filename = '1.ts'
bufsize = 1024
file_handler = open('1.ts', 'wb').write  #以写模式在本地打开文件
ftp.sendcmd('RETR %s' % filename)

#ftp.retrbinary('RETR %s' % filename, file_handler, bufsize)
ftp.quit()
print("ftp down OK")



'''print("FTP当前路径:", pwd_path)
allFileName = ftp.nlst()
for lists in allFileName:
    print(lists)
#ftp.sendcmd('LIST')
#files = ftp.nlst()
#for file in files:
  #fp = open(file, 'wb')
  #print(file)
  #ftps.retrbinary('RETR %s' % file, fp.write)
 #ftps.close()
#ftp.quit()
'''
