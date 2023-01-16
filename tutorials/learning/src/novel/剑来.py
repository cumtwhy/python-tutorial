# coding=UTF-8
import urllib.request
import re
import random
import time
import socket


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
                print("Has tried %d times to access url, all failed!", i)
                break


def get_name(url):
    html = open_url(url).decode('UTF-8')
    name = re.findall(r'(?<=html\">).*?(?=<)', html)
    for each in name:
        print(each)
    return name


# sorted by embnumber
re_digits = re.compile(r'(\d+)')


def emb_numbers(s):
    pieces = re_digits.split(s)
    pieces[1::2] = map(int, pieces[1::2])
    return pieces


def sort_strings_with_emb_numbers(alist):
    return sorted(alist, key=emb_numbers)


def get_nurl(url):
    html = open_url(url).decode('UTF-8')
    a = re.findall(
        r'(?<=href=\").*?html(?=\")|(?<=href=\').*?html(?=\')', html)
    a2 = list(set(a))  # distinct
    adds = sort_strings_with_emb_numbers(a2)
    for i in adds:
        print(i)
    return adds


def get_per_txt(url):
    html = open_url(url).decode("UTF-8")
    text = re.findall(r'(?<= id=\"content\">).*?(?=</div>)', html)
    txt = "".join(text)
    txt = txt.replace('&nbsp;', '')
    return txt


def download():
    #os.mkdir (folder)
    # os.chdir(folder)
    url = "http://www.biqu6.com/7_7021/"
    name = get_name(url)
    ul = get_nurl(url)
    i = 9
    f = open(r'F:\Python\src\novel\剑来.txt', "w", encoding='UTF-8')
    f.truncate()  # clear
    f.write(name[i]+"\n"+"\n")
    for each in ul:
        url = "http://www.biqu6.com"+each
        txt = get_per_txt(url)
        f.write(txt+"\n"+"\n")
        print(name[i]+"    下载完成")
        i = i+1
        try:
            f.write(name[i]+"\n"+"\n")
        except:
            pass
    f.close()
    print("完成下载！")


if __name__ == '__main__':
    download()
