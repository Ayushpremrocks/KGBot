from telegram import Update
from telegram.ext import CallbackContext

async def pin_message(update: Update, context: CallbackContext):
    if not update.effective_chat or update.effective_chat.type not in ['group', 'supergroup']:
        await update.message.reply_text("This command can only be used in groups.")
        return

    try:
        chat_member = await context.bot.get_chat_member(update.effective_chat.id, update.effective_user.id)
        if chat_member.status not in ['administrator', 'creator']:
            await update.message.reply_text("You must be an admin to pin messages.")
            return
    except Exception as e:
        await update.message.reply_text(f"Error checking admin status: {e}")
        return

    if not update.message.reply_to_message:
        await update.message.reply_text("Reply to a message to pin it.")
        return

    try:
        await update.message.reply_to_message.pin(disable_notification=True)
        await update.message.reply_text("Message pinned successfully!")
    except Exception as e:
        await update.message.reply_text(f"Failed to pin the message: {e}")

async def delete_message(update: Update, context: CallbackContext):
    if not update.effective_chat or update.effective_chat.type not in ['group', 'supergroup']:
        await update.message.reply_text("This command can only be used in groups.")
        return

    try:
        chat_member = await context.bot.get_chat_member(update.effective_chat.id, update.effective_user.id)
        if chat_member.status not in ['administrator', 'creator']:
            await update.message.reply_text("You must be an admin to delete messages.")
            return
    except Exception as e:
        await update.message.reply_text(f"Error checking admin status: {e}")
        return

    if not update.message.reply_to_message:
        await update.message.reply_text("Reply to a message to delete it.")
        return

    try:
        await update.message.reply_to_message.delete()
        await update.message.reply_text("Message deleted successfully!")
    except Exception as e:
        await update.message.reply_text(f"Failed to delete the message: {e}")

async def kick_user(update: Update, context: CallbackContext):
    if not update.effective_chat or update.effective_chat.type not in ['group', 'supergroup']:
        await update.message.reply_text("This command can only be used in groups.")
        return

    if not update.message.reply_to_message or not update.message.reply_to_message.from_user:
        await update.message.reply_text("Reply to a user's message to kick them.")
        return

    user_to_kick = update.message.reply_to_message.from_user
    
    try:
        chat_member = await context.bot.get_chat_member(update.effective_chat.id, update.effective_user.id)
        if not (chat_member.status in ['administrator', 'creator']):
            await update.message.reply_text("You must be an admin to kick users.")
            return
    except Exception as e:
        await update.message.reply_text(f"Error checking admin status: {e}")
        return

    try:
        await context.bot.ban_chat_member(
            chat_id=update.effective_chat.id, 
            user_id=user_to_kick.id, 
            revoke_messages=False
        )
        await update.message.reply_text(f"User {user_to_kick.full_name} kicked successfully!")
    except Exception as e:
        await update.message.reply_text(f"Failed to kick the user: {e}")
        return

async def ban_user(update: Update, context: CallbackContext):
    if not update.effective_chat or update.effective_chat.type not in ['group', 'supergroup']:
        await update.message.reply_text("This command can only be used in groups.")
        return

    try:
        chat_member = await context.bot.get_chat_member(update.effective_chat.id, update.effective_user.id)
        if chat_member.status not in ['administrator', 'creator']:
            await update.message.reply_text("You must be an admin to ban users.")
            return
    except Exception as e:
        await update.message.reply_text(f"Error checking admin status: {e}")
        return

    if not update.message.reply_to_message or not update.message.reply_to_message.from_user:
        await update.message.reply_text("Reply to a user's message to ban them.")
        return

    try:
        user_id = update.message.reply_to_message.from_user.id
        await context.bot.ban_chat_member(
            chat_id=update.effective_chat.id,
            user_id=user_id
        )
        await update.message.reply_text("User banned successfully!")
    except Exception as e:
        await update.message.reply_text(f"Failed to ban the user: {e}")

async def promote_user(update: Update, context: CallbackContext):
    if not update.effective_chat or update.effective_chat.type not in ['group', 'supergroup']:
        await update.message.reply_text("This command can only be used in groups.")
        return

    try:
        chat_member = await context.bot.get_chat_member(update.effective_chat.id, update.effective_user.id)
        if chat_member.status not in ['administrator', 'creator']:
            await update.message.reply_text("You must be an admin to promote users.")
            return
    except Exception as e:
        await update.message.reply_text(f"Error checking admin status: {e}")
        return

    if not update.message.reply_to_message:
        await update.message.reply_text("Reply to a user's message to promote them.")
        return

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
        await update.message.reply_text(f"Failed to promote user: {e}")

async def demote_user(update: Update, context: CallbackContext):
    if not update.effective_chat or update.effective_chat.type not in ['group', 'supergroup']:
        await update.message.reply_text("This command can only be used in groups.")
        return

    try:
        chat_member = await context.bot.get_chat_member(update.effective_chat.id, update.effective_user.id)
        if chat_member.status not in ['administrator', 'creator']:
            await update.message.reply_text("You must be an admin to demote users.")
            return
    except Exception as e:
        await update.message.reply_text(f"Error checking admin status: {e}")
        return

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
    if not update.effective_chat or update.effective_chat.type not in ['group', 'supergroup']:
        await update.message.reply_text("This command can only be used in groups.")
        return

    try:
        admins = await context.bot.get_chat_administrators(update.message.chat_id)
        admin_list = "\n".join([f"- {admin.user.full_name}" for admin in admins if not admin.user.is_bot])
        if not admin_list:
            await update.message.reply_text("No admins found (except bots).")
        else:
            await update.message.reply_text(f"Admins in this group:\n{admin_list}")
    except Exception as e:
        await update.message.reply_text(f"Failed to fetch admin list: {e}")
