# coding=UTF-8
import urllib.request
import re
import random
import time
import socket
import os
import urllib.parse


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
            # print(html.decode('UTF-8'))
            return html
        except:
            if i < (num-1):
                continue
            else:
                print(r"Has tried %d times to access url, all failed! " % (num))
                introduce = "\t你搜索的您要的内容没有相关的内容！\n"
                print(introduce)
                with open("../@Introduction.txt", 'a+') as f:
                    f.write(introduce)
                break


def get_information(url):
    html = open_url(url).decode('utf-8')
    name = re.findall(r'(?<=<date>).*?(?=</date>)', html)  # 后面处理了
    pic = re.findall(r'(?<=img src=\").*?jpg(?=\")', html)
    has_next = html.find(r'next')
    return (name, pic, has_next)


def save_pic(pic, name):
    for index in range(len(pic)):
        print(pic[index])
        print(name[2*index])
        filename = name[2*index]+".jpg"
        if not os.path.exists(filename):
            with open(filename, 'wb') as f:
                img = open_url(pic[index])
                f.write(img)
                print("OK")
        else:
            print("This picture is exist!")


def download():
    # print(1)
    target = input("请输入要搜索的内容：")
    search = "search/"+urllib.parse.quote(target)
    if not os.path.exists(target):
        os.mkdir(target)
        os.chdir(target)
    else:
        os.chdir(target)

    url="url"+search
    i=1
    print (url)
    try:
        (name,pic,has_next)=get_information(url)
        while has_next!=-1:
            #print(2)
            save_pic(pic,name)
            #print(3)
            i=i+1
            url="url/"+search+"/"+str(i)
            print(url)
            (name, pic, has_next) = get_information(url)
            if has_next == -1:
                save_pic(pic, name)
        introduce = "\t你搜索的"+target+"下载完成！一共"+str(i)+"个pages!\n"
        print(introduce)
        with open("../@Introduction.txt", 'a+') as f:
            f.write(introduce)
    except:
        pass


if __name__=='__main__':
    download()

