# Python
import logging
from logging.config import fileConfig
from dotenv import load_dotenv

fileConfig("app/config/logger_config.ini")
load_dotenv()
logger = logging.getLogger()
logger.info("Logger configured")
