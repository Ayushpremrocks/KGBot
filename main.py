from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ChatMemberHandler
from config import TELEGRAM_TOKEN
from handlers.general import creator, contribute, about
from handlers.userInfo import get_group_info, get_user_info
from handlers.admin import pin_message, delete_message, kick_user, ban_user, promote_user, demote_user, get_admins
from handlers.moderation import warn_user, show_warnings, clear_warnings, mute_user, unmute_user
from handlers.polls import create_poll
from handlers.messages import handle_message
from handlers.group_events import welcome_new_member, member_left


def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # General command handlers #working
    application.add_handler(CommandHandler("creator", creator)) # working
    application.add_handler(CommandHandler("contribute", contribute)) # working
    application.add_handler(CommandHandler("about", about)) # working

    # Admin command handlers
    # add user function
    application.add_handler(CommandHandler("pin", pin_message)) # working
    application.add_handler(CommandHandler("delete", delete_message)) # working
    application.add_handler(CommandHandler("kick", kick_user))  # not working
    application.add_handler(CommandHandler("ban", ban_user)) # not working
    application.add_handler(CommandHandler("promote", promote_user)) # not working
    application.add_handler(CommandHandler("demote", demote_user)) # not working
    application.add_handler(CommandHandler("admins", get_admins)) # working

    # General message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)) # working

    # User info commands
    # error in the code
    application.add_handler(CommandHandler("groupinfo", get_group_info)) # working
    application.add_handler(CommandHandler("myinfo", get_user_info)) # not working

    # Moderation commands
    # error in this code as well
    # add user function
    application.add_handler(CommandHandler("warn", warn_user)) # not working
    application.add_handler(CommandHandler("warnings", show_warnings)) # not working
    application.add_handler(CommandHandler("clearwarnings", clear_warnings)) # not working
    application.add_handler(CommandHandler("mute", mute_user)) # not working
    application.add_handler(CommandHandler("unmute", unmute_user)) # not working

    # Poll command
    # error in the code
    application.add_handler(CommandHandler("poll", create_poll)) # not working

    # Group event handlers
    # error in the code
    application.add_handler(ChatMemberHandler(welcome_new_member, filters.StatusUpdate.NEW_CHAT_MEMBERS)) # not working
    application.add_handler(ChatMemberHandler(member_left, filters.StatusUpdate.LEFT_CHAT_MEMBER)) # not working

    # Run the bot
    print("Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
