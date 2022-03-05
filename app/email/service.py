import os
import smtplib
from socket import gaierror
from email.message import EmailMessage
import logging

logging.basicConfig(filename=os.getenv("LOGS_FILE"), filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

FROM_EMAIL = os.getenv("FROM_EMAIL_ADDRESS")
FROM_PWD = os.getenv("FROM_EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL_ADDRESS")
SMTP_SERVER = os.getenv("SMTP_SERVER")
PORT = os.getenv("PORT")


def send_email(content=""):
    msg = EmailMessage()
    msg["Subject"] = "Test"
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg.set_content(content)

    try:
        logging.info("Sending Email to %s", TO_EMAIL)
        with smtplib.SMTP_SSL(SMTP_SERVER, PORT) as smtp:
            smtp.login(FROM_EMAIL, FROM_PWD)
            smtp.send_message(msg)
    except (gaierror, ConnectionRefusedError):
        # tell the script to report if your message was sent or which errors need to be fixed
        logging.error(
            'Failed to connect to the server. Bad connection settings?')
    except smtplib.SMTPServerDisconnected:
        logging.error('Failed to connect to the server. Wrong user/password?')
    except smtplib.SMTPException as e:
        logging.error('SMTP error occurred: ', exc_info=True)
    else:
        logging.info('The mail has been sent successfully.')


if __name__ == "__main__":
    send_email('Te amo mami :3')
