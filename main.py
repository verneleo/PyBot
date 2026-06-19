import os
from dotenv import load_dotenv
from telegram import Update, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

print(TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! \nЯ бот для поиска фильмов.")
    print(update.message.text)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Памятка о командах: \n/help - сводка о всех командах \n/start - запуск бота")

async def whoami(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Твой username: {update.effective_user.username}")
    
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    username = update.effective_user.username

    firstname = update.effective_user.first_name    

    us_text = f"Привет, {firstname}! \nТвой username в ТГ: @{username}"
    
    if firstname:
        us_text = us_text
    else:
        us_text = f"Привет! \nТвой username в ТГ: @{username}"
    await update.message.reply_text(us_text)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uname = update.effective_user.first_name
    message = update.message.text.lower().strip()
    clear_message = ''
    if not message.isalnum():
        for symb in message:
            if symb.isalnum() or symb.isspace():
                clear_message += symb
    else:
         clear_message = message
    if clear_message.startswith("привет"):
            await update.message.reply_text(f"Привет, {uname}!")
    elif clear_message.startswith("пока"):
            await update.message.reply_text(f"До встречи, {uname}!")
    else:        
            await update.message.reply_text(f"Я ещё не знаю, что значит '{message}'")
    
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CommandHandler("help", help))

app.add_handler(CommandHandler("whoami", whoami))

app.add_handler(CommandHandler("hello", hello))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()