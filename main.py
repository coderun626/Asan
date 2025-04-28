# Asan 2
import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Bu yerga OpenWeatherMap API kalitingizni kiriting
OPENWEATHER_API_KEY = os.environ("WEATHER_API_KEY")
# Bu yerga o'z bot tokeningizni kiriting
TELEGRAM_BOT_TOKEN = os.environ("TELEGRAM_BOT_TOKEN")

# Weather function
def get_weather(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHER_API_KEY}&units=metric&lang=uz"
    response = requests.get(url)
    data = response.json()

    if data.get('cod') != 200:
        return "City not found. Please check the name and try again."

    city = data['name']
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    weather_info = (
        f"🏙 City: {city}\n"
        f"🌤 Condition: {weather_description}\n"
        f"🌡 Temperature: {temperature}°C\n"
        f"💧 Humidity: {humidity}%\n"
        f"🌬 Wind speed: {wind_speed} m/s\n"
    )
    return weather_info

# Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am Hawarayi Bot 🌤\nSend me a city name, and I will give you the weather info!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city_name = update.message.text
    weather_info = get_weather(city_name)
    await update.message.reply_text(weather_info)

# Main function (NOT async anymore)
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot started!")
    app.run_polling()

if __name__ == '__main__':
    main()
