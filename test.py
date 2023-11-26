from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def send(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_document(
        open('users_id.txt', 'r'),
        )


if __name__ == '__main__':
    app = ApplicationBuilder().token("5446625068:AAF3WJf9WbqKm71Gtx720FP2hSuPOvgll3s").build()

    app.add_handler(CommandHandler("send", send))

    app.run_polling()