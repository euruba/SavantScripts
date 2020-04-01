import smtplib
import sys

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
if len(sys.argv) < 6:
    print 'Usage: python ~/mail.py "user" "password" "smtp-server" "email@domain.com" "subject" "message"'
else:
    toaddr = sys.argv[4] # Email 
    fromaddr = sys.argv[1]
    password = sys.argv[2]
    smtpServer = sys.argv[3]
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = sys.argv[5] # Subject
 
    body = sys.argv[6] # Message
    msg.attach(MIMEText(body, 'plain'))
 
    server = smtplib.SMTP(smtpServer, 25)
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
