

from email.mime.text import MIMEText
import smtplib

msg = MIMEText('hello, send by python...', 'plain', 'utf-8')

from_addr = 'liangrenhong2017@gmail.com'

password = '_lrh0000'

to_addr = '1075220132@qq.com'

smtp_server = 'smtp.gmail.com'

server = smtplib.SMTP_SSL(smtp_server, 465)
# server.connect(smtp_server, 465)
# server.set_debuglevel(1)

server.login(from_addr, password)

server.sendmail(from_addr, [to_addr], msg.as_string())

server.quit()

print('sended')

