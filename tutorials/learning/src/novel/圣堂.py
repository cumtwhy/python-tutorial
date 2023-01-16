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


def get_information(url):
    html = open_url(url).decode('UTF-8')
    a = html.find('正文</dt>')
    html = html[a:]
    reg = re.compile(r'(?<=href=\"\/).*?(?=\")', re.S)
    per_url = re.findall(reg, html)
    names = re.findall(r'\d{1,10}.html\"?>(.*)?</a>', html)
    return (names, per_url)


def get_per_txt(url):
    html = open_url(url).decode("UTF-8")
    reg = re.compile(r'(?<=<script>readx\(\);<\/script>).*?(?=<script>)', re.S)
    text = re.findall(reg, html)
    txt = "".join(text)
    return txt


def download():
    URL = input("请输入小说在笔去读的网址：")  # url="https://www.biqudu.com/0_374/"
    (names, per_url) = get_information(URL)
    i = 0
    f = open(r'./圣堂.txt', "w", encoding='UTF-8')
    f.truncate()  # clear
    f.write(names[i]+"\n"+"\n")
    for each in per_url:
        url = "https://www.biqudu.com/"+each
        txt = get_per_txt(url)
        f.write(txt+"\n"+"\n")
        print(names[i]+"\t下载完成")
        i = i+1
        try:
            f.write(names[i]+"\n"+"\n")
        except:
            pass
    f.close()

    introduce = "\t你下载的小说已经完成！一共%d章！\n" % len(per_url)
    print(introduce)
    with open("./@Introduction.txt", 'a+') as f:
        f.write(introduce)
        f.close()
    print("完成下载！")


if __name__ == '__main__':
    download()
