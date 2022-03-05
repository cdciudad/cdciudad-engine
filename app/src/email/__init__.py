import os

FROM_EMAIL = os.getenv("FROM_EMAIL_ADDRESS")
FROM_PWD = os.getenv("FROM_EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL_ADDRESS")
SMTP_SERVER = os.getenv("SMTP_SERVER")
PORT = os.getenv("PORT")


def deploy_email_daemon():
    print("future thread running")
