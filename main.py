from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

TOKEN = "7582117943:AAEplGrrEUSKbqj7ewmd1pNrGDaOmp_FVqI"

logging.basicConfig(level=logging.INFO)

# أغاني تجريبية
songs_data = [
    {"title": "Fast Beat Energy", "url": "https://music.youtube.com/watch?v=dummy1"},
    {"title": "Power Vibes", "url": "https://music.youtube.com/watch?v=dummy2"},
    {"title": "Up Tempo Drive", "url": "https://music.youtube.com/watch?v=dummy3"},
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بيك في بوت البحث عن الأغاني المشابهة! ابعتلي اسم الأغنية أو شارك لينك من YouTube Music.")

async def recommend(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(song["title"], url=song["url"])] for song in songs_data
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("دي شوية ترشيحات لأغاني شبه اللي بتحبها:", reply_markup=reply_markup)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("recommend", recommend))

print("Bot is polling")
app.run_polling()
