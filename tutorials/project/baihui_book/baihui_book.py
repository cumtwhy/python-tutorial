import requests
import re
from lxml import etree
import pymysql
import random
import time
import xlwt
import os
from smtplib import SMTP, SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from apscheduler.schedulers.background import BlockingScheduler

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}


def get_response_html(url):
    num = 10
    for i in range(num):
        try:
            response_html = requests.get(url=url, headers=headers).text
            time.sleep(random.uniform(0, 2))
            return response_html
        except Exception:
            if i < (num - 1):
                continue
            else:
                print(r"Has tried 10 times to access url, all failed!")
                continue


# 获取所有要爬的 URL 路径:
def init_type_urls(url):
    response_html = get_response_html(url)
    selector = etree.HTML(response_html)
    book_type_urls = selector.xpath(
        '//ul[@class="navigation"]//li//ul//li//a/@href')
    return book_type_urls


def get_book_type_urls_pages(url):
    response_html = get_response_html(url)
    return re.findall(r'(?<=<div><b>总计).*?(?=页)', response_html)


def get_xpath_data(url):
    response_html = get_response_html(url)
    selector = etree.HTML(response_html)
    book_name = selector.xpath('//div[@class="mysw"]//h1/text()')
    book_pages = re.findall(r'(?<=h2>页数：).*(?=</)', response_html)
    book_size = re.findall(r'(?<=h2>开本：).*(?=开</)', response_html)
    book_weight = re.findall(r'(?<=h2>商品重量：).*(?=克</)', response_html)
    book_price = selector.xpath('//div[@class="s1"]//h2//font[2]/text()')
    book_origin_price = re.findall(r'(?<=class=\"bookprice\" style=\"color:#e80e18;\">).*(?=<\/font><\/h2><\/div>)',
                                   response_html)
    book_image_url = selector.xpath('//img[@class="simg"]/@src')
    book_publisher = re.findall(r'(?<=h2>出版社：).*(?=</)', response_html)
    '''  不同书籍的种类
    lei: 187  青少课外名著类
    lei: 181  幼儿教育启蒙类
    lei: 188  青春言情小说类
    lei: 184  孕产育儿家教类
    + lei: 199  字词典工具书类
    + lei: 186  生活养生保健类
    + lei: 185  经营管理励志类
    + lei: 183  社科文学哲理类
    + lei: 182  作文课外辅导类
    + lei: 179  59元大全集（满40本厂家发货）
    + lei: 178  1---2元特价区
    + lei: 177  精装套盒12套一箱厂家发货
    + lei: 202  红星图书系列
    + lei: 201  8.5常春藤（满28本/箱厂家代发）
    + lei: 198  精品字帖 1.5元系列
    + lei: 191  百汇图书精品专区
    '''
    if "lei=187" in url:
        book_type = "青少课外名著类"
    elif "lei=181" in url:
        book_type = "幼儿教育启蒙类"
    elif "lei=188" in url:
        book_type = "青春言情小说类"
    elif "lei=184" in url:
        book_type = "孕产育儿家教类"
    elif "lei=199" in url:
        book_type = "字词典工具书类"
    elif "lei=186" in url:
        book_type = "生活养生保健类"
    elif "lei=185" in url:
        book_type = "经营管理励志类"
    elif "lei=183" in url:
        book_type = "社科文学哲理类"
    elif "lei=182" in url:
        book_type = "作文课外辅导类"
    elif "lei=179" in url:
        book_type = "59元大全集（满40本厂家发货）"
    elif "lei=178" in url:
        book_type = "1---2元特价区"
    elif "lei=177" in url:
        book_type = "精装套盒12套一箱厂家发货"
    elif "lei=202" in url:
        book_type = "红星图书系列"
    elif "lei=201" in url:
        book_type = "8.5常春藤（满28本/箱厂家代发）"
    elif "lei=198" in url:
        book_type = "精品字帖 1.5元系列"
    elif "lei=191" in url:
        book_type = "百汇图书精品专区"

    return [book_name, book_pages, book_size, book_weight, book_price, book_origin_price, book_image_url,
            book_publisher, book_type]


'''
  这个函数干了好多事:
    1. 连接数据库;
    2. 插入数据库数据;
    3. 导出数据到Excel.
'''


def get_db_connection(url):
    config = {
        "host": "*.*.*.*",
        "user": "root",
        "password": "Yu***?",
        "database": "baihui_book",
        "port": 3306,
        "charset": "utf8"
    }
    db = pymysql.connect(**config)
    cursor = db.cursor()
    try:
        insert_data_from(cursor, url, db)
    except Exception as e:
        print(Exception)
        print("insert_data_from....failed" + e)
    try:
        export(cursor, r'datetest.xlsx')
    except Exception as e:
        print("export....failed" + e)
    cursor.close()
    db.close()


