from telegram import (Update,
                      ReplyKeyboardRemove,
                      InlineKeyboardButton,
                      InlineKeyboardMarkup)
from app.utils import config, helper
from app.services import db_helper
from app.templates import text_and_markup as tandm
from telegram.ext import (ConversationHandler,
                          ContextTypes,
                          MessageHandler,
                          CommandHandler,
                          filters)
import asyncio
import uuid
import json
import time

logger = config.setup_logger(__name__)

DataBase = db_helper.DatabaseService()

FORM_PAGES = range(11)

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
     try:
          await update.message.reply_text(tandm.cancel)
     except Exception as e:
          logger.error(f"cancel faild to rplay for {update.message.chat_id}: {e}")
     return ConversationHandler.END
async def timeout(update: Update, context: ContextTypes.DEFAULT_TYPE):
     try:
          await update.message.reply_text(tandm.timeout)
     except Exception as e:
          logger.error(f"timeout failed to reply for {update.message.chat_id}: {e}")
     return ConversationHandler.END

###DV FORM###  
async def form_entery(update: Update, context: ContextTypes.DEFAULT_TYPE):
     for i in range(3):
          try:
               await update.message.reply_text(tandm.messages['eng']['questions'][0])
               return FORM_PAGES[0]
          except Exception as e:
               if i == 2:
                    logger.warning(f"Conversation entery failed to start: {e}")
                    return ConversationHandler.END
               else:
                    logger.warning(f"Conversation entery failing: {e}")
async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data['full_name'] = update.message.text
     for i in range(3):
          try:
               await update.message.reply_text(tandm.messages['eng']['questions'][1],
                                               reply_markup=tandm.messages['eng']['gender'])
               return FORM_PAGES[1]
          except Exception as e:
               if i == 2:
                    logger.warning(f"Conversation entery failed to start: {e}")
                    return ConversationHandler.END
               else:
                    logger.warning(f"Conversation entery failing: {e}")
          await asyncio.sleep()
