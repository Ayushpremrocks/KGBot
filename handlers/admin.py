from telegram import Update
from telegram.ext import CallbackContext


async def pin_message(update: Update, context: CallbackContext):
    if not update.message.reply_to_message:
        await update.message.reply_text("Reply to a message to pin it.")
        return

    try:
        await update.message.reply_to_message.pin(disable_notification=True)  # Optionally disable notifications
        await update.message.reply_text("Message pinned successfully!")
    except Exception as e:
        await update.message.reply_text(f"Failed to pin the message: {e}")


async def delete_message(update: Update, context: CallbackContext):
    if not update.message.reply_to_message:
        await update.message.reply_text("Reply to a message to delete it.")
        return

    try:
        await update.message.reply_to_message.delete()
        await update.message.reply_text("Message deleted successfully!")
    except Exception as e:
        await update.message.reply_text(f"Failed to delete the message: {e}")


from telegram import Update
from telegram.ext import CallbackContext

async def kick_user(update: Update, context: CallbackContext):
    if not update.message.reply_to_message or not update.message.reply_to_message.from_user:
        await update.message.reply_text("Reply to a user's message to kick them.")
        return

    user_id = update.message.reply_to_message.from_user.id

    # Check if the bot has the necessary permissions
    chat_member = await update.effective_chat.get_member(context.bot.id)
    if chat_member.status not in ["administrator", "member"]:
        await update.message.reply_text("Bot does not have permission to kick members.")
        return

    # Get a list of admins to check if the user is an admin
    admins = await update.effective_chat.get_administrators()
    admin_ids = [admin.user.id for admin in admins]

    if user_id in admin_ids:
        await update.message.reply_text("You can't kick an admin!")
        return

    try:
        # Kick the user by using the `kick_member` method from `Chat` object
        await update.effective_chat.kick_member(user_id)

        # Send confirmation message
        await update.message.reply_text("User kicked successfully!")
    except Exception as e:
        # Handle any errors that occur
        await update.message.reply_text(f"Failed to kick the user: {e}")


async def ban_user(update: Update, context: CallbackContext):
    if not update.message.reply_to_message or not update.message.reply_to_message.from_user:
        await update.message.reply_text("Reply to a user's message to ban them.")
        return

    try:
        user_id = update.message.reply_to_message.from_user.id
        await update.effective_chat.ban_member(user_id)
        await update.message.reply_text("User banned successfully!")
    except Exception as e:
        await update.message.reply_text(f"Failed to ban the user: {e}")


async def promote_user(update: Update, context: CallbackContext):
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        try:
            await context.bot.promote_chat_member(
                chat_id=update.message.chat_id,
                user_id=user_id,
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_promote_members=True
            )
            await update.message.reply_text(f"Promoted {update.message.reply_to_message.from_user.full_name}")
        except Exception as e:
            await update.message.reply_text("Failed to promote user.")

async def demote_user(update: Update, context: CallbackContext):
    if not update.message.reply_to_message:
        await update.message.reply_text("Reply to a user's message to demote them.")
        return

    user_id = update.message.reply_to_message.from_user.id
    try:
        await context.bot.promote_chat_member(
            chat_id=update.message.chat_id,
            user_id=user_id,
            is_anonymous=False,
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_promote_members=False
        )
        await update.message.reply_text(f"Demoted {update.message.reply_to_message.from_user.full_name}")
    except Exception as e:
        await update.message.reply_text(f"Failed to demote user: {e}")

async def get_admins(update: Update, context: CallbackContext):
    try:
        admins = await context.bot.get_chat_administrators(update.message.chat_id)
        admin_list = "\n".join([f"- {admin.user.full_name}" for admin in admins if not admin.user.is_bot])
        if not admin_list:
            await update.message.reply_text("No admins found (except bots).")
        else:
            await update.message.reply_text(f"Admins in this group:\n{admin_list}")
    except Exception as e:
        await update.message.reply_text(f"Failed to fetch admin list: {e}")
