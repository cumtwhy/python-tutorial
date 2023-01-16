import urllib.request
import re
import random
import time


def open_url(url):
    num = 10
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
            # print(html.decode('utf-8'))
            return html
        except:
            if i < (num-1):
                continue
            else:
                print("Has tried %d times to access url, all failed!", i)
                break


def get_name(url):
    name = []
    html = open_url(url).decode('utf-8')
    #     addrs=re.findall(r'',html)
    st = html.find('<a href="/book/16.html" title="�������">�������</a></dd>')
    # print(st)
    a = html.find('>��', st)
    print(a)
    print('find a')
    while a != -1:
        b = html.find('</a>', a)
        if b != -1:
            name.append(html[a+1:b])
        else:
            b = a+9
        a = html.find('>��', b, a+100)
        print(a)
    for each in name:
        print(each)
    return name


def get_nurl(url):
    addrs = []
    html = open_url(url).decode('utf-8')
    #     addrs=re.findall(r'',html)
    st = html.find('<a href="/book/16.html" title="�������">�������</a></dd>')
    # print(st)
    a = html.find('<a href="', st)
    # print(a)
    while a != -1:
        b = html.find('" title="��', a, a+40)
        # print(b)
        if b != -1:
            addrs.append(html[a+9:b])
        else:
            b = a+25
        a = html.find('<a href="', b, b+100)
        # print(a)
    for i in addrs:
        print(i)
    return addrs


def get_per_txt(url):
    text = []
    txt = ""
    html = open_url(url).decode('utf-8')
    text = re.findall(r'<p>.*?</p>', html)
    for each in text:
        txt = txt+each
    # print(txt)
    return txt


def download():
    #os.mkdir (folder)
    # os.chdir(folder)
    url = "http://www.jianlaixiaoshuo.com/"
    name = get_name(url)
    ul = get_nurl(url)
    i = 0
    f = open(r'F:\Python\src\novel\����1.txt', "w", encoding='GB18030')
    f.truncate()
    f.write(name[0]+"\n"+"\n")
    for each in ul:
        url = "http://www.jianlaixiaoshuo.com"+each
        txt = get_per_txt(url)
        f.write(txt+"\n"+"\n")
        print(name[i]+"�������")
        i = i+1
        try:
            f.write(name[i]+"\n"+"\n")
        except:
            pass
    f.close()
    print("�������")


if __name__ == '__main__':
    download()