def insert_data_from(cursor, url, db):
    book_type_urls = init_type_urls(url)
    for i in range(len(book_type_urls)):
        book_type_urls_pages = get_book_type_urls_pages(
            "http://www.baihuitushu888.com/" + book_type_urls[i])
        for j in range(int(book_type_urls_pages[0])):
            type_url = "http://www.baihuitushu888.com/" + \
                book_type_urls[i] + "&topage=" + str(j + 1)
            [book_name, book_page, book_size, book_weight, book_price, book_origin_price, book_image_url,
             book_publisher, book_type] = get_xpath_data(type_url)
            for k in range(len(book_name)):
                # 去除图书名字相同的数据
                sql_for_uniqe = "select * from baihui_book where book_name = '%s'"
                cursor.execute(sql_for_uniqe % book_name[k])
                result = cursor.fetchone()
                if result:
                    continue
                else:
                    sql = "INSERT INTO baihui_book(book_name, book_type, book_price, book_origin_price, book_page, " \
                          "book_weight, book_size, book_publisher, book_image_url) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                    if book_page[k].strip() == '':
                        book_page[k] = '0'
                    if book_weight[k].strip() == '':
                        book_weight[k] = '0'
                    data = (book_name[k], book_type, book_price[k], book_origin_price[k], book_page[k], book_weight[k],
                            book_size[k], book_publisher[k], "http://www.baihuitushu888.com/" + book_image_url[k])
                    print(sql % data)
                    cursor.execute(sql % data)
            db.commit()


def export(cursor, outputpath):
    xlsxFile = "datetest.xlsx"
    try:
        if os.path.exists(xlsxFile):
            os.remove(xlsxFile)
    except Exception as e:
        print("delete datetest.xlsx ..... failed" + e)
    cursor.execute('select * from baihui_book')
    # 重置游标的位置
    cursor.scroll(0, mode='absolute')
    # 搜取所有结果
    results = cursor.fetchall()

    # 获取MYSQL里面的数据字段名称
    fields = cursor.description
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('百汇图书清单', cell_overwrite_ok=True)

    # 写上字段信息
    for field in range(0, len(fields)):
        sheet.write(0, field, fields[field][0])

    # 获取并写入数据段信息
    row = 1
    col = 0
    for row in range(1, len(results) + 1):
        for col in range(0, len(fields)):
            sheet.write(row, col, u'%s' % results[row - 1][col])

    workbook.save(outputpath)


def job():
    # 获取网页上的数据
    url = 'http://www.baihuitushu888.com/shop.asp'
    try:
        get_db_connection(url)
        # send email
        send_export_email('定时邮件--百汇图书: 成功')
    except Exception as e:
        send_export_email('定时邮件--百汇图书: 失败' + e)


class SendEmail():
    def __init__(self, receiver_list=None, subject=None, content=None):
        self.stm_server = 'smtp.163.com'
        self.send_addr = 'zzhang_xz@163.com'
        self.password = 'Yu***?'
        self.receiver_list = receiver_list
        self.subject = subject
        self.content = content

    def send_email(self):
        email_client = SMTP_SSL(self.stm_server, 465)
        email_client.login(self.send_addr, self.password)

        try:
            for reveiver in self.receiver_list:
                message = MIMEMultipart()
                message['From'] = self.send_addr
                message['To'] = reveiver
                # subject
                message['Subject'] = Header(self.subject, 'utf-8')
                # content
                message.attach(MIMEText(self.content, 'html', 'utf-8'))
                # attachment
                xlsx_file = "datetest.xlsx"
                xlsx_apart = MIMEApplication(open(xlsx_file, 'rb').read())
                xlsx_apart.add_header(
                    'Content-Disposition', 'attachment', filename=xlsx_file)
                message.attach(xlsx_apart)
                email_client.sendmail(
                    self.send_addr, reveiver, message.as_string())
                time.sleep(random.randint(1, 3))
        except Exception as e:
            print(e)

        email_client.quit()


def send_export_email(subject):
    receiverlist = ['1252068782@qq.com', "zzhang_xz@163.com"]
    content = """
            <p>定时邮件--百汇图书清单</p>
            <img src="https://t1.hddhhn.com/uploads/tu/201903/195/4554fds.jpg"  alt="百汇图书" />
            """
    send_email1 = SendEmail(
        subject=subject, content=content, receiver_list=receiverlist)
    send_email1.send_email()


if __name__ == '__main__':
    # scheduler = BlockingScheduler()
    #
    # # scheduler.add_job(job, 'cron', month='1-12', day='1', hour='7')
    # scheduler.add_job(job, 'cron', hour='17', minute='40')
    #
    # scheduler.start()
    url = 'http://www.baihuitushu888.com/shop.asp'
    get_db_connection(url)
