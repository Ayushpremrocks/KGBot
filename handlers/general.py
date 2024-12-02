from telegram import Update
from telegram.ext import CallbackContext

AYUSH_PREM_REPO = "https://github.com/Ayushpremrocks"
KGBOT_REPO = "https://github.com/Ayushpremrocks/KGBot"
TELEGRAM_USERNAME = "@ayushpremrocks"

CREATOR_INFO = (
    f"Created by [{TELEGRAM_USERNAME}](https://t.me/{TELEGRAM_USERNAME})\n"
    f"GitHub: [Ayush Prem's GitHub]({AYUSH_PREM_REPO})"
)

CONTRIBUTE_INFO = (
    f"Want to contribute to KGbot?\n"
    f"Contact the creator: [{TELEGRAM_USERNAME}](https://t.me/{TELEGRAM_USERNAME})\n"
    f"Creator GitHub: [Ayush Prem's GitHub]({AYUSH_PREM_REPO})\n"
    f"GitHub Repository: [KGbot on GitHub]({KGBOT_REPO})"
)

ABOUT_INFO = (
    "Hi! I'm KGbot, an AI chatbot.\n\n"
    "I'm here to chat with you, help manage your group, moderate users, and provide useful information.\n"
    "I can also create polls and assist with other tasks to make your group experience smoother."
)

async def creator(update: Update, context: CallbackContext):
    try:
        await update.message.reply_text(CREATOR_INFO, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text("Oops! Something went wrong. Please try again later.")

async def contribute(update: Update, context: CallbackContext):
    try:
        await update.message.reply_text(CONTRIBUTE_INFO, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text("Oops! Something went wrong. Please try again later.")

async def about(update: Update, context: CallbackContext):
    try:
        await update.message.reply_text(ABOUT_INFO, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text("Oops! Something went wrong. Please try again later.")