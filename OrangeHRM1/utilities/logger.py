
import logging
import os

os.makedirs("logs",exist_ok=True)

logging.basicConfig(
    filename="logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    force=True
)

class Logger:

    @staticmethod
    def info(message):
        #logging.error(message)
        logging.info(message)

    @staticmethod
    def error(message):
        logging.error(message)

    @staticmethod
    def warning(message):
        logging.warning(message)

    @staticmethod
    def debug(message):
        logging.debug(message)