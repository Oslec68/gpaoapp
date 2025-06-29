import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7569335662:AAEv99Vo8nNH6sGrGay8PXJH6qUMsgpoMD8"
async def visita_loja(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://oslec68.github.io/gpaoapp/frontend/"  # ou a URL real hospedada
    await update.message.reply_text(
        f"🔍 Acesse o formulário de visita da loja:\n\n{url}"
    keyboard = [
        [InlineKeyboardButton("✅ Iniciar Visita GPA", web_app=WebAppInfo(url="https://oslec68.github.io/gpa-visita-telegram-webapp/webapp/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Clique abaixo para abrir o App de Visita GPA:", reply_markup=reply_markup)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
