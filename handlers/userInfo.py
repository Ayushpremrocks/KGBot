from telegram import Update
from telegram.ext import CallbackContext

async def get_group_info(update: Update, context: CallbackContext):
    chat = update.message.chat

    try:
        member_count = await context.bot.get_chat_member_count(chat.id)
        group_info = (
            f"Group Name: {chat.title}\n"
            f"Group ID: {chat.id}\n"
            f"Total Members: {member_count}\n"
        )
    except Exception as e:
        group_info = "Unable to fetch group details. Please try again later."
        print(f"Error fetching group info: {e}")

    await update.message.reply_text(group_info)

async def get_my_info(update: Update, context: CallbackContext):
    user = update.message.from_user
    user_info = (
        f"Name: {user.full_name}\n"
        f"Username: @{user.username}\n"
        f"User ID: {user.id}\n"
    )
    await update.message.reply_text(user_info)

async def get_user_info(update: Update, context: CallbackContext):
    target_user = None

    try:
        if update.message.reply_to_message:
            target_user = update.message.reply_to_message.from_user
        elif context.args:
            username = context.args[0].lstrip('@')
            chat = update.effective_chat

            try:
                member = await chat.get_member(username)
                target_user = member.user if member else None
            except Exception as e:
                print(f"Direct username lookup failed: {e}")

                print("Performing case-insensitive member search...")
                admins = await chat.get_administrators()
                for member in admins:
                    if member.user.username and member.user.username.lower() == username.lower():
                        target_user = member.user
                        break

                if not target_user:
                    async for member in chat.get_members():
                        if member.user.username and member.user.username.lower() == username.lower():
                            target_user = member.user
                            break

        if not target_user:
            await update.message.reply_text("User not found. Please reply to their message or provide a valid username.")
            return

        user_info = (
            f"Name: {target_user.full_name}\n"
            f"Username: @{target_user.username}\n"
            f"User ID: {target_user.id}\n"
        )
        await update.message.reply_text(user_info)

    except Exception as e:
        await update.message.reply_text("An error occurred while fetching user info.")
        print(f"Error in get_user_info: {e}")