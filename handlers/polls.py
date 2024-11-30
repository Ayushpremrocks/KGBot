from telegram import Update
from telegram.ext import CallbackContext

async def create_poll(update: Update, context: CallbackContext):
    if len(context.args) >= 2:
        question = context.args[0]
        options = context.args[1:]
        await context.bot.send_poll(
            chat_id=update.message.chat_id,
            question=question,
            options=options,
            is_anonymous=False
        )
    else:
        await update.message.reply_text("Usage: /poll <question> <option1> <option2> ...")