import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders

def send_mail( send_sender, send_receiver, subject, body, files=[], server, username, password):
	mail_sender ='novartval@mail.ru'
	mail_receiver ='novartval@mail.ru'
	username ='novartval@mail.ru'
	password ='1234'
	server = smtplib.SMTP('smtp.mail.ru:587')
	subject = u'Тестовый email от '# + mail_sendler
	body =u'ya = Hello, Bro)' 'ga = Hello, sister)'

	mag = MIMEText (body, 'plain','utf-8')

for f in files:
    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(f,"rb").read() )
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(f)))
    msg.attach(part)


server.starttls()
server.ehlo()
server.login(username, password)
server.sendmail(mail_sender, mail_receiver, mag.as_string())