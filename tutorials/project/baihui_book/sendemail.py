# #coding:utf-8   #强制使用utf-8编码格式
# import smtplib  #加载smtplib模块
# from sendemail.mime.text import MIMEText
# from sendemail.utils import formataddr
# my_sender = 'zzhang_xz@163.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
# my_user = '1252068782@qq.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
#
#
# def mail():
#     ret = True
#     try:
#         msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
#         msg['From'] = formataddr(["zack", my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
#         msg['To'] = formataddr(["zack-to", my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
#         msg['Subject'] = "主题" #邮件的主题，也可以说是标题
#
#         server = smtplib.SMTP("smtp.163.com",25)  #发件人邮箱中的SMTP服务器，端口是25
#         server.login(my_sender,"Yu***")    #括号中对应的是发件人邮箱账号、邮箱密码
#         server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#         server.quit()   #这句是关闭连接的意思
#     except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
#         ret=False
#     return ret
#
# ret=mail()
# if ret:
#     print("ok") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
# else:
#     print("filed")  #如果发送失败则会返回filed


from email.mime.multipart import MIMEMultipart

from email.mime.application import MIMEApplication
from smtplib import SMTP, SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header

import random
import time


class SendEmail():
    def __init__(self, receiver_list=None, subject=None, content=None):
        self.stm_server = 'smtp.163.com'
        self.send_addr = 'zzhang_xz@163.com'
        self.password = 'yu100861'
        self.receiver_list = receiver_list
        self.subject = subject
        self.content = content

    def send_email(self):
        email_client = SMTP_SSL(self.stm_server, 465)
        email_client.login(self.send_addr, self.password)

        try:
            for reveiver in self.receiver_list:
                message = MIMEMultipart()
                message['From'] = 'main<{}>'.format(self.send_addr)
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


if __name__ == "__main__":
    receiverlist = ['1252068782@qq.com']
    subject = '狗东西'
    content = """
        <p>定时邮件--百汇图书清单</p>
        <img src="https://t1.hddhhn.com/uploads/tu/201903/195/4554fds.jpg"  alt="百汇图书" />
        """
    send_email1 = SendEmail(
        subject=subject, content=content, receiver_list=receiverlist)
    send_email1.send_email()
