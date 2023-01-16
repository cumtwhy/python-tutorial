# code='utf-8'
import urllib.request
import os  # 鍙互鍐嶅綋鍓嶇洰褰曚笅鐢熸垚涓�釜鏂囦欢澶�
import random


def url_open(url):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)

    # proxy_list=['111.56.5.42:8080','111.56.5.41:80','111.13.7.119:80' ]
    # proxy= random.choice(proxy_list)
    # urlhandle= urllib.request.ProxyHandler({'http':proxy})
    # opener= urllib.request.build_opener(urlhandle)
    # urllib.request.install_opener(opener)

    # ===========================================================================
    #
    # response=urllib.request.urlopen(url)
    # html=response.read()
    # ===========================================================================
    html = urllib.request.urlopen(req).read()
    print(html)
    return html


def get_pages(url):
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']', a)

    return html[a:b]
    #print (html[a:b])


def find_imgs(pages_url):
    # url="http://jandan.net/ooxx/"
    html = url_open(pages_url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg', a, a + 255)
        if b != -1:
            img_addrs.append('http:'+html[a+9:b+4])
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


def download_mm(folder='yellow', pages=1):
    #     os.mkdir (folder)
    #     os.chdir(folder)

    url = "http://jandan.net/ooxx/"
    pages_num = int(get_pages(url))

    for i in range(pages):
        try:
            pages_num -= 1
            print(i)
            pages_url = url+'page-'+str(pages_num)+'#comments'
            print(pages_url)
            img_addrs = find_imgs(pages_url)
            save_imgs(folder, img_addrs)
        except:
            pass


if __name__ == '__main__':
    download_mm()
