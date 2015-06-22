PyMailMan
===
A simple tool for sending mail by Python

###Homepage
https://github.com/kongkongyzt/PyMailMan

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
    ['3456767@qq.com','testman@gmail.com'], 
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
    ['3456767@qq.com','testman@gmail.com'],
    'This is title', 
    "<p style='color:red'>This is the content</p>"
)
print 'OK' if mail.status else mail.errMsg
```

+ To send the email with file

```python
from PyMailMan import PyMailMan

mail = PyMailMan(host='smtp.qq.com', user='12345678', password='12345678')
#Recommand to write the absolute path of the file
mail.send(
    ['3456767@qq.com','testman@gmail.com'], 
    'This is title', 
    'This is the content',
    '/home/kongkongyzt/a.txt',
    '/home/kongkongyzt/b.txt'
)
print 'OK' if mail.status else mail.errMsg
```

+ To show the image in the mail content

```python
mail = PyMailMan(host='smtp-mail.outlook.com', user='xxxxx@outlook.com', password='xxxx')
mail.send(
    ['783087000@qq.com'],
    'This is title',
    "Hello,The following image is the photo of last vacation in China, do you <span style='color:red'>like</span> it ? <img src='cid:1'>",
    "/home/kongkongyzt/a.jpg",
    "/home/kongkongyzt/b.docx",
    "/home/kongkongyzt/c.jpg"
)
print 'OK' if mail.status else mail.errMsg
```

You need to attention that the 1 in <cid:1> means the second pictrue in your attachment,in this example is /home/kongkongyzt/c.jpg
You should also know that once you choose one of the image in the attachment to show in the mail content by using ````<img src='cid:xx'>````,
the image file will not present in the attachList of the mail

###Common mail smtp configure sample
assume the email address is 1234567@xx.com and password is 12345678
Here are some of the smtp configure example:

+ QQ Mail

```python
PyMailMan(host='smtp.qq.com', user='1234567', password='12345678')
```

+ Gmail

```python
PyMailMan(host='smtp.gmail.com', user='1234567@gmail.com', password='12345678')
```

+ Outlook

```python
PyMailMan(host='smtp-mail.outlook.com', user='1234567@outlook.com', password='12345678')
```

###Tips

+ You can manual defined the ports and the prefix

```python
PyMailMan(host='smtp.gmail.com', user='1234567@gmail.com', password='12345678', ports=25, prefix='gmail.com')
```

###Feedback
If you have any problem or issue, please contact me by opening an issue on the github homepage
Homepage: https://github.com/kongkongyzt/PyMailMan