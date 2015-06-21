PyMailMan
===
A simple tool for sending mail by Python

###Install
```sh
sudo pip install PyMailMan
```

###Usage
+ To send the text

```python
from PyMailMan import PyMailMan

mail = PyMailMan(host='smtp.qq.com', user='12345678', password='12345678')
mail.send(
    ['783087000@qq.com'], 
    'This is title', 
    'This is the content'
)
print 'OK' if mail.status else mail.errMsg
```

+ To send the HTML

```python
from PyMailMan import PyMailMan

mail = PyMailMan(host='smtp.qq.com', user='12345678', password='12345678')
mail.send(
    ['783087000@qq.com'],
    'This is title', 
    "<p style='color:red'>This is the content</p>"
)
print 'OK' if mail.status else mail.errMsg
```

+ To send the email with file

```python
from PyMailMan import PyMailMan

mail = PyMailMan(host='smtp.qq.com', user='12345678', password='12345678')
#You need to write the absolute path of the file
mail.send(
    ['783087000@qq.com'], 
    'This is title', 
    'This is the content',
    '/home/kongkongyzt/a.txt',
    '/home/kongkongyzt/b.txt'
)
print 'OK' if mail.status else mail.errMsg
```