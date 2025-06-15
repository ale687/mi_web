import smtplib, ssl
import os
from dotenv import load_dotenv

load_dotenv()

host = "smtp.gmail.com"
port = 465

username = os.getenv("GMAIL_ADDRESS")
password = os.getenv("GMAIL_APP_PASSWORD")

receiver = username
context = ssl.create_default_context()

message =  """\
From: {}
To: {}
Subject: Prueba de envío con Python

Hola! Este correo fue enviado desde un 
script de Python usando variables de entorno.
""".format(username, receiver)

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

