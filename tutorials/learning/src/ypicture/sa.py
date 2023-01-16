code='utf-8'
import urllib.request;
import random;
import os;
import urllib.error
import time
import socket
import re


def open_url(url):
    num = 10
    socket.setdefaulttimeout(20)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Mobile Safari/537.36'}
    for i in range(num):
        try:
            req = urllib.request.Request(url, headers=headers)
            time.sleep(random.uniform(0, 2))
            res = urllib.request.urlopen(req)
            time.sleep(random.uniform(0, 2))
            html = res.read()
            res.close()
            return html
        except:
            if i < (num-1):
                continue
            else:
                print(r"Has tried %d times to access url, all failed! " % (num))
                introduce = "没有图片: "+url
                print(introduce)
                with open("../@Introduction.txt", 'a+') as f:
                    f.write(introduce)
                # break
                continue
    return html

def get_pages(url):
    print(url)
    haddrs = []
    html = open_url(url).decode('utf-8')
    haddrs = re.findall(r'knstz_\d{6}.html', html)
    for i in range(0, len(haddrs)):
        haddrs[i]='url'+haddrs[i]
    return haddrs


def per_pictureadds(url):
    per_pictureadds=[]
    html=open_url(url).decode('utf-8')
    per_pictureadds=re.findall(r'(?<=img src=\").*?jpg(?=\")',html)
    return per_pictureadds

def save_pic(folder,img_addrs):
    for each in img_addrs:
        print(each)
        filename = each.split('/')[-1]
        if not os.path.exists(filename):
            with open(filename, 'wb') as f:
                try:
                    img = open_url(each)
                    f.write(img)
                    print("OK")
                except:
                    print("fail")
                    continue
        else:
            print("This picture is exist!")


def download_mm(folder='yellow'):
    if not os.path.exists("yellow"):
        os.mkdir("yellow")
        os.chdir("yellow")
    else:
        os.chdir("yellow")

    url="url"
    try:
        hurl = get_pages(url)
        for each in hurl:
            print(each)
            picaddrs=per_pictureadds(each)
            save_pic(folder,picaddrs)
    except urllib.error.URLError as e:
        print(e.reason)

if __name__=='__main__':
    download_mm()
