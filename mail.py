# -*- coding: utf-8 -*-
from email import encoders                                  
from email.mime.base import MIMEBase                       
from email.mime.text import MIMEText                                                               
from email.mime.multipart import MIMEMultipart
import mimetypes
import os
import smtplib

import settings


def send_mail():
    addr_from = settings.ADDR_FROM
    addr_to = settings.ADDR_TO
    password = settings.PASSWORD
    filepath = settings.FILEPATH
    filename = os.path.basename(filepath)

    for addr in addr_to:
        msg = MIMEMultipart()
        msg['From'] = addr_from
        msg['To'] = addr
        msg['Subject'] = 'еженедельный отчет'
        body = 'Во вложениие к письму находится файл report.xlsx c результатами выполнения скрипта'
        msg.attach(MIMEText(body, 'plain'))

        if os.path.isfile(filepath):
            ctype, encoding = mimetypes.guess_type(filepath)
            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/', 1)
            if maintype == 'text':
                with open(filepath) as fp:
                    file = MIMEText(fp.read(), _subtype=subtype)
                    fp.close()
            else:
                with open(filepath, 'rb') as fp:
                    file = MIMEBase(maintype, subtype)
                    file.set_payload(fp.read())
                    fp.close()
                encoders.encode_base64(file)
            file.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(file)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(addr_from, password)
        server.send_message(msg)
        server.quit()


if __name__ == '__main__':
    send_mail()
