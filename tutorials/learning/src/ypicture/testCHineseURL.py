# coding=UTF-8
import urllib.request
import re
import random
import time
import socket
import os
import urllib.parse


def open_url(url):
    num = 20
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
            # print(html.decode('UTF-8'))
            return html
        except:
            if i < (num-1):
                continue
            else:
                print("Has tried %d times to access url, all failed!", num)
                break




def get_addrs(url):
    html = open_url(url).decode('utf-8')
    # a=re.findall(r'http://[\w/]+?\d{3,6}.jpg',html)
    pic = re.findall(r'(?<=img src=\").*?jpg(?=\")', html)
    # ===========================================================================
    # for each in a:
    #     print(each)
    # ===========================================================================
    return pic


def get_name(url):
    html = open_url(url).decode('utf-8')
    # a=re.findall(r'http://[\w/]+?\d{3,6}.jpg',html)
    name = re.findall(r'(?<=<date>).*?(?=</date>)', html)
    # ===========================================================================
    # for each in a:
    #     print(each)
    # ===========================================================================
    return name


def save_pic(folder, pic, name):
    for index in range(len(pic)):
        print(pic[index])
        print(name[2*index-1])
        filename = name[2*index]
        if not os.path.exists(filename):
            with open(filename, 'wb') as f:
                img = open_url(pic[index])
                f.write(img)
                print("OK")
        else:
            print("This picture is exist!")

            #===================================================================
            # if not os.path.exists(filename):
            #     f.write(img)
            #     print("OK")
            # else:
            #     print("This picture is exist!")
            #     pass
            # ===================================================================


def download(folder="search"):
    #     os.mkdir(folder)
    #     os.chdir(folder)
    if not os.path.exists(folder):
        os.mkdir(folder)
        os.chdir(folder)
    else:
        os.chdir(folder)

    print(1)
    search="search/"+urllib.parse.quote("人妻")


    url="https://www.javbus.com/"+search+str(1)
    print (url)
    pic=get_addrs(url)
    print(pic)
    name = get_name(url)
    print(name)
    print(2)
    save_pic(folder, pic, name)
    print(3)



if __name__=='__main__':
    download()

