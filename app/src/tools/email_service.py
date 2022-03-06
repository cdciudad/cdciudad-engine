import smtplib
from app.src.tools import *
from socket import gaierror
from email.message import EmailMessage
from app import logger


def set_email_metadata():
    msg = EmailMessage()
    msg["Subject"] = "Test"
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    return msg


def attach_file(filename, msg):
    with open(filename, "r") as file:
        logger.info("Sending attachment file: %s", file)
        msg.add_attachment(
            file.read(),
            filename=filename.split("/")[-1]
        )
    return msg


def send_email(content="", content_type="plain", filename=None):
    msg = set_email_metadata()
    msg.set_content(content, subtype=content_type)
    if filename:
        msg = attach_file(filename, msg)

    try:
        logger.info("Sending Email to %s", TO_EMAIL)
        with smtplib.SMTP_SSL(SMTP_SERVER, PORT) as smtp:
            smtp.login(FROM_EMAIL, FROM_PWD)
            smtp.send_message(msg)

    except (gaierror, ConnectionRefusedError):
        logger.error(
            'Failed to connect to the server. Bad connection settings?')
    except smtplib.SMTPServerDisconnected:
        logger.error('Failed to connect to the server. Wrong user/password?')
    except smtplib.SMTPException as e:
        logger.error('SMTP error occurred: ', exc_info=True)
    else:
        logger.info('The mail has been sent successfully.')
