# encoding:utf8
__author__ = 'kongkongyzt'

import smtplib
import mimetypes
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class PyMailMan():
    def __init__(self, host, user, password, ports=25, postfix='', charset='UTF-8'):
        self.host = host
        self.user = user
        self.password = password
        self.ports = ports
        self.postfix = postfix if postfix else '.'.join(host.split('.')[-2:])
        self.charset = charset
        self.status = False
        self.errMsg = ''

    def send(self, receivers, title, content, *attachment):
        me=self.user+"<"+self.user+"@"+self.postfix+">"
        if attachment:
            msg = MIMEMultipart()
            for attachName in attachment:
                attachFile = MIMEText(open(attachName, 'rb').read(), 'base64', self.charset)
                attachFile["Content-Type"] = 'application/octet-stream'
                attachFile["Content-Disposition"] = 'attachment; filename="{}"'.format(attachName)
                msg.attach(attachFile)
            msg.attach(MIMEText(content, _subtype='html', _charset=self.charset))
            msg['Subject'] = title
            msg['From'] = me
            msg['To'] = ";".join(receivers)
        else:
            msg = MIMEText(content, _subtype='html', _charset=self.charset)
            msg['Subject'] = title
            msg['From'] = me
            msg['To'] = ";".join(receivers)
        try:
            server = smtplib.SMTP()
            server.connect("{}:{}".format(self.host, self.ports))
            server.ehlo()
            server.starttls()
            server.login(self.user, self.password)
            server.sendmail(me, receivers, msg.as_string())
            server.close()
            self.status = True

        except Exception, e:
            self.status = False
            self.errMsg = str(e)
