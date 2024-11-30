from telegram import Update
from telegram.ext import CallbackContext

warnings = {}

# Helper function to get user details (either by user ID or username)
def get_user_info_from_message(update: Update):
    # Check if it's a reply to a message
    if update.message.reply_to_message:
        return update.message.reply_to_message.from_user
    # Check if the user is mentioned (using '@username')
    elif update.message.entities:
        for entity in update.message.entities:
            if entity.type == 'mention' or entity.type == 'text_mention':
                username = update.message.text[entity.offset + 1: entity.offset + entity.length]
                try:
                    # Try to get the user by username
                    user_info = update.message.bot.get_chat(username)
                    return user_info
                except Exception as e:
                    print(f"Error fetching user by username {username}: {e}")
                    return None
    return None

# Function to warn a user by user ID or username
async def warn_user(update: Update, context: CallbackContext):
    user_info = get_user_info_from_message(update)
    
    if user_info:
        user_id = user_info.id
        warnings[user_id] = warnings.get(user_id, 0) + 1
        username = user_info.username if user_info.username else user_info.full_name
        await update.message.reply_text(f"Warned {username}. Warnings: {warnings[user_id]}")
    else:
        await update.message.reply_text("Please reply to a message or mention the user.")

# Function to show warnings by user ID or username
async def show_warnings(update: Update, context: CallbackContext):
    user_info = get_user_info_from_message(update)
    
    if user_info:
        user_id = user_info.id
        count = warnings.get(user_id, 0)
        username = user_info.username if user_info.username else user_info.full_name
        await update.message.reply_text(f"{username} has {count} warnings.")
    else:
        await update.message.reply_text("Please reply to a message or mention the user.")

# Function to clear warnings for a user
async def clear_warnings(update: Update, context: CallbackContext):
    user_info = get_user_info_from_message(update)
    
    if user_info:
        user_id = user_info.id
        warnings[user_id] = 0
        username = user_info.username if user_info.username else user_info.full_name
        await update.message.reply_text(f"Cleared warnings for {username}.")
    else:
        await update.message.reply_text("Please reply to a message or mention the user.")

# Function to mute a user by user ID or username
async def mute_user(update: Update, context: CallbackContext):
    user_info = get_user_info_from_message(update)
    
    if user_info:
        user_id = user_info.id
        await context.bot.restrict_chat_member(
            chat_id=update.message.chat_id,
            user_id=user_id,
            permissions={"can_send_messages": False}
        )
        username = user_info.username if user_info.username else user_info.full_name
        await update.message.reply_text(f"Muted {username}")
    else:
        await update.message.reply_text("Please reply to a message or mention the user.")

# Function to unmute a user by user ID or username
async def unmute_user(update: Update, context: CallbackContext):
    user_info = get_user_info_from_message(update)
    
    if user_info:
        user_id = user_info.id
        await context.bot.restrict_chat_member(
            chat_id=update.message.chat_id,
            user_id=user_id,
            permissions={"can_send_messages": True}
        )
        username = user_info.username if user_info.username else user_info.full_name
        await update.message.reply_text(f"Unmuted {username}")
    else:
        await update.message.reply_text("Please reply to a message or mention the user.")
