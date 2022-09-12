# Python
import logging
from logging.config import fileConfig
import os
from dotenv import load_dotenv

# Configure app logger
fileConfig("app/config/logger_config.ini")
logger = logging.getLogger()
logger.info("Logger configured")

# Configure environment
load_dotenv()
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
