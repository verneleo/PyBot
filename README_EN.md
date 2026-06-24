##Kinopoisk Telegram Bot
A Telegram bot that recommends random movies using the Kinopoisk API.
##Features
Random movie recommendations
Genre selection via Telegram keyboard
Movie poster preview
Movie description
Kinopoisk rating
Release year
Movie duration
Country information
##Supported Genres
Comedy
Drama
Action
Detective
##Technologies
Python 3
python-telegram-bot
Requests
Kinopoisk API
dotenv
##Installation
#Clone the repository:
git clone <repository-url>
cd PyBot
#Install dependencies:
pip install -r requirements.txt
#Create a .env file:
BOT_TOKEN=your_telegram_bot_token
X-API-KEY=your_kinopoisk_api_key
#Run the bot:
python main.py
##Project Structure
main.py          - Telegram bot logic
kinopoisk.py     - Kinopoisk API requests
requirements.txt - Dependencies
.env             - Secrets (not tracked by git)
##Future Plans
“Show another movie” button
More genres
Country filters
Rating filters
Watch history
Favorites
License
This project is created for educational purposes.
