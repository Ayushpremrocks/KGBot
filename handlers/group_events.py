from telegram import Update
from telegram.ext import CallbackContext, ChatMemberHandler

async def welcome_new_member(update: Update, context: CallbackContext):
    print("New member joined!")  # Debugging line
    if update.message.new_chat_members:
        for member in update.message.new_chat_members:
            welcome_message = f"Welcome to the group, {member.full_name}! 🎉 Feel free to introduce yourself and follow the group rules!"
            await update.message.reply_text(welcome_message)

async def member_left(update: Update, context: CallbackContext):
    print("Member left!")  # Debugging line
    left_member = update.message.left_chat_member
    if left_member:
        await update.message.reply_text(f"Goodbye, {left_member.full_name}! We will miss you. Appki yaado me hum rooya karenge 👋")
