# -*- coding: utf-8 -*-


from email import encoders
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr

import smtplib

from_addr = raw_input('From:')
password = raw_input('Password:')
to_addr = raw_input('To:')
smtp_server = raw_input('SMTP server:')

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

msg = MIMEText('hello ,send by python...',_subtype='plain',_charset='utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP()
server.connect(smtp_server,25)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()


