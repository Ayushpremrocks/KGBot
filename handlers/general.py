from telegram import Update
from telegram.ext import CallbackContext

AYUSH_PREM_REPO = "https://github.com/Ayushpremrocks"
KGBOT_REPO = "https://github.com/Ayushpremrocks/KGBot"

async def creator(update: Update, context: CallbackContext):
    await update.message.reply_text(
        f"Created by [@ayushpremrocks](https://t.me/ayushpremrocks)\n"
        f"GitHub: [Ayush Prem's GitHub]({AYUSH_PREM_REPO})",
        parse_mode="Markdown"
    )

async def contribute(update: Update, context: CallbackContext):
    await update.message.reply_text(
        f"Want to contribute to KGbot?\n"
        f"Contact the creator: [@ayushpremrocks](https://t.me/ayushpremrocks)\n"
        f"Creator GitHub: [Ayush Prem's GitHub]({AYUSH_PREM_REPO})\n"
        f"GitHub Repository: [KGbot on GitHub]({KGBOT_REPO})",
        parse_mode="Markdown"
    )

async def about(update: Update, context: CallbackContext):
    await update.message.reply_text(
        f"Hi! I'm KGbot, an AI chatbot.\n\n"
        f"I'm here to chat with you, help manage your group, moderate users, and provide useful information.\n"
        f"I can also create polls and assist with other tasks to make your group experience smoother.",
        parse_mode="Markdown"
    )