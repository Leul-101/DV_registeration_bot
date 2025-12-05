from telegram import Update
from app.utils import config, helper
from app.templates import text_and_markup
from telegram.ext import CommandHandler, ContextTypes
from app.services import db_helper

logger = config.setup_logger(__name__)

DataBase = db_helper.DatabaseService()

@helper.safe_request
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    DataBase.start()
    if DataBase.search_user(update.effective_chat.id) == None:
        referral = str()
        if len(context.args) > 0:
            referral = context.args[0]
            DataBase.update_ref_start(context.args[0])
        else:
            referral = 'none'
        DataBase.insert_user(update.effective_user.full_name, 'eng', update.effective_chat.id, referral)
    DataBase.end()
    await update.message.reply_text(text_and_markup.choose_lang,
                                    reply_markup=text_and_markup.lang_key)

async def help(update: Update, context) ->  None:
    for i in range(3):
        try:
            DataBase.start()
            user = DataBase.search_user(update.message.chat_id)
            DataBase.end()
            await update.message.reply_text(text_and_markup.messages[user[3]]['help'])
            break
        except Exception as e:
            if i == 2:
                logger.error(f"failed to send help message: {e}")
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