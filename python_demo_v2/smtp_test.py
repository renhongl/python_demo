

from email.mime.text import MIMEText
import smtplib

msg = MIMEText('hello, send by python...', 'plain', 'utf-8')

from_addr = 'liang_renhong@163.com'

password = '111621116'

to_addr = 'liangrenhong2017@gmail.com'

smtp_server = 'smtp.163.com'

server = smtplib.SMTP(smtp_server, 25)

server.set_debuglevel(1)

server.login(from_addr, password)

server.sendmail(from_addr, [to_addr], msg.as_string())

server.close()


