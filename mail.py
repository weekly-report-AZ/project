import smtplib
from email.mime.text import MIMEText
from email.header import Header


mail_sender ='novartval@mail.ru'
mail_receiver ='novartval@mail.ru'
username ='novartval@mail.ru'
password ='123456789'
server = smtplib.SMTP('smtp.mail.ru:587')


subject = u'Тестовый email от '# + mail_sendler
body =u'ya = Hello, Bro)' 'ga = Hello, sister)'
mag = MIMEText (body, 'plain','utf-8')



server.starttls()
server.ehlo()
server.login(username, password)
server.sendmail(mail_sender, mail_receiver, mag.as_string())