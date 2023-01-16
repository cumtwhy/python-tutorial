# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup


url = 'http://www.bjyj.gov.cn/flfg/bs/ggws/t1244662.html'

try:
    req = urllib.request.Request(url)
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
    req.add_header('Connection', 'keep-alive')
    req.add_header('Referer', 'http://www.bjyj.gov.cn/flfg/bs/')
    req.add_header('Accept-Language', 'zh-CN,zh;q=0.8')
    req.add_header(
        'Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    req.add_header('Accept-Encoding', 'gzip, deflate, sdch')
    req.add_header('Cookie', '__jsluid=ef23d3a97e6d8b523e87d5587cde500c; _gscu_807569590=76627641noct8h81; _gscs_807569590=t76631045b9n6pp57|pv:4; _gscbrs_807569590=1')
    req.add_header('If-None-Match', '"7519-53913419503c0"')
    req.add_header('Cache-Control', 'max-age=0')
    req.add_header('Host', 'http://www.bjyj.gov.cn/')
    req.add_header('Upgrade-Insecure-Requests', '1')
    req.add_header('If-Modified-Since', 'Tue, 02 Aug 2016 09:22:31 GMT')
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')

    print(soup)
except urllib.request.HTTPError as h:
    print(h.code)
    print(h.headers)
