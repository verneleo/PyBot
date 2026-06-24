import os
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from kinopoisk import get_random_movie

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

keyboard = [["Комедия", "Боевик"], ["Драма", "Детектив"], ["Помощь", "Назад"]]

main_keyboard = [["Выбрать жанр"], ["Помощь"]]

second_keyboard = [["🎲Ещё фильм"], ["🤝Достаточно"]]

genres = set()

flags = {
    "Россия": "🇷🇺",
    "США": "🇺🇸",
    "Великобритания": "🇬🇧",
    "Франция": "🇫🇷",
    "Германия": "🇩🇪",
    "Италия": "🇮🇹",
    "Испания": "🇪🇸",
    "Канада": "🇨🇦",
    "Австралия": "🇦🇺",
    "Новая Зеландия": "🇳🇿",
    "Япония": "🇯🇵",
    "Китай": "🇨🇳",
    "Южная Корея": "🇰🇷",
    "Индия": "🇮🇳",
    "Швеция": "🇸🇪",
    "Норвегия": "🇳🇴",
    "Дания": "🇩🇰",
    "Финляндия": "🇫🇮",
    "Бельгия": "🇧🇪",
    "Нидерланды": "🇳🇱",
    "Швейцария": "🇨🇭",
    "Ирландия": "🇮🇪",
    "Польша": "🇵🇱",
    "Турция": "🇹🇷",
    "Мексика": "🇲🇽",
    "Бразилия": "🇧🇷",
}

for row in keyboard:
    for genre in row:
         genres.add(genre.lower)

main_markup = ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True)

second_markup = ReplyKeyboardMarkup(second_keyboard, resize_keyboard=True)

genres_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def format_movie_message(year, name, rate, desc, movieLength, country):
    return(
        "Предлагаю следующий фильм по Вашему запросу:\n\n"
        f"🎬{name} ({year}г)\n"
        f"{flags[country]} Страна: {country}\n"
        f"⏳Длительность: {movieLength} минут \n"
        f"⭐️Рейтинг КП: {rate} \n\n"
        f"📝Описание: \n\n{desc}"
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет!" \
    "\nЯ бот, рекомендующий фильмы с Кинопоиска. Что хотите сделать?", reply_markup=main_markup)
    

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Памятка о командах:" 
    "\n/help - сводка о всех командах"
    "\n/start - запуск бота"
    "\n/whoami - вывод вашего username" 
    "\n/hello - приветствие"
    "\nКлючевые слова:" 
    "\nГруппа 'жанров' выдает случайный фильм из базы с рейтингом" \
    " от 7.4 по кинопоиску с годом выпуска от 1990 до 2026"
    "\n'Помощь' дублирует команду /help"
    )

async def whoami(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await  update.message.reply_text(f"Твой username: {update.effective_user.username}")
    
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
    
    elif clear_message.startswith("выбрать жанр"):
        await update.message.reply_text("Да, конечно, выбор на ваших глазах", reply_markup=genres_markup)
    
    elif clear_message.startswith("пока"):
        await update.message.reply_text(f"До встречи, {uname}!")
    
    elif clear_message.startswith("помощь"):
        await help(update, context)

    elif clear_message.startswith("комедия"):
        context.user_data["genre"] = "комедия"
        
        year, name, rate, desc, poster_url, movieLength, country = get_random_movie("комедия")

        await update.message.reply_photo(
            photo=poster_url,
            caption=format_movie_message(year, name, rate, desc, movieLength, country)
        )
        await update.message.reply_text("Что дальше?", reply_markup=second_markup)
    
    elif clear_message.startswith("боевик"):
        context.user_data["genre"] = "боевик"

        year, name, rate, desc, poster_url, movieLength, country = get_random_movie("боевик")
        
        await update.message.reply_photo(
            photo=poster_url,
            caption=format_movie_message(year, name, rate, desc, movieLength, country)
        ) 
        await update.message.reply_text("Что дальше?", reply_markup=second_markup)
        
    elif clear_message.startswith("драма"):
            context.user_data["genre"] = "драма"

            year, name, rate, desc, poster_url, movieLength, country = get_random_movie("драма")
            
            await update.message.reply_photo(
                photo=poster_url,
                caption=format_movie_message(year, name, rate, desc, movieLength, country)
            )
            await update.message.reply_text("Что дальше?", reply_markup=second_markup)
            
    elif clear_message.startswith("детектив"):
        context.user_data["genre"] = "детектив"

        year, name, rate, desc, poster_url, movieLength, country = get_random_movie("детектив")
            
        await update.message.reply_photo(
                photo=poster_url,
                caption=format_movie_message(year, name, rate, desc, movieLength, country)
            )
        await update.message.reply_text("Что дальше?", reply_markup=second_markup)

    elif clear_message.startswith("назад"):
        await update.message.reply_text("Одну секунду...", reply_markup=main_markup)
    
    elif clear_message.startswith("ещё"):
        genre = context.user_data.get("genre")              
        if genre:
            year, name, rate, desc, poster_url, movieLength, country = get_random_movie(genre)
            
        await update.message.reply_photo(
                photo=poster_url,
                caption=format_movie_message(year, name, rate, desc, movieLength, country), reply_markup=second_markup
            )
        
    elif clear_message.startswith("достаточно"):
        await update.message.reply_text("🫡Принято. \nВы можете выбрать новое действие", reply_markup=main_markup)
    
    else:        
        await update.message.reply_text(f"Я ещё не знаю, что значит '{message}'")
    


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CommandHandler("help", help))

app.add_handler(CommandHandler("whoami", whoami))

app.add_handler(CommandHandler("hello", hello))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()