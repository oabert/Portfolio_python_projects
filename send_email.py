import smtplib, ssl
import os


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'rbn.leona@gmail.com'
    password = os.getenv('PASSWORD_LEONA')

    receiver = 'rbn.leona@gmail.com'
    my_context = ssl.create_default_context()
    # message = """\
    # Subject:Python app email
    # HI!
    # My first email
    # """
    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

# qccl asqc eiqk htzp
# send_email()
