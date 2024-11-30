import requests
from telegram import Update, MessageEntity
from telegram.ext import CallbackContext
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Fetch the Gemini API key from .env


async def handle_message(update: Update, context: CallbackContext):
    bot_username = context.bot.username  # Bot's username for detecting mentions

    # If it's a private chat, always respond
    if update.message.chat.type == "private":
        user_message = update.message.text
        bot_response = await get_gemini_response(user_message)
        await update.message.reply_text(bot_response)
        return

    # Check if the bot is mentioned in the message
    if update.message.entities:
        for entity in update.message.entities:
            if entity.type == MessageEntity.MENTION:
                mentioned_text = update.message.text[entity.offset:entity.offset + entity.length]
                if f"@{bot_username}" == mentioned_text:
                    # Remove the mention before sending the user message to the API
                    user_message = update.message.text.replace(mentioned_text, "").strip()
                    bot_response = await get_gemini_response(user_message)
                    await update.message.reply_text(bot_response)
                    return

    # Check if the bot is being replied to in the group
    if update.message.reply_to_message and update.message.reply_to_message.from_user.id == context.bot.id:
        user_message = update.message.text
        bot_response = await get_gemini_response(user_message)
        await update.message.reply_text(bot_response)
        return

    # If the bot isn't mentioned or replied to, ignore the message
    print("Bot not mentioned or replied to, ignoring message.")


async def get_gemini_response(user_message: str) -> str:
    """
    Send user input to the Gemini API and get a response with KG's personality.
    """
    headers = {
        'Content-Type': 'application/json',
    }

    # Add contextual instructions to reflect KG's personality
    prompt = (
        f"You are KG, a smart, witty, and helpful AI assistant with a warm and friendly tone. "
        f"You always respond as a supportive and approachable female character. "
        f"Keep your answers concise, 2-5 lines, and engaging. "
        f"Here is the user's input: {user_message}"
    )

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        # Send request to Gemini API
        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}",
            headers=headers,
            json=data
        )

        # Check for a successful response
        if response.status_code == 200:
            response_json = response.json()
            raw_response = response_json['candidates'][0]['content']['parts'][0]['text']

            # Trim the response to ensure it remains concise
            return trim_response(raw_response)
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return "Oops! Something went wrong with the AI. Please try again later."

    except Exception as e:
        print(f"Exception: {e}")
        return "Oops! Something went wrong with the AI. Please try again later."


def trim_response(response: str, max_lines: int = 5) -> str:
    """
    Trims the response to a maximum number of lines.
    """
    lines = response.strip().splitlines()
    if len(lines) > max_lines:
        return "\n".join(lines[:max_lines]) + "..."
    return response.strip()