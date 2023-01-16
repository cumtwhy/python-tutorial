import urllib.request
import re
import random
import time
import socket


def open_url(url):
    headers = {
        'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    socket.setdefaulttimeout(20)
    num = 20
    for i in range(num):
        try:
            req = urllib.request.Request(url, headers=headers)
            time.sleep(random.uniform(0, 2))
            res = urllib.request.urlopen(req)
            time.sleep(random.uniform(1, 3))
            html = res.read()
            res.close()
            #print(html.decode('GB18030') )
            return html
        except:
            if i < (num-1):
                continue
            else:
                print(r"Has tried %d times to access url, all failed! " % (num))
                break


def get_infromation(url):
    html = open_url(url).decode('GBK')
    name = re.findall(r'href=\"\d{1,10}.*?>(.*)?</a>', html)
    per_url = re.findall(r'(?<=href=\")\d{1,10}.html(?=\">)', html)
    return (name, per_url)


def get_per_txt(url):
    print(url)
    html = open_url(url).decode("GBK")
    reg = re.compile(r'(?<= id=\"content\">).*?(?=</div>)', re.S)
    text = re.findall(reg, html)
    txt = "".join(text)
    txt = txt.replace('&nbsp;', '')
    return txt


def download():
    url = input("������С˵�ڱ�Ȥ��ĵ�ַ��")  # https://www.23wxw.cc/html/947/
    novel_name = input("������С˵�����֣�")
    (name, per_url_list) = get_infromation(url)
    i = 0
    f = open(r'./%s.txt' % novel_name, "w")
    # f=open(r'F:\Python\src\novel\123.txt',"w",encoding='GB18030')
    f.truncate()  # clear
    f.write(name[i]+"\n")
    f.flush()
    for each in per_url_list:
        per_url = url+each
        txt = get_per_txt(per_url)
        f.write(txt+"\n"+"\n")
        print(name[i]+"    ������ɣ�")
        f.flush()
        i = i+1
        try:
            f.write(name[i]+"\n"+"\n")
        except:
            pass
    f.close()
    print("�������!")


if __name__ == '__main__':
    download()
