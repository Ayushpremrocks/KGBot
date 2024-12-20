# KGBot - An AI-powered assistant for group management, moderation, and fun conversations
 
## Bot Telegram Username: [@hbd_kg_bot](https://t.me/hbd_kg_bot)

KGbot is a Telegram bot designed to provide various functionalities such as group management, user moderation, and even AI-based conversational abilities using Google's Gemini API. It's built with Python and utilizes the `python-telegram-bot` library for interacting with the Telegram API.

---

## Features
- **AI-powered Chat**:
  - The bot responds to messages in private chats or when mentioned in group chats using AI responses powered by Google's Gemini API.

- **General Commands**:
  - `/creator`: Know about the creator of this bot.
  - `/contribute`: Information on how to contribute to this bot.
  - `/about`: Learn more about the bot.

- **Admin Commands**:
  - `/pin`: Pin a message in the group.
  - `/delete`: Delete a message from the group.
  - `/kick`: Kick a user from the group.
  - `/ban`: Ban a user from the group.
  - `/promote`: Promote a user to admin.
  - `/demote`: Demote a user from admin.
  - `/admins`: View the list of admins in the group.

- **User Information Commands**:
  - `/groupinfo`: Get group details.
  - `/myinfo`: Get your user information.
  - `/userinfo [username]`: Get information about a specific user.

- **Moderation Commands**:
  - `/warn [username]`: Warn a user.
  - `/warnings [username]`: View the number of warnings a user has.
  - `/clearwarnings [username]`: Clear all warnings for a user.
  - `/mute [username]`: Mute a user.
  - `/unmute [username]`: Unmute a user.

- **Poll Creation**:
  - `/poll [question] [option1, option2, option3,...]`: Create a poll with a question and options.

- **Group Event Handlers**:
  - Welcomes new members.
  - Notifies when a member leaves.
    
---

## Requirements

- Python 3.8 or higher
- `python-telegram-bot` library
- `requests` library
- A `.env` file with the following keys:
  - `TELEGRAM_TOKEN`: Your Telegram Bot API token.
  - `GEMINI_API_KEY`: Your Gemini API key for AI responses.
 
---

## Tech Stack

- **Programming Language**: Python
  
- **Bot Framework**: 
  - [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - A Python library for building Telegram bots.

- **AI Integration**: 
  - [Google Gemini API](https://ai.google.dev/gemini-api/docs/api-key) - Provides AI-powered conversational abilities for the bot.

- **Environment Management**: 
  - [Virtualenv](https://virtualenv.pypa.io/en/latest/) - Used for creating isolated Python environments.
  - [dotenv](https://pypi.org/project/python-dotenv/) - Loads environment variables from a `.env` file to securely store sensitive data like API keys.

- **Libraries**: 
  - [requests](https://pypi.org/project/requests/) - A simple library for making HTTP requests, used for interacting with the Gemini API.

- **Deployment**: 
  - [Heroku](https://www.heroku.com/) or **VPS** - Cloud platforms for deploying and hosting the bot.
  
- **Version Control**: 
  - [Git](https://git-scm.com/) & [GitHub](https://github.com/) - Version control and collaboration platform for the source code.
  
- **Logging**: 
  - Python's built-in [logging](https://docs.python.org/3/library/logging.html) module for error tracking and activity monitoring.


---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/KGbot.git
   cd KGbot
   ```
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
3. Activate the virtual environent:
   - On windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Create a .env file in the project root directory and add your keys:
   ```bash
   TELEGRAM_TOKEN=your_telegram_bot_token
   GEMINI_API_KEY=your_gemini_api_key
   ```
6. Run the bot:
   ```bash
   python main.py
   ```
---

## Contributing

We welcome contributions to improve the bot! To contribute:

1. Fork the repository by clicking the "Fork" button at the top right of the page.
2. Clone your fork to your local machine:

   ```bash
   git clone https://github.com/your-username/KGbot.git
   ```
3. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
4. Make your changes and commit them:
   ```bash
   git commit -am 'Add new feature or fix bug'
   ```
5. Push your changes to your forked repository:
   ```bash
   git push origin feature-name
   ```
6. Open a pull request (PR) with a detailed description of the changes.

---
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.