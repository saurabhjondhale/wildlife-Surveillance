from telegram import Bot

bot = Bot(token='YOUR_TELEGRAM_BOT_TOKEN')
chat_id = 'YOUR_CHAT_ID'

def send_alert(message, photo_path=None):
    bot.send_message(chat_id=chat_id, text=message)
    if photo_path:
        bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
