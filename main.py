import os
from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import filters
from dotenv import load_dotenv
from handlers.general import creator, contribute, about
from handlers.userInfo import get_group_info, get_my_info, get_user_info
from handlers.admin import pin_message, delete_message, kick_user, ban_user, promote_user, demote_user, get_admins
from handlers.moderation import warn_user, show_warnings, clear_warnings, mute_user, unmute_user
from handlers.polls import create_poll
from handlers.messages import handle_message
from handlers.group_events import welcome_new_member, member_left

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("creator", creator))
    application.add_handler(CommandHandler("contribute", contribute))
    application.add_handler(CommandHandler("about", about))

    application.add_handler(CommandHandler("pin", pin_message))
    application.add_handler(CommandHandler("delete", delete_message))
    application.add_handler(CommandHandler("kick", kick_user))
    application.add_handler(CommandHandler("ban", ban_user))
    application.add_handler(CommandHandler("promote", promote_user))
    application.add_handler(CommandHandler("demote", demote_user))
    application.add_handler(CommandHandler("admins", get_admins))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.add_handler(CommandHandler("groupinfo", get_group_info))
    application.add_handler(CommandHandler("myinfo", get_my_info))
    application.add_handler(CommandHandler("userinfo", get_user_info))

    application.add_handler(CommandHandler("warn", warn_user))
    application.add_handler(CommandHandler("warnings", show_warnings))
    application.add_handler(CommandHandler("clearwarnings", clear_warnings))
    application.add_handler(CommandHandler("mute", mute_user))
    application.add_handler(CommandHandler("unmute", unmute_user))

    application.add_handler(CommandHandler("poll", create_poll))

    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))
    application.add_handler(MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, member_left))

    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()