# coding=gbk
import urllib.request;
import re
import os
import random
import socket
import time


def open_url(url):
    headers = {
        'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    socket.setdefaulttimeout(20)
    num = 10
    for i in range(num):
        try:
            req = urllib.request.Request(url, headers=headers)
            time.sleep(random.uniform(0, 2))
            res = urllib.request.urlopen(req)
            time.sleep(random.uniform(1, 3))
            html = res.read()
            res.close()
            #print(html.decode('utf-8') )
            return html
        except:
            if i < (num-1):
                continue
            else:
                print("��"+str(url)+"��ҳʧ�ܣ�����ʮ����Ч")
                break


def get_pages(url):
    html = open_url(url).decode('utf-8')
    a = re.findall(r'\/tupianqu[\w\/]+?\d{6}\.html', html)
    # ===========================================================================
    # for each in a:
    #     print(each)
    # ===========================================================================
    return a


def get_addrs(url):
    html = open_url(url).decode('utf-8')
    # a=re.findall(r'http://[\w/]+?\d{3,6}.jpg',html)
    a = re.findall(r'http://c[\w/.]+?\d{2,7}.jpg', html)
    # ===========================================================================
    # for each in a:
    #     print(each)
    # ===========================================================================
    return a


def save_pic(folder, a):
    for each in a:
        print(each)
        filename = each.split('/')[-1]
        if not os.path.exists(filename):
            with open(filename, 'wb') as f:
                img = open_url(each)
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


def download(URL, folder="yellow1"):
    #     os.mkdir(folder)
    #     os.chdir(folder)
    if not os.path.exists(folder):
        os.mkdir(folder)
        os.chdir(folder)
    else:
        os.chdir(folder)

    pageurl=get_pages(URL)
    for each in pageurl:
        try:
            url="url"+each
            print (url)
            print(1)
            addrs = get_addrs(url)
            print(2)
            save_pic(folder, addrs)
            print(3)
        except:
            pass


if __name__=='__main__':
    for i in range(10):
        try:
            url="url"+str(i+17)+".html"
            download(url)
        except:
            pass

