# encoding:utf8
__author__ = 'kongkongyzt'
from PyMailMan import PyMailMan

mail = PyMailMan(host='smtp.qq.com', user='783087000', password='Ysly2345')
mail.send(['783087000@qq.com'], 'This is title', '<p style="color:red">This is the content</p>', "/home/kongkongyzt/a.txt")
print 'OK' if mail.status else mail.errMsg