from app.utils.config import setup_logger
import functools
import time
logger = setup_logger(__name__)

def safe_request(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        for i in range(3):
            try:
                result = func(*args, **kargs)
                logger.debug(f"Operation: sending message, or other, status: successful")
                return result
            except Exception as e:
                if i==2:
                    logger.error(f"Operation: sending messaeg, Resone: {e}, re-try: 3")
                else:
                    logger.warning(f"Operation: sending message, Resone: {e}, re-try: {i+1}")
                    time.sleep(3)                   
    return wrapper

                    