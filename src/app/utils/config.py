import logging, os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def setup_logger(name: str, level = logging.DEBUG) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_h = logging.FileHandler(os.path.join(BASE_DIR, 'debug', 'logging.log'), encoding='utf-8')
    file_h.setLevel(level)
    file_h.setFormatter(formatter)
    stream_h = logging.StreamHandler()
    stream_h.setLevel(level)
    stream_h.setFormatter(formatter)
    logger.addHandler(file_h)
    return logger

load_dotenv(BASE_DIR + '/etc/.env')

DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

DB_PATH = os.path.join(BASE_DIR, 'data', DB_NAME)

ADMIN_PATH = BASE_DIR + '/etc/admins.json'

BOT_TOKEN = os.getenv('BOT_TOKEN')

ADMIN_REFERRAL = os.getenv('ADMIN_REFERRAL')

PHOTO_STORAGE = os.path.join(BASE_DIR, 'data', 'photo_storage')

PAYMENT_STORAGE = os.path.join(BASE_DIR, 'data', 'payment_storage')

##STUFF##

PAYMENT_CHECKER = os.getenv('PAYMENT_CHECKER')
REGISTER = os.getenv('REGISTER')
