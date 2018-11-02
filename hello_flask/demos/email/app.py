
from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.config.update(
    MAIL_SERVER = os.getenv('MAIL_SERVER'),
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD'),
    MAIL_DEFAULT_SENDER = ('Liang Ren Hong', os.getenv('MAIL_USERNAME'))
)

mail = Mail(app)

def send_mail(subject, to, body):
    message = Message(subject, recipients=[to], body=body)
    mail.send(message)

@app.route('/send_mail')
def send_mail_for_user():
    send_mail('Welcome for Register', '1075220132@qq.com', 'This is a auto mail for register, please do not reply.')
    return 'Welcome for Register, one email already send to you, please check...'