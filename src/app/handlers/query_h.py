from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from app.utils import config, helper
from app.services import db_helper
from app.templates import text_and_markup
from telegram.ext import ContextTypes, CallbackQueryHandler

logger = config.setup_logger(__name__)

DataBase = db_helper.DatabaseService()

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    try:
        await query.answer()
    except Exception as e:
        logger.error(f"button_handler fialed to answer query: {e}")
        return True
    if query.data in ('eng', 'amh', 'oro'):
        DataBase.start()
        if DataBase.search_user(update.effective_chat.id) != None:
            DataBase.update_lang(update.effective_chat.id, query.data)
            await query.edit_message_text(text=text_and_markup.messages[query.data]['start'])
        else:
            DataBase.insert_user(update.effective_user.full_name, query.data, update.effective_chat.id, 'none')
            try:
                await query.edit_message_text(text=text_and_markup.messages[query.data]['start'])
            except Exception as e:
                logger.error(f"failed to send welcom message: {e}")
        DataBase.end()
    elif query.data.split('_')[0] in ['rejected', 'approved']:
        status, id = query.data.split('_')
        if status == 'approved':
            DataBase.start()
            DataBase.update_payment(id, 'Paid')
            try:
                await query.message.delete()
            except Exception as e:
                logger.error(e)
            application = DataBase.search_appliction(id)
            if application == None:
                return None
            caption = ''
            column_list = [
                            'Application ID', 
                            'User ID',
                            'Agent Referral',
                            'Full Name', 
                            'Gender', 
                            'Birth Date', 
                            'Birth City', 
                            'Current City', 
                            'Phone Number', 
                            'Email', 
                            'Education', 
                            'Marital Status', 
                            'Photo Path', 
                            'Payment Path', 
                            'Payment Status', 
                            'Register Status', 
                            'Creation Date'
                        ]
            for i in range(len(application)):
                caption += f"{column_list[i]}: {application[i]}\n"
            keyboard = [
               [InlineKeyboardButton("✅ Submitted", callback_data=f"submitted_{application[0]}")]
               ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            try:
                await context.bot.send_photo(
                                                chat_id=config.REGISTER,
                                                photo=open(application[12], 'rb'),
                                                caption=caption,
                                                reply_markup=reply_markup
                                            )
            except Exception as e:
                logger.error(e)
            DataBase.end()
        else:
            DataBase.start()
            DataBase.update_payment(id, 'Rejected')
            try:
                await query.message.delete()
            except Exception as e:
                logger.error(e)
            DataBase.end()
    elif query.data.split('_')[0] == 'submitted':
        DataBase.start()
        DataBase.update_register(query.data.split('_')[1], 'Submitted')
        app_data = DataBase.search_app_id(query.data.split('_')[1])
        referral_code = app_data[2]
        user_data = DataBase.search_user_by_id(app_data[1])
        if user_data[4] == 'Regular' and user_data[5] != 'None':
            DataBase.update_ref_apply(user_data[5])
        if user_data[4] == 'Agent':
            agent_data = DataBase.search_agent(user_data[1])
            DataBase.update_app_count(agent_data[5])
        DataBase.end()
        try:
            await query.message.delete()
        except Exception as e:
            logger.error(e)
    else:
        try:
            await query.message.reply_text("This is unknown callback data!!")
        except Exception as e:
            logger.error(e)
button_h = CallbackQueryHandler(button_handler)