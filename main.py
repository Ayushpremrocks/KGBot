from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ChatMemberHandler
from dotenv import load_dotenv
import os
from handlers.general import creator, contribute, about
from handlers.userInfo import get_group_info, get_user_info
from handlers.admin import pin_message, delete_message, kick_user, ban_user, promote_user, demote_user, get_admins
from handlers.moderation import warn_user, show_warnings, clear_warnings, mute_user, unmute_user
from handlers.polls import create_poll
from handlers.messages import handle_message
from handlers.group_events import welcome_new_member, member_left

# Load environment variables
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # Fetch token from .env

def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # General command handlers #working
    application.add_handler(CommandHandler("creator", creator))  # working
    application.add_handler(CommandHandler("contribute", contribute))  # working
    application.add_handler(CommandHandler("about", about))  # working

    # Admin command handlers
    application.add_handler(CommandHandler("pin", pin_message))  # working
    application.add_handler(CommandHandler("delete", delete_message))  # working
    application.add_handler(CommandHandler("kick", kick_user))  # check implementation
    application.add_handler(CommandHandler("ban", ban_user))  # check implementation
    application.add_handler(CommandHandler("promote", promote_user))  # check implementation
    application.add_handler(CommandHandler("demote", demote_user))  # check implementation
    application.add_handler(CommandHandler("admins", get_admins))  # working

    # General message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # working

    # User info commands
    application.add_handler(CommandHandler("groupinfo", get_group_info))  # working
    application.add_handler(CommandHandler("myinfo", get_user_info))  # check implementation

    # Moderation commands
    application.add_handler(CommandHandler("warn", warn_user))  # check implementation
    application.add_handler(CommandHandler("warnings", show_warnings))  # check implementation
    application.add_handler(CommandHandler("clearwarnings", clear_warnings))  # check implementation
    application.add_handler(CommandHandler("mute", mute_user))  # check implementation
    application.add_handler(CommandHandler("unmute", unmute_user))  # check implementation

    # Poll command
    application.add_handler(CommandHandler("poll", create_poll))  # check implementation

    # Group event handlers
    application.add_handler(ChatMemberHandler(welcome_new_member, filters.StatusUpdate.NEW_CHAT_MEMBERS))  # check
    application.add_handler(ChatMemberHandler(member_left, filters.StatusUpdate.LEFT_CHAT_MEMBER))  # check

    # Run the bot
    print("Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
