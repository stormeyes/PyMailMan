# encoding:utf8
__author__ = 'kongkongyzt'

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class PyMailMan():
    def __init__(self, host, user, password, postfix='', charset='UTF-8'):
        self.host = host
        self.user = user
        self.password = password
        self.postfix = postfix if postfix else '.'.join(host.split('.')[-2:])
        self.charset = charset
        self.status = False
        self.errMsg = ''

    def send(self, recieverList, mailTitle, mailContent, *attachment):
        me=self.user+"<"+self.user+"@"+self.postfix+">"
        if attachment:
            msg = MIMEMultipart()
            for attachName in attachment:
                attachFile = MIMEText(open(attachName, 'rb').read(), 'base64', self.charset)
                attachFile["Content-Type"] = 'application/octet-stream'
                attachFile["Content-Disposition"] = 'attachment; filename="{}"'.format(attachName)
                msg.attach(attachFile)
            msg['Subject'] = mailTitle
            msg['From'] = me
            msg['To'] = ";".join(recieverList)
        else:
            msg = MIMEText(mailContent, _subtype='html', _charset=self.charset)
            msg['Subject'] = mailTitle
            msg['From'] = me
            msg['To'] = ";".join(recieverList)
        try:
            server = smtplib.SMTP()
            server.connect(self.host)
            server.ehlo()
            server.starttls()
            server.login(self.user, self.password)
            server.sendmail(me, recieverList, msg.as_string())
            server.close()
            self.status = True

        except Exception, e:
            self.status = False
            self.errMsg = str(e)
