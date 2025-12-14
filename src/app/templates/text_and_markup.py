from telegram import (InlineKeyboardButton,
                      InlineKeyboardMarkup,
                      ReplyKeyboardMarkup)

choose_lang = """🌐 Welcome!

Before we begin, please choose your preferred language.
ይህን ቦት ለመጠቀም የሚመርጡትን ቋንቋ ይምረጡ።
Afaan ati itti fayyadamu fedhii qabdu filadhu.

👇 Choose from the options below:
"""
lang_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🇬🇧 English", callback_data='eng'),
      InlineKeyboardButton("🇪🇹 አማርኛ", callback_data='amh'),
      InlineKeyboardButton("🟢 Oromiffa", callback_data='oro')]]
)

messages = {
    'eng' : {
        'start' : """👋 Welcome to the DV Lottery Registration Bot!

⚠️ The U.S. DV Lottery is not open yet.
Until then, here are the things you can do:

✅ you can register as an agent to work with us.
👉click or send /agent to register

🎯 Once DV officially opens, you will receive an alert — and then you can submit your information through this bot and our website to complete your registration.

📢 Join our Telegram group to receive news and updates quickly:
👉 https://t.me/dvlotteryethiopia2027""",
        'help' : """✨ DV Lottery Assistant Bot — Help Menu

🤖 What This Bot Does
• Helps you submit DV Lottery applications
• Lets registered agents apply for clients
• Sends confirmation numbers when applications are completed

📌 Commands
• /start — Begin using the bot
• /apply — Start a new DV application
• /agent — Register as an agent
• /help — Show this help menu

📞 Support
Need help? Contact our support team:
• Telegram: @YourSupportUsername
• Phone: +123 456 7890
• Email: example@mail.com""",
        'questions' : ["Please enter your FULL LEGAL NAME exactly as it appears on your passport.",
                      "Please select your gender.",
                      "Please enter your date of birth (DD-MM-YYYY).",
                      "Which city or town were you born in?",
                      "What is your current city or town of residence?",
                      "Please enter your active phone number",
                      "Please enter your email address (used for confirmation).",
                      "What is your highest level of education?",
                      "What is your marital status?",
                      """Please upload a recent color passport-style photo. Make sure:
• Plain light background (white/cream)
• No glasses, hats, or shadows
• Face in center, clearly visible
• Photo taken within last 6 months
• Photo file is JPEG, max size 240 KB, 600×600 px (or per DV requirements).""",
                      """Please send a screenshot of your payment receipt to verify your application.

Make sure the screenshot clearly shows:
• Full name of sender
• Transaction amount
• Transaction reference code
• Date & time of payment

📤 Upload your screenshot here as an image.
Once verified, your application process will continue."""
                      ],
    'all_done' : """Screenshot received! 🎉
We’re now reviewing your payment.
Once confirmed, we’ll process your DV application and send you your confirmation number as soon as it's ready.
Thank you for choosing us! 🙏""",
    'gender' : ReplyKeyboardMarkup(
    [["Male", "Female"]],
    resize_keyboard=True,
    one_time_keyboard=True,
)
    },
    #####amharic######
    'amh' : {
        'start' : """👋 እንኳን ወደ DV ሎተሪ የመመዝገቢያ ቦታ በደህና መጡ!

⚠️ በአሁኑ ጊዜ የአሜሪካ DV ሎተሪ አልተከፈተም።
እስከዚያው ድረስ የምትችሉት ነገሮች፦

✅ ከእኛ ጋር ለመስራት እንደ ኤጀንት መመዝገብ ትችላላችሁ።
👉 /agent በመላክ ወይም በመጫን ይመዝገቡ

🎯 DV በይፋ እንደተከፈተ የማሳወቂያ መልእክት ይደርሶታል፤ ከዚያም በዚህ ቦት እና በድረ-ገጻችን መረጃዎን በመላክ መመዝገብ ትችላላችሁ።

📢 ዜናና ማሳወቂያዎች በፍጥነት እንዲደርሱዎት የቴሌግራም ግሩፓችንን ይቀላቀሉ፦
👉 https://t.me/dvlotteryethiopia2027""",
        'help' : """✨ DV Lottery አገልጋይ ቦት — የእርዳታ ሜኑ

🤖 ቦቱ የሚያደርገው
• የDV ሎተሪ መስጫ ሂደትን ይረዳዎታል
• የተመዘገቡ ወኪሎች ለደንበኞቻቸው ማመልከት ይችላሉ
• መመርያዎች ከተጠናቀቁ በኋላ የማረጋገጫ ቁጥሮችን ይልካል

📌 ትእዛዞች
• /start — ቦቱን ጀምር
• /apply — አዲስ የDV መዝገብ ጀምር
• /agent — እንደ ወኪል ተመዝገብ
• /help — ይህን የእርዳታ ሜኑ አሳይ

📞 ድጋፍ
እገዛ ይፈልጋሉ? የድጋፍ ቡድናችንን ያነጋግሩ፦
• ቴለግራም፦ @YourSupportUsername
• ስልክ፦ +123 456 7890
• ኢሜይል፦ example@mail.com
""",
    },
    #######affan_oromo########
    'oro' : {
        'start' : """👋 Baga nagaan gara Botii Galmeessa DV Lottery dhuftan!

⚠️ Amma yeroo kanatti DV Lottery Ameerikaa hin banne.
Hanga sanitti wantoota armaan gadii gochuu dandeessu:

✅ Nuti waliin hojjechuuf akka agentii galmaa’uu dandeessu.
👉 /agent cuqaasi ykn ergiitii galmaa’i

🎯 DV yommuu banu siif beeksisni ni dhufa; sana booda odeeffannoo kee bot kana fi marsariitii keenya fayyadamuun galmeessuu ni dandeessa.

📢 Oduu fi beeksisa haaraa saffisaan akka siif gahuuf garee Telegram keenyaa seeni:
👉 https://t.me/dvlotteryethiopia2027""",
        'help' : """✨ DV Lottery Gargaarsa Botii — Galmee Gargaarsaa

🤖 Botichi Wanta Dalagu
• Deeggarsa galmee DV Lottery siif kenna
• Ejansoonni galmaa’an maamiltootaaf ni dhiyeessu
• Galmeen fixxiin booda lakkoofsa mirkaneessaa ni erga

📌 Ajajawwan
• /start — Botii eegali
• /apply — Galmee DV haaraa jalqabi
• /agent — Akkuma ejansaatti of galmeessi
• /help — Galmee gargaarsaa kana agarsiisi

📞 Deeggarsa
Deeggarsa barbaaddaa? Garee deeggarsa keenya qunnamaa:
• Telegram: @YourSupportUsername
• Bilbila: +123 456 7890
• Email: example@mail.com""",
    }
}

