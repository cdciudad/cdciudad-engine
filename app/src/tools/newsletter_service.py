# Python
import threading
from datetime import datetime as dt

# App
from app import logger
from app.src.services.subscribers import SubscribersService
from app.src.tools.email_service import send_email
from app.src.tools.files_service import generate_subscribers_file

message = '''
¡Hola Alex, te paso los subscriptores de esta semana!

No respondas directamente este correo electrónico
Copyright © 2022, Casa de la Ciudad | Frente a la Catedral de Cartago, Avenida Central, C. 6, Provincia de Cartago, Costa Rica
'''
t_day, t_hour, t_min, t_sec, t_mic = ("Thursday", 10, 10, 0, 0)
bussy = False


def send_weekly_subscribers():
    global bussy
    logger.info("Send weekly subscribers")
    subscribers = SubscribersService.get_weekly_subscribers()
    generate_subscribers_file(subscribers)
    send_email(message,
               filename="app/src/tools/tmp/subscribers.txt")
    logger.info("Sending subscribers was successful")
    bussy = False


def run_service():
    global bussy
    t = threading.Thread(target=send_weekly_subscribers, daemon=True)
    while True:
        now = dt.now()
        if not bussy and now.strftime("%A") == t_day and now.hour == t_hour and now.minute == t_min and now.second == 0:
            bussy = True
            logger.info(
                "Starting the process of sending new subscribers by email")
            t.start()
