import logging
from telegram.ext import Updater, MessageHandler, Filters

# Konfigurasi logging untuk mendapatkan pesan debug
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Fungsi untuk meneruskan pesan
def forward_message(update, context):
    chat_id = '<TARGET_CHAT_ID>'  # Ganti dengan ID chat tujuan untuk meneruskan pesan
    message = update.message
    message_text = message.text

    context.bot.send_message(chat_id=chat_id, text=message_text)

# Fungsi utama untuk menjalankan bot
def main():
    # Gantikan <YOUR_BOT_TOKEN> dengan token bot Anda
    updater = Updater('<YOUR_BOT_TOKEN>', use_context=True)

    # Dapatkan handler untuk pesan yang masuk
    dp = updater.dispatcher

    # Jalankan fungsi forward_message() ketika ada pesan masuk
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))

    # Mulai bot
    updater.start_polling()

    # Tunggu hingga bot berhenti
    updater.idle()

if __name__ == '__main__':
    main()
￼Enter
