import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
from flask import Flask, request

from handlers.general import creator, contribute, about
from handlers.userInfo import get_group_info, get_my_info, get_user_info
from handlers.admin import pin_message, delete_message, kick_user, ban_user, promote_user, demote_user, get_admins
from handlers.moderation import warn_user, show_warnings, clear_warnings, mute_user, unmute_user
from handlers.polls import create_poll
from handlers.messages import handle_message
from handlers.group_events import welcome_new_member, member_left

# Load environment variables
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
VERCEL_URL = os.getenv("VERCEL_URL")  # Your Vercel deployment URL

# Create Flask app
app = Flask(__name__)

# Create Telegram Application
bot_app = Application.builder().token(TELEGRAM_TOKEN).build()

# Add all handlers
bot_app.add_handler(CommandHandler("creator", creator))
bot_app.add_handler(CommandHandler("contribute", contribute))
bot_app.add_handler(CommandHandler("about", about))

bot_app.add_handler(CommandHandler("pin", pin_message))
bot_app.add_handler(CommandHandler("delete", delete_message))
bot_app.add_handler(CommandHandler("kick", kick_user))
bot_app.add_handler(CommandHandler("ban", ban_user))
bot_app.add_handler(CommandHandler("promote", promote_user))
bot_app.add_handler(CommandHandler("demote", demote_user))
bot_app.add_handler(CommandHandler("admins", get_admins))

bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

bot_app.add_handler(CommandHandler("groupinfo", get_group_info))
bot_app.add_handler(CommandHandler("myinfo", get_my_info))
bot_app.add_handler(CommandHandler("userinfo", get_user_info))

bot_app.add_handler(CommandHandler("warn", warn_user))
bot_app.add_handler(CommandHandler("warnings", show_warnings))
bot_app.add_handler(CommandHandler("clearwarnings", clear_warnings))
bot_app.add_handler(CommandHandler("mute", mute_user))
bot_app.add_handler(CommandHandler("unmute", unmute_user))

bot_app.add_handler(CommandHandler("poll", create_poll))

bot_app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))
bot_app.add_handler(MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, member_left))


@app.route("/")
def home():
    return "KGbot is running on Vercel!"


@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def webhook():
    update = request.get_json()
    bot_app.update_queue.put_nowait(update)
    return "OK", 200


# Set webhook when Flask starts
@app.before_first_request
def set_webhook():
    bot_app.bot.set_webhook(url=f"https://{VERCEL_URL}/{TELEGRAM_TOKEN}")


if __name__ == "__main__":
    app.run(port=3000)
