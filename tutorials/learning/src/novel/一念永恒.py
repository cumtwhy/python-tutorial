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
                print("��"+str(url)+"��ҳʧ�ܣ�����ʮ����Ч")
                break


def get_name(url):
    html = open_url(url).decode('GB18030')
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
    html = open_url(url).decode('GB18030')
    a = re.findall(
        r'(?<=href=\").*?html(?=\")|(?<=href=\').*?html(?=\')', html)
    a2 = list(set(a))  # distinct
    adds = sort_strings_with_emb_numbers(a2)
    for i in adds:
        print(i)
    return adds


def get_per_txt(url):
    html = open_url(url).decode("GB18030")
    text = re.findall(r'(?<= class=\"showtxt\">).*?(?=</div>)', html)
    txt = "".join(text)
    txt = txt.replace('&nbsp;', '')
    txt = txt.replace('<br /><br />', '<br/>')
    return txt


def download():
    #os.mkdir (folder)
    # os.chdir(folder)
    url = "http://www.biqukan.com/1_1094/"
    name = get_name(url)
    ul = get_nurl(url)
    i = 13
    f = open(r'F:\Python\src\novel\һ������1.txt', "w", encoding='GB18030')
    f.truncate()  # clear
    f.write(name[i]+"\n"+"\n")

    # for contune
    # ul=ul[1109+18+10:]
    for each in ul:
        url = "http://www.biqukan.com"+each
        txt = get_per_txt(url)
        f.write(txt+"\n"+"\n")
        print(name[i]+"    �������")
        i = i+1
        try:
            f.write(name[i]+"\n"+"\n")
        except:
            pass
    f.close()
    print("������ɣ�!")


if __name__ == '__main__':
    download()
