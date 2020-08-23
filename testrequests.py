import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return  r.text
        #"gbk"
    except:
        return "error！！！"

if __name__ == "__main__":
    #url = "http://192.168.18.251:83"
    url = "175.6.15.136"
    print(getHTMLText(url))