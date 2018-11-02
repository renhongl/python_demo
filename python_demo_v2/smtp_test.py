import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'liang_renhong@163.com'
password = '******'
receivers = ['1075220132@qq.com']
mail_server = 'smtp.163.com'

message = MIMEText('Test smtp prog', 'plain', 'utf-8')
message['Subject'] = 'Test'
message['From'] = sender
message['To'] =  ';'.join(receivers)

try:
    smtp = smtplib.SMTP(mail_server, 25)
    smtp.login(sender, password)
    smtp.sendmail(sender, receivers, message.as_string())
    smtp.quit()
    print('发送成功。')
except smtplib.SMTPException as e:
    print('发送失败。')
    print(e)
