from telegram import Update
from telegram.ext import CallbackContext

async def get_group_info(update: Update, context: CallbackContext):
    chat = update.message.chat

    try:
        # Fetch the total number of members using get_chat_member_count
        member_count = await context.bot.get_chat_member_count(chat.id)
        group_info = (
            f"Group Name: {chat.title}\n"
            f"Group ID: {chat.id}\n"
            f"Total Members: {member_count}\n"
        )
    except Exception as e:
        group_info = "Unable to fetch group details. Please try again later."
        print(f"Error fetching group info: {e}")

    await update.message.reply_text(group_info)

async def get_user_info(update: Update, context: CallbackContext):
    user = update.message.from_user
    user_info = (
        f"Name: {user.full_name}\n"
        f"Username: @{user.username}\n"
        f"User ID: {user.id}\n"
    )
    await update.message.reply_text(user_info)