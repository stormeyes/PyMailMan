# encoding:utf8
__author__ = 'kongkongyzt'
from PyMailer import PyMailer

mail = PyMailer(host='smtp.qq.com', user='12345678', password='12345678')
mail.send(['783087000@qq.com'], 'This is title', 'This is the content')
print 'OK' if mail.status else mail.errMsg