from telegram import Update
from telegram.ext import CallbackContext

warnings = {}

def get_user_info_from_update(update: Update, context: CallbackContext):
    if update.message.reply_to_message:
        return update.message.reply_to_message.from_user
    
    if context.args and len(context.args) > 0:
        username = context.args[0].lstrip('@')
        try:
            chat = update.message.chat
            member = chat.get_member(username)
            return member.user
        except Exception as e:
            print(f"Error fetching user by username {username}: {e}")
            return None
    
    return None

async def warn_user(update: Update, context: CallbackContext):
    user_info = get_user_info_from_update(update, context)
    
    if user_info:
        user_id = user_info.id
        warnings[user_id] = warnings.get(user_id, 0) + 1
        username = user_info.username if user_info.username else user_info.full_name
        await update.message.reply_text(f"Warned {username}. Warnings: {warnings[user_id]}")
    else:
        await update.message.reply_text("Please reply to a message or provide a valid username.")

async def show_warnings(update: Update, context: CallbackContext):
    user_info = get_user_info_from_update(update, context)
    
    if user_info:
        user_id = user_info.id
        count = warnings.get(user_id, 0)
        username = user_info.username if user_info.username else user_info.full_name
        await update.message.reply_text(f"{username} has {count} warnings.")
    else:
        await update.message.reply_text("Please reply to a message or provide a valid username.")

async def clear_warnings(update: Update, context: CallbackContext):
    user_info = get_user_info_from_update(update, context)
    
    if user_info:
        user_id = user_info.id
        warnings[user_id] = 0
        username = user_info.username if user_info.username else user_info.full_name
        await update.message.reply_text(f"Cleared warnings for {username}.")
    else:
        await update.message.reply_text("Please reply to a message or provide a valid username.")

async def mute_user(update: Update, context: CallbackContext):
    user_info = get_user_info_from_update(update, context)
    
    if user_info:
        user_id = user_info.id
        try:
            await context.bot.restrict_chat_member(
                chat_id=update.message.chat_id,
                user_id=user_id,
                permissions={"can_send_messages": False}
            )
            username = user_info.username if user_info.username else user_info.full_name
            await update.message.reply_text(f"Muted {username}")
        except Exception as e:
            await update.message.reply_text(f"Failed to mute user: {e}")
    else:
        await update.message.reply_text("Please reply to a message or provide a valid username.")

async def unmute_user(update: Update, context: CallbackContext):
    user_info = get_user_info_from_update(update, context)
    
    if user_info:
        user_id = user_info.id
        try:
            await context.bot.restrict_chat_member(
                chat_id=update.message.chat_id,
                user_id=user_id,
                permissions={"can_send_messages": True}
            )
            username = user_info.username if user_info.username else user_info.full_name
            await update.message.reply_text(f"Unmuted {username}")
        except Exception as e:
            await update.message.reply_text(f"Failed to unmute user: {e}")
    else:
        await update.message.reply_text("Please reply to a message or provide a valid username.")