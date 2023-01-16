
import urllib.request
import os
import random
import time
import socket


def url_open(url):
    socket.setdefaulttimeout(20)
    req = urllib.request.Request(url)
    req.add_header(
        'User-Agent', ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393')
#     proxy_list=[
# #     '1.161.62.107:8088',
#     '190.12.22.166:53281',
#     '14.29.92.196:80',
#     '114.99.3.113:6890',
#     '172.106.68.3:3128',
#     '36.72.193.45:8080',
#     '190.203.76.122:8080',
#     '27.254.220.2:8080',
#     '190.1.137.102:3128'
# #       '104.17.19.92:443'
#         ]

    proxy_list = ['54.187.52.159:8080',
                  '185.89.217.56:50020', '111.13.7.119:80']
    proxy = random.choice(proxy_list)
    urlhandle = urllib.request.ProxyHandler({'https': proxy})
    opener = urllib.request.build_opener(urlhandle)
    urllib.request.install_opener(opener)

    print(1)
    time.sleep(10)
    response = urllib.request.urlopen(url)
    print(response.code())
    html = response.read()
#     print()
    response.close()
    print(1)
    return html


def find_imgs(picture_url):
    html = url_open(picture_url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg', a, a + 255)
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a+9
        a = html.find('img src=', b)

    for each in img_addrs:
        print(each)

    return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)


def download_yp(folder='yellow', pages=10):
    if not os.path.exists(folder):
        os.mkdir(folder)
        os.chdir(folder)
    else:
        os.chdir(folder)

    url = "https://www.3344sa.com/tupianqu/katong/"
    page_num = int(268514)

    for i in range(pages):
        page_num
        page_num += 1
        print(i)
        page_url = url+str(page_num)+'.html'
        print(page_url)
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)


if __name__ == '__main__':
    download_yp()
