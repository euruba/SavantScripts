import smtplib
import sys

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
if len(sys.argv) < 6:
    print 'Usage: python ~/mail.py "user" "password" "email@domain.com" "subject" "message"'
else:
    toaddr = sys.argv[3] # Email 
    fromaddr = sys.argv[1]
    password = sys.argv[2]
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = sys.argv[4] # Asunto
 
    body = sys.argv[5] # Mensaje
    msg.attach(MIMEText(body, 'plain'))
 
    server = smtplib.SMTP('smtp.1and1.es', 25)
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
