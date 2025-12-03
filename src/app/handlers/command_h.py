from telegram import Update
from app.utils import config, helper
from app.templates import text_and_markup
from telegram.ext import CommandHandler, ContextTypes

logger = config.setup_logger(__name__)

@helper.safe_request
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(text_and_markup.choose_lang, reply_markup=text_and_markup.lang_key)
@helper.safe_request
async def help(update: Update, context) ->  None:
    await update.message.reply_text(text_and_markup.help)
@helper.safe_request
async def language(update: Update, context) ->  None:
    await update.message.reply_text(text_and_markup.choose_lang,
                                    reply_markup=text_and_markup.lang_key)
async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass


#Command handlers
start_c = CommandHandler('start', start)
help_c = CommandHandler('help', help)
lang_c = CommandHandler('language', language)