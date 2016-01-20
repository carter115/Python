# -*- coding: utf-8 -*-
import smtplib
import string

# smtplib.SMTP.connect()  # 连接远程smtp主机方法
# smtplib.SMTP.login()    # 远程smtp主机的检验方法
# smtplib.SMTP.sendmail() # 实现邮件的发送功能
# smtplib.SMTP.starttls() # 启用TLS安全传输模式
# smtplib.SMTP.quit()     # 断开smtp服务器的连接

HOST = "smtp.139.com"
SUBJECT = "Test email from python"
TO = "10000@qq.com"
FROM = "13500000000@139.com"
text = "Python rules them all!"
BODY = string.join(("From: %s" % FROM,
                    "To: %s" % TO,
                    "Subject: %s" % SUBJECT,
                    "",
                    text),"\r\n"
                   )
# print(BODY)
"""
From: 13500000000@139.com
To: 10000@qq.com
Subject: Test email from python

Python rules them all!
"""
server = smtplib.SMTP()
server.connect(HOST,25)
server.starttls()
server.login(FROM,"mypassword")
server.sendmail(FROM,TO,BODY)
server.quit()

