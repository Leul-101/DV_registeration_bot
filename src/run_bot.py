from telegram.ext import (Application,
                          CommandHandler,
                          MessageHandler,
                          filters)
from app.utils import config
from app.handlers import command_h, query_h, conversation_h
import threading

logger = config.setup_logger(__name__)
TOKEN = config.BOT_TOKEN

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(command_h.start_c)
    app.add_handler(command_h.help_c)
    app.add_handler(command_h.lang_c)
    app.add_handler(query_h.button_h)
    app.add_handler(conversation_h.conv_h_for_form)
    app.add_handler(conversation_h.conv_h_for_admin)
    app.add_handler(conversation_h.conv_h_for_agent)
    logger.info('starting...')
    app.run_polling()
    logger.info('Program stoped!')

if __name__ == "__main__":
    main()
