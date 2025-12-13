from app.web_app import flask_app
from app.utils import config

logger = config.setup_logger(__name__)

if __name__ == "__main__":
    try:
        flask_app.flask_run()
    except Exception as e:
        logger.error(f"failed to start the flask app: {e}")
