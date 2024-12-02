from telegram import Update
from telegram.ext import CallbackContext

async def create_poll(update: Update, context: CallbackContext):
    if not context.args:
        await update.message.reply_text("Usage: /poll Favorite Color? Red, Blue, Green")
        return
    
    full_text = ' '.join(context.args)
    
    try:
        question, options_text = full_text.split('?', 1)
        
        options = [option.strip() for option in options_text.split(',')]
        
        if len(options) < 2:
            await update.message.reply_text("You need at least 2 options for a poll.")
            return
        
        await update.message.reply_poll(
            question=question.strip(), 
            options=options,
            is_anonymous=False
        )
    
    except ValueError:
        await update.message.reply_text("Incorrect format. Use: /poll Question? Option1, Option2, Option3")