async def get_gender(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data['gender'] = update.message.text
     for i in range(3):
          try:
               await update.message.reply_text(tandm.messages['eng']['questions'][2],
                                               reply_markup=ReplyKeyboardRemove())
               return FORM_PAGES[2]
          except Exception as e:
               if i == 2:
                    logger.warning(f"Conversation entery failed to start: {e}")
                    return ConversationHandler.END
               else:
                    logger.warning(f"Conversation entery failing: {e}")
          await asyncio.sleep()
async def get_birthdate(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data['birth_date'] = update.message.text
     for i in range(3):
          try:
               await update.message.reply_text(tandm.messages['eng']['questions'][3])
               return FORM_PAGES[3]
          except Exception as e:
               if i == 2:
                    logger.warning(f"Conversation entery failed to start: {e}")
                    return ConversationHandler.END
               else:
                    logger.warning(f"Conversation entery failing: {e}")
          await asyncio.sleep()
async def get_birthcity(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data['birth_city'] = update.message.text
     for i in range(3):
          try:
               await update.message.reply_text(tandm.messages['eng']['questions'][4])
               return FORM_PAGES[4]
          except Exception as e:
               if i == 2:
                    logger.warning(f"Conversation entery failed to start: {e}")
                    return ConversationHandler.END
               else:
                    logger.warning(f"Conversation entery failing: {e}")
          await asyncio.sleep()
async def get_currentcity(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data['current_city'] = update.message.text
     for i in range(3):
          try:
               await update.message.reply_text(tandm.messages['eng']['questions'][5])
               return FORM_PAGES[5]
          except Exception as e:
               if i == 2:
                    logger.warning(f"Conversation entery failed to start: {e}")
                    return ConversationHandler.END
               else:
                    logger.warning(f"Conversation entery failing: {e}")
          await asyncio.sleep()
async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data['phone_number'] = update.message.text
     for i in range(3):
          try:
               await update.message.reply_text(tandm.messages['eng']['questions'][6])
               return FORM_PAGES[6]
          except Exception as e:
               if i == 2:
                    logger.warning(f"Conversation entery failed to start: {e}")
                    return ConversationHandler.END
               else:
                    logger.warning(f"Conversation entery failing: {e}")
          await asyncio.sleep()
async def get_email(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data['email'] = update.message.text
     for i in range(3):
          try:
               await update.message.reply_text(tandm.messages['eng']['questions'][7])
               return FORM_PAGES[7]
          except Exception as e:
               if i == 2:
                    logger.warning(f"Conversation entery failed to start: {e}")
                    return ConversationHandler.END
               else:
                    logger.warning(f"Conversation entery failing: {e}")
          await asyncio.sleep()
async def get_education(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data['education'] = update.message.text
     for i in range(3):
          try:
               await update.message.reply_text(tandm.messages['eng']['questions'][8])
               return FORM_PAGES[8]
          except Exception as e:
               if i == 2:
                    logger.warning(f"Conversation entery failed to start: {e}")
                    return ConversationHandler.END
               else:
                    logger.warning(f"Conversation entery failing: {e}")
          await asyncio.sleep()
async def get_marital(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data['marital_status'] = update.message.text
     for i in range(3):
          try:
               await update.message.reply_text(tandm.messages['eng']['questions'][9])
               return FORM_PAGES[9]
          except Exception as e:
               if i == 2:
                    logger.warning(f"Conversation entery failed to start: {e}")
                    return ConversationHandler.END
               else:
                    logger.warning(f"Conversation entery failing: {e}")
          await asyncio.sleep()
async def get_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
     for i in range(3):
          try:
               photo = await update.message.photo[-1].get_file()
               id = uuid.uuid4()
               path = f"{config.PHOTO_STORAGE}/{id}.jpg"
               context.user_data['photo_path'] = path
               await photo.download_to_drive(path)
               for j in range(2):
                    try:
                         await update.message.reply_text(tandm.messages['eng']['questions'][10])
                         return FORM_PAGES[10]
                    except:
                         if j == 1:
                              return ConversationHandler.END
               return FORM_PAGES[10]
          except Exception as e:
               if i == 2:
                    logger.warning(f"Conversation entery failed to start: {e}")
                    return ConversationHandler.END
               else:
                    logger.warning(f"Conversation entery failing: {e}")
          await asyncio.sleep(3)
async def get_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
     for i in range(3):
          try:
               photo = await update.message.photo[-1].get_file()
               id = uuid.uuid4()
               path = f"{config.PAYMENT_STORAGE}/{id}.jpg"
               context.user_data['payment_path'] = path
               await photo.download_to_drive(path)
               for j in range(2):
                    try:
                         DataBase.start()
                         bot_user = DataBase.search_user(update.message.chat_id)
                         DataBase.submit_application(bot_user[0],
                                                     bot_user[5],
                                                     context.user_data['full_name'],
                                                     context.user_data['gender'],
                                                     context.user_data['birth_date'],
                                                     context.user_data['birth_city'],
                                                     context.user_data['current_city'],
                                                     context.user_data['phone_number'],
                                                     context.user_data['email'],
                                                     context.user_data['education'],
                                                     context.user_data['marital_status'],
                                                     context.user_data['photo_path'],
                                                     context.user_data['payment_path']
                                                     )
                         DataBase.end()
                         await update.message.reply_text(tandm.messages['eng']['all_done'])
                         #return ConversationHandler.END
                         break
                    except:
                         if j == 1:
                              return ConversationHandler.END
                         await asyncio.sleep(3)
               keyboard = [
               [InlineKeyboardButton("✅ Approve", callback_data=f"approved_{id}"),
               InlineKeyboardButton("❌ Reject", callback_data=f"rejected_{id}")]
               ]
               reply_markup = InlineKeyboardMarkup(keyboard)

               await context.bot.send_photo(
               chat_id=int(config.PAYMENT_CHECKER),
               photo=photo.file_id,
               reply_markup=reply_markup
               )
               return ConversationHandler.END
          except Exception as e:
               if i == 2:
                    logger.warning(f"Conversation entery failed to start: {e}")
                    return ConversationHandler.END
               else:
                    logger.warning(f"Conversation entery failing: {e}")
          await asyncio.sleep(3)

##ADMIN####
ADMIN_PAGES = range(4)
async def admin_entery(update: Update, context: ContextTypes.DEFAULT_TYPE):
     admin_list = dict()
     with open(config.ADMIN_PATH, 'r') as file:
          admin_list = json.load(file)
     if str(update.message.chat_id)  in admin_list:
          try:
               await update.message.reply_text(tandm.admin_panel['welcome'],
                                         reply_markup=tandm.admin_panel['choice'])
               return ADMIN_PAGES[1]
          except Exception as e:
               logger.error(e)
               return ConversationHandler.END
     else:
          await update.message.reply_text('🔐Enter the referral code to be an admin🗝️:')
          return ADMIN_PAGES[0]
async def referral_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
     if update.message.text != config.ADMIN_REFERRAL:
          try:
               await update.message.reply_text("❌The referral code is incorrect")
               return ConversationHandler.END
          except Exception as e:
               logger.error(e)
     else:
          admin_list = dict()
          with open(config.ADMIN_PATH, 'r') as file:
               admin_list = json.load(file)
          admin_list[str(update.message.chat_id)] = update.effective_chat.full_name
          with open(config.ADMIN_PATH, 'w') as file:
               json.dump(admin_list, file, indent=4)
          DataBase.start()
          DataBase.update_role(update.effective_chat.id, 'Admin')
          DataBase.end()
          try:
               await update.message.reply_text(tandm.admin_panel['welcome'],
                                         reply_markup=tandm.admin_panel['choice'])
               return ADMIN_PAGES[1]
          except Exception as e:
               logger.error(e)
               return ConversationHandler.END
async def admin_service(update: Update, context: ContextTypes.DEFAULT_TYPE):
     if update.message.text == "🔔Broadcast Message":
          try:
               text = """Please choose who you want to send this message to 👇

🎯 Select one of the options below to continue."""
               await update.message.reply_text(text=text,
                                               reply_markup=tandm.admin_panel['message_to'])
               return ADMIN_PAGES[2]
          except Exception as e:
               logger.error(e)
     elif update.message.text == "📊Statistics Dashboard":
          try:
               DataBase.start()
               users = DataBase.retun_users()
               DataBase.end()
               await update.message.reply_text(f"number of user: {len(users)}",
                                               reply_markup=ReplyKeyboardRemove())
               return ConversationHandler.END
          except Exception as e:
               logger.error(e)
     else:
          try:
               await update.message.reply_text("❌The service your looking for is not available",
                                               reply_markup=ReplyKeyboardRemove())
               return ConversationHandler.END
          except Exception as e:
               logger.error(e)
     return ConversationHandler.END
async def admin_broadcast_to(update: Update, context: ContextTypes.DEFAULT_TYPE):
     broadcast_to = update.message.text
     context.user_data['broadcast_to'] = broadcast_to
     try:
          await update.message.reply_text("""Please type the message you want to send.

📌 This message will be delivered to the selected users.
When ready, just send the text below 👇""", reply_markup=ReplyKeyboardRemove())
          return ADMIN_PAGES[3]
          
     except Exception as e:
          logger.error(f"filed to send message to admin: {e}")
          return ConversationHandler.END
async def admin_broadcast_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
          message = update.message.text
          DataBase.start()
          all_users = DataBase.retun_users()
          DataBase.end()

          if all_users:
               index = 0
               if context.user_data['broadcast_to'] in ['Agent', 'Regular']:
                    for i in all_users:
                         if i[4] == context.user_data['broadcast_to']:
                              try:
                                   await context.bot.send_message(chat_id=i[1], text=message)
                                   index += 1
                              except Exception as e:
                                   logger.error(f"failed to broadcast message to {i[1]}: {e}")
                              
                              if index % 20 == 0:
                                   time.sleep(1)
                    try:
                         await update.message.reply_text(f"✅ Message sent to {index} {context.user_data['broadcast_to']}s.")
                    except Exception as e:
                         logger.error(e)
               elif context.user_data['broadcast_to'] == 'All_bot_users':
                    for i in all_users:
                         try:
                              await context.bot.send_message(chat_id=i[1], text=message)
                              index += 1
                         except Exception as e:
                              logger.error(f"failed to broadcast message to {i[1]}: {e}")
                         if index % 20 == 0:
                                   time.sleep(1)
                    try:
                         await update.message.reply_text(f"✅ Message sent to {index} {context.user_data['broadcast_to']}s.")
                    except Exception as e:
                         logger.error(e)
               else:
                    try:
                         await update.message.reply_text("Soory, i can't find the  people you are looking for!")
                    except Exception as e:
                         logger.error(e)
          return ConversationHandler.END

###AGENT###
AGENT_FORM = range(3)
async def agent_entery(update: Update, context: ContextTypes.DEFAULT_TYPE):
     DataBase.start()
     data = DataBase.search_user(update.message.chat_id)
     context.user_data['lang'] = data[3]
     context.user_data['user_id'] = data[0]
     agent_data = DataBase.search_agent(update.message.chat_id)
     DataBase.end()
     for i in range(3):
          try:
               if data[4] == 'Agent':
                    text = f"""📊 Agent Panel

👥 Referrals Started: {agent_data[6]}
🎯 Referrals Applied: {agent_data[7]}
💼 Total Clients You Applied For: {agent_data[8]}

📎 Your Referral Link:
https://t.me/{context.bot.username}?start={agent_data[5]}

⚙️ Tools
• 👉 Use /apply to submit an application for a client
• 📥 Share your link to get more clients
• 📌 Use /agent anytime to refresh this panel"""
                    #await update.message.reply_text(tandm.agent[context.user_data['lang']]['form'][4])
                    await update.message.reply_text(text)
                    return ConversationHandler.END
               await update.message.reply_text(tandm.agent[context.user_data['lang']]['form'][0])
               return AGENT_FORM[0]
          except Exception as e:
               if i == 2:
                    logger.error(f"agent Conversation entery failed to start: {e}")
                    return ConversationHandler.END
               else:
                    logger.warning(f"agent Conversation entery failing: {e}")
          asyncio.sleep(3)
async def get_agent_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data['agent_name'] = update.message.text
     for i in range(3):
          try:
               await update.message.reply_text(tandm.agent[context.user_data['lang']]['form'][1])
               return AGENT_FORM[1]
          except Exception as e:
               if i == 2:
                    logger.error(f"Conversation entery failed to start: {e}")
                    return ConversationHandler.END
               else:
                    logger.warning(f"Conversation entery failing: {e}")
          await asyncio.sleep()
async def get_agent_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data['agent_phone'] = update.message.text
     for i in range(3):
          try:
               await update.message.reply_text(tandm.agent[context.user_data['lang']]['form'][2])
               return AGENT_FORM[2]
          except Exception as e:
               if i == 2:
                    logger.error(f"Conversation entery failed to start: {e}")
                    return ConversationHandler.END
               else:
                    logger.warning(f"Conversation entery failing: {e}")
          await asyncio.sleep()
async def get_agent_bank(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data['agent_bank'] = update.message.text
     code = f"{str(uuid.uuid4()).split('-')[1]}_{update.message.chat_id}" 
     DataBase.start()
     DataBase.update_role(update.message.chat_id, 'Agent')
     DataBase.insert_agent(context.user_data['user_id'],
                           context.user_data['agent_name'],
                           context.user_data['agent_phone'],
                           context.user_data['agent_bank'],
                           code)
     DataBase.end()
     text = f"""📊 Agent Panel

👥 Referrals Started: 0
🎯 Referrals Applied: 0
💼 Total Clients You Applied For: 0

📎 Your Referral Link:
https://t.me/{context.bot.username}?start={code}

⚙️ Tools
• 👉 Use /apply to submit an application for a client
• 📥 Share your link to get more clients
• 📌 Use /agent anytime to refresh this panel"""
     for i in range(3):
          try:
               await update.message.reply_text(text)
               return ConversationHandler.END
          except Exception as e:
               if i == 2:
                    logger.error(f"Conversation entery failed to start: {e}")
                    return ConversationHandler.END
               else:
                    logger.warning(f"Conversation entery failing: {e}")
          await asyncio.sleep()
#CONVERSATION_HANDLERS
conv_h_for_form = ConversationHandler(
     entry_points= [#MessageHandler(filters.Regex("^🛒 Add Item$"), add_item),
                    CommandHandler('apply', form_entery)
                    ],
     states = {
          FORM_PAGES[0] : [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
          FORM_PAGES[1] : [MessageHandler(filters.TEXT & ~filters.COMMAND, get_gender)],
          FORM_PAGES[2] : [MessageHandler(filters.TEXT & ~filters.COMMAND, get_birthdate)],
          FORM_PAGES[3] : [MessageHandler(filters.TEXT & ~filters.COMMAND, get_birthcity)],
          FORM_PAGES[4] : [MessageHandler(filters.TEXT & ~filters.COMMAND, get_currentcity)],
          FORM_PAGES[5] : [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
          FORM_PAGES[6] : [MessageHandler(filters.TEXT & ~filters.COMMAND, get_email)],
          FORM_PAGES[7] : [MessageHandler(filters.TEXT & ~filters.COMMAND, get_education)],
          FORM_PAGES[8] : [MessageHandler(filters.TEXT & ~filters.COMMAND, get_marital)],
          FORM_PAGES[9] : [MessageHandler(filters.PHOTO , get_photo)],
          FORM_PAGES[10] : [MessageHandler(filters.PHOTO , get_payment)],
          ConversationHandler.TIMEOUT: [MessageHandler(filters.ALL & ~filters.COMMAND, timeout)]
     },
     conversation_timeout=1800,
     fallbacks=[CommandHandler('cancel', cancel)],
     per_chat=True,
     per_user=True
)

conv_h_for_admin = ConversationHandler(
     entry_points= [CommandHandler('admin', admin_entery)],
     states = {
          ADMIN_PAGES[0] : [MessageHandler(filters.TEXT & ~filters.COMMAND, referral_check)],
          ADMIN_PAGES[1] : [MessageHandler(filters.TEXT & ~filters.COMMAND, admin_service)],
          ADMIN_PAGES[2] : [MessageHandler(filters.TEXT & ~filters.COMMAND, admin_broadcast_to)],
          ADMIN_PAGES[3] : [MessageHandler(filters.TEXT & ~filters.COMMAND, admin_broadcast_message)],
          ConversationHandler.TIMEOUT: [MessageHandler(filters.ALL & ~filters.COMMAND, timeout)]
     },
     conversation_timeout=1800,
     fallbacks=[CommandHandler('cancel', cancel)],
     per_chat=True,
     per_user=True
)
conv_h_for_agent = ConversationHandler(
     entry_points= [CommandHandler('agent', agent_entery)],
     states = {
          FORM_PAGES[0] : [MessageHandler(filters.TEXT & ~filters.COMMAND, get_agent_name)],
          FORM_PAGES[1] : [MessageHandler(filters.TEXT & ~filters.COMMAND, get_agent_phone)],
          FORM_PAGES[2] : [MessageHandler(filters.TEXT & ~filters.COMMAND, get_agent_bank)],
          ConversationHandler.TIMEOUT: [MessageHandler(filters.ALL & ~filters.COMMAND, timeout)]
     },
     conversation_timeout=1800,
     fallbacks=[CommandHandler('cancel', cancel)],
     per_chat=True,
     per_user=True
)