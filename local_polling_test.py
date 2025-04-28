# simple_bot.py
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

# Define a simple start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text("Hello! I'm a simple test bot. ✅")
    else:
        print("No message received.")


def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    app = ApplicationBuilder().token(os.environ['TELEGRAM_BOT_TOKEN']).build()

    app.add_handler(CommandHandler("start", start))

    print(f"Bot is running...{TELEGRAM_BOT_TOKEN}")
    app.run_polling()


if __name__ == '__main__':
    main()