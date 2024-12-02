from telegram import Update
from telegram.ext import CallbackContext

async def welcome_new_member(update: Update, context: CallbackContext):
    if update.message.new_chat_members:
        for member in update.message.new_chat_members:
            welcome_message = (
                f"Hey there, sweetheart, {member.full_name}! 💖🌸\n"
                "Welcome to our cozy little group! 🌟 We're so happy to have you here! 🥰\n"
                "Feel free to say hi, share a bit about yourself, and don't forget to check out the group rules. 😇\n"
                "Let's make this space even more amazing together! 💬✨"
            )

            await update.message.reply_text(welcome_message)

async def member_left(update: Update, context: CallbackContext):
    if update.message.left_chat_member:
        left_member = update.message.left_chat_member
        goodbye_message = (
            f"Aw, {left_member.full_name}, we're so sad to see you go... 😢💔\n"
            "You’ll always be missed here, and we hope you'll come back someday! 🌸👋\n"
            "Take care of yourself and remember you’ll always have friends here! 🫶💖"
        )

        await update.message.reply_text(goodbye_message)