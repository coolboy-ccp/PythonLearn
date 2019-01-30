# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chu chengpeng'

from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib

def sendSMTP():
    msg = MIMEText('Just enjoy yourself!', 'plain', 'utf-8')
    #pw = input('peng0305')
    msg['From'] = Header('测试邮件发送功能From', 'utf-8')
    msg['To'] = Header('测试邮件发送功能To', 'utf8')
    msg['Subject'] = Header('测试邮件发送功能Subject', 'utf-8')
    smtp = smtplib.SMTP('192.168.0.184', 25)
    #smtp.set_debuglevel(1)
    #smtp.login(from_addr, pw)
    smtp.sendmail('chuchengpeng0119@163.com', ['532961592@qq.com'], msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    sendSMTP()