cancel = """❌ Action cancelled.

You’ve stopped the current process. Use the menu to continue whenever you’re ready."""

timeout = """⏰ Session timed out.

Please start again if you want to continue"""

admin_panel = {'choice' : ReplyKeyboardMarkup(
                    [["🔔Broadcast Message"],
                     ["📊Statistics Dashboard"]],
                    resize_keyboard=True,
                    one_time_keyboard=True,
                ),
                'message_to' : ReplyKeyboardMarkup(
                    [["Agent", "Regular"],
                     ["All_bot_users"]],
                    resize_keyboard=True,
                    one_time_keyboard=True,
                ),
                'welcome' : """🔐 Admin Panel
Welcome back, Admin!
Please choose an option below to continue:"""
}

agent = {
    'eng' : {
        'form' : ['👤 Please enter your full name as an agent',
                  '📞 Enter your active phone number.',
                  '🏦 Please enter your CBE Bank Account Number.',
                  """🎉 Registration Complete!

👏 Your agent profile has been successfully created.

🚀 You can now start applying for clients using the bot.

Welcome aboard! 🤝

https://t.me/dvlotteryethiopiaagents
""",
"""⚠️ You’re already registered as an agent!

🎉 No need to register again.

https://t.me/dvlotteryethiopiaagents"""]
    },
    'amh' : {
        'form' : ['👤 እባክዎ የእርስዎን ሙሉ ስም ያስገቡ።',
                  '📞 የስልክ ቁጥርዎን ያስገቡ።',
                  '🏦 የCBE የባንክ አካውንት ቁጥርዎን ያስገቡ።',
                  """🎉 ቅጽዎ በተሳካ ሁነታ ተሞልቷል!

👏 የወኪል መዝገብዎ በተሳካ ሁኔታ ተፈጥሯል።

🚀 ከአሁን ጀምሮ በቦቱ የተመዝጋቢችን መረጃ መሙላት ይችላሉ።

እንኳን ወደ ቡድናችን በደህና መጡ! 🤝

https://t.me/dvlotteryethiopiaagents
""",
"""⚠️ እርስዎ ቀድሞውኑ እንደ ኤጀንት ተመዝግበዋል!

🎉 እንደገና መመዝገብ አያስፈልግዎትም።

https://t.me/dvlotteryethiopiaagents
"""]
    },
    'oro' : {
        'form' : ['👤 Maqaa guutuu kee galchi.',
                  '📞 Lakkoofsa bilbilaa kee galchi.',
                  '🏦 Lakkoofsa herrega CBE kee galchi.',
                  """🎉 Galmee keessan xumuramee!

👏 Proofaayilii Ajeentii keessan milkaa’inaan uumameera.

🚀 Amma irraa eegaluun odeeffannoo maamiltoota bot kanaan galchuu ni dandeessu.

Baga gara hojiitti dhuftan! 🤝

https://t.me/dvlotteryethiopiaagents
""",
"""⚠️ Ati dura booda akka ejentii galmaa’ee jira!

🎉 Irra deebi’anii galmaa’uu hin barbaachisu.

https://t.me/dvlotteryethiopiaagents
"""]
    }
}