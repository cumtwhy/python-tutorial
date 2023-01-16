# coding=utf-8
# import urllib.request
# import random
#
# def url_open(url):
#     req=urllib.request.Request(url)
#     user_agents = [
#                     'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
#                     'Opera/9.25 (Windows NT 5.1; U; en)',
#                     'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
#                     'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
#                     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
#                     'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
#                     "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
#                     "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
#
#                     ]
#
#     agent = random.choice(user_agents)
#
#     req.add_header('User-Agent',agent)
#     response=urllib.request.urlopen(url)
#     html=response.read()
#
# url="https://www.3344su.com/tupianqu/katong/268514.html"
# html=url_open(url).decode ('utf-8')
# img_addrs=[]
#
# a=html.find('img src=')
#
# while a!=-1:
#     b=html.find('.jpg',a,a +255)
#     if b!=-1:
#         img_addrs.append(html[a+9:b+4])
#     else :
#         b=a+9
#     a=html.find('img src=',b)
#
# for each in img_addrs:
#     print(each)
#
#


#
# import random
# import urllib.request
#
# proxy_list=[
#     '106.58.38.69:8118',
#     '1.161.62.107:8088',
#     '190.12.22.166:53281',
#     '14.29.92.196:80',
#     '114.99.3.113:6890',
#     '172.106.68.3:3128',
#     '36.72.193.45:8080',
#     '190.203.76.122:8080',
#     '27.254.220.2:8080',
#     '190.1.137.102:3128',
#         ]
#
#
# proxy       = random.choice(proxy_list)
# urlhandle   = urllib.request.ProxyHandler({'http':proxy})
# opener      = urllib.request.build_opener(urlhandle)
# urllib.request.install_opener(opener)
#
#
# url="http://www.67ro.com/"
# req=urllib.request.Request(url)
# req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
# response=urllib.request.urlopen(url)
# html=response.read()


# import urllib.request
#
# url="http://blog.csdn.net/beliefer/article/details/51251757"
# html=urllib.request.urlopen(url)
# print( html.read().decode('utf-8') )


import urllib.request
# import socket
# import time
import random
# timeout = 20
# socket.setdefaulttimeout(timeout)#这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置
# sleep_download_time = 10
# time.sleep(sleep_download_time) #这里时间自己设定
url = "http://www.baidu.com"
req = urllib.request.Request(url)  # 这里是要读取内容的url
req.add_header(
    'User-Agent', ' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
# req.add_header('Cookie','__jsluid=ef23d3a97e6d8b523e87d5587cde500c; _gscu_807569590=76627641noct8h81; _gscs_807569590=t76631045b9n6pp57|pv:4; _gscbrs_807569590=1')
proxy_list = ['111.56.5.42:8080', '111.56.5.41:80', '111.13.7.119:80']
proxy = random.choice(proxy_list)
urlhandle = urllib.request.ProxyHandler({'http': proxy})
opener = urllib.request.build_opener(urlhandle)
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
html = response.read()  # 读取，一般会在这里报异常
response.close()  # 记得要关闭
print(html.decode('gbk'))
