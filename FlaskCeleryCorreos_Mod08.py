Urbano Iguala Modulo 8

# -*- coding: utf-8 -*-


from flask import Flask, session
from flask_mail import Mail, Message
app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'urbano.iguala@gmail.com'
app.config['MAIL_PASSWORD'] = 'Z42701Track'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

with app.app_context():
    msg = Message('Hello Dear Friends', sender = 'Sosa Valenzuela<sos.vlz.sos@gmail.com>',\
                  recipients = ['Anna.hand.cs@gmail.com','Anna.hand@gmail.com'],\
                  reply_to='Anna.hand@gmail.com')
    msg.body = "Este correo es un test"
    mail.send(msg)

all_emails = ['Helin.dear@gmail.com']
with app.app_context():
    with mail.connect() as conn:
        for email in all_emails:
            message = 'Este es un tutorial, por favor omitirlo'
            subject = "Hi, Mr./Miss"
            msg = Message(recipients=[email],sender = 'Sosa Valenzuela<sos.vlz.sos@gmail.com>',\
                          body=message,subject=subject)
            conn.send(msg)

from threading import Thread


def send_email_thread(msg):
    with app.app_context():
        mail.send(msg)

with app.app_context():
    all_emails = ['Helin.dear@gmail.com']
    for email in all_emails:        
        message = 'Este es un tutorial, por favor omitirlo'
        subject = "hello, Mr./Miss"
        msg = Message(recipients=[email],sender = 'Anna.hand<Anna.hand.cs@gmail.com>',\
                          body=message,subject=subject)
        thr = Thread(target=send_email_thread, args=[msg])
        thr.start()