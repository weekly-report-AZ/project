import smtplib                                              
import os                                                   
import mimetypes                                            
from email import encoders                                  
from email.mime.base import MIMEBase                       
from email.mime.text import MIMEText                                                               
from email.mime.multipart import MIMEMultipart             


addr_from = "novartval@mail.ru"
addr_to   = "novartval@mail.ru"                   
password  = "12345"                                  

msg = MIMEMultipart()                          
msg['From']    = addr_from
msg['To']      = addr_to                            
msg['Subject'] = 'Тема сообщения'                   
body = "1234"
msg.attach(MIMEText(body, 'plain')) 


filepath="full_file_path_with_filename"                   
filename = os.path.basename(filepath)                    

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
server = smtplib.SMTP('smtp.mail.ru:587')           
server.set_debuglevel(True)                         # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
server.starttls()                                   
server.login(addr_from, password)                   
server.send_message(msg)                            
server.quit()     