#!/usr/bin/env python
# coding: utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
pass_google = os.environ.get('PASS_GOOGLE_AUTHENTICATION')
sender_gmail = os.environ.get('SENDER_GMAIL')
attachment_path = './Vendas.xlsx'
attachment_name = 'Vendas.xlsx'


def __add_attachment(menssage, attachment_path, attachment_name):
    attachment = open(attachment_path, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={attachment_name}')
    menssage.attach(part)


def send_mail():  
    email_body = """
    <h2>Arquivo da planilha de vendas.</h2>
    <p>Segue em anexo a planilha de vendas organizada por datas de vendas</p>
    """

    msg = MIMEMultipart()
    msg['Subject'] = f'Planilha de vendas {datetime.today().strftime("%d/%m/%Y")}'
    msg['From'] = f'{sender_gmail}'
    msg['To'] = f'{sender_gmail}'
    password = f'{pass_google}' 
    msg.attach(MIMEText(email_body, 'html'))

    __add_attachment(msg, attachment_path, attachment_name)
    

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

