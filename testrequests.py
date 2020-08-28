import requests
import pycurl
import os

ftpurl = 'ftp://mgtv:mgtv123456@125.62.27.92/1.ts'
weburl = 'http://192.168.18.251:83'
pos = 0

#f = open('1.ts', 'wb')

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return  r.text
        #"gbk"
    except:
        return "error！！！"

def getFTPfile(url):
    #response = StringIO.StringIO()
    os.makedirs('files')
    os.chdir('files')
    f = open('1.ts', 'wb')
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.NOPROGRESS, 0)
    #c.setopt(c.WRITEFUNCTION, f.write)
    c.setopt(c.WRITEDATA, f)
    #c.setopt(c.HTTPHEADER, ['Content-Type: application/json', 'Accept-Charset: UTF-8'])
    #c.setopt(c.POSTFIELDS, '@request.json')
    c.perform()
    c.close()

if __name__ == "__main__":
    if pos == 0:
        getFTPfile(ftpurl)
    else:
        print(getHTMLText(weburl))