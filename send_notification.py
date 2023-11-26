from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def send_ad(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """

    Send ad to specified users

    Usage: /send_ad#1000#text
        /send = command
        #1000 = number of users to send ad to
        #text = text of ad

    """
    e_u = 0

    msg = update.message.text
    print('msg:', msg)
    
    content = msg.split('#')
    print('content:', content)

    if len(content) == 3:
        to_users = content[1]
        print('to_users:', to_users)

        txt = content[2]
        print('txt:', txt)

        tg_users = await _get_clients()

        for i in range(0, len(to_users)):
            try:
                msg = await context.bot.send_message(chat_id=tg_users[i]['tg_id'], text=txt, parse_mode='HTML')
            except Exception as e:
                e_u += 1

        await update.message.reply_text('ad was sent to {} users'.format(len(to_users)-e_u))
    else:
        await update.message.reply_text('wrong format\nUsage: /send_ad#1000#ad')


if __name__ == '__main__':
    app = ApplicationBuilder().token("5593884317:AAGY5-c4DZhNtUlOZyr09Wj75P2QiKBHoFI").build()
    app.add_handler(CommandHandler("send_ad", send_ad))

    print('bot started')

    app.run_polling()
