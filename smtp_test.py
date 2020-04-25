#!/usr/bin/env python
# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart

my_sender='lwscode@163.com'
my_pass = 'hahaha597'
my_user='suyelu@126.com'
fd=open('baidu.html', 'rb')
mail_msg=fd.read()
fd.close()
msg=MIMEMultipart()
msg.attach(MIMEText(mail_msg,'html','utf-8'))
att1 = MIMEText(open('test.pdf', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="test.pdf"'
msg.attach(att1)

def mail():
    ret=True
    try:
        msg['From']=formataddr(["lws",my_sender])
        msg['To']=formataddr(["syl",my_user])
        msg['Subject']="廖卫狮"
        server=smtplib.SMTP_SSL("smtp.163.com", 465)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender,[my_user,],msg.as_string())
        server.quit()
    except Exception:
        ret=False
    return ret

ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
