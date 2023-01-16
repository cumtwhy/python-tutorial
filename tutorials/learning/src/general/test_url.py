#code=gbk
import urllib.request;
import re
import random
import time
import imp
import urllib.parse

def open_url(url):
    num=10
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Mobile Safari/537.36'}
       
    req=urllib.request.Request(url,headers=headers)
    time.sleep(random.uniform(0,2))
    res=urllib.request.urlopen(req)
    time.sleep(random.uniform(0,2))
    html=res.read()
    res.close()
    print(html)
    #print(html.decode('UTF-8'))
    return html
        
        
if __name__=='__main__':
    #search="search/"+urllib.parse.quote("人妻")###########Chinese url
    url="https://www.biqudu.com/0_374/"
    open_url(url)
    #html=open_url(url).decode("UTF-8")
    #print(html)
    #replace()
