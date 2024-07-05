from datetime import datetime
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from config import OWNER_ID as owner_id
from DAXXMUSIC import app



def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " in text_to_return:
        try:
            return msg.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@app.on_message(filters.command("bug"))
async def bugs(_, msg: Message):
    if msg.chat.username:
        chat_username = f"@{msg.chat.username}/`{msg.chat.id}`"
    else:
        chat_username = f"ᴩʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴩ/`{msg.chat.id}`"

    bugs = content(msg)
    user_id = msg.from_user.id
    mention = (
        "[" + msg.from_user.first_name + "](tg://user?id=" + str(msg.from_user.id) + ")"
    )
    datetimes_fmt = "%d-%m-%Y"
    datetimes = datetime.utcnow().strftime(datetimes_fmt)

    

    bug_report = f"""
**𝐁ᴜɢ : ** **tg://user?id={owner_id}**

**𝐑ᴇᴩᴏʀᴛᴇᴅ ʙʏ : ** **{mention}**
**𝐔sᴇʀ ɪᴅ : ** **{user_id}**
**𝐂ʜᴀᴛ : ** **{chat_username}**

**𝐁ᴜɢ : ** **{bugs}**

**𝐄ᴠᴇɴᴛ 𝐒ᴛᴀᴍᴩ : ** **{datetimes}**
**𝐏ᴏᴡᴇʀᴇᴅ  𝐁ʏ :** || [𝐁ʀᴏᴋᴇɴ 𝐗 𝐍ᴇᴛᴡᴏʀᴋ](https://t.me/brokenxnetwork) ☠️||"""

    if msg.chat.type == "private":
        await msg.reply_text("<b>» ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴩs.</b>")
        return

    if user_id == owner_id:
        if bugs:
            await msg.reply_text(
                "<b>» ᴀʀᴇ ʏᴏᴜ ᴄᴏᴍᴇᴅʏ ᴍᴇ 🤣, ʏᴏᴜ'ʀᴇ ᴛʜᴇ ᴏᴡɴᴇʀ ᴏғ ᴛʜᴇ ʙᴏᴛ.</b>",
            )
            return
        else:
            await msg.reply_text("ᴄʜᴜᴍᴛɪʏᴀ ᴏᴡɴᴇʀ!")
    elif user_id != owner_id:
        if bugs:
            await msg.reply_text(
                f"<b>ʙᴜɢ ʀᴇᴩᴏʀᴛ : {bugs}</b>\n\n"
                "<b>» ʙᴜɢ sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇᴩᴏʀᴛᴇᴅ ᴀᴛ sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ !</b>",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("⌯ ᴄʟᴏsᴇ ⌯", callback_data="close_data")]]
                ),
            )
            await app.send_photo(
                -1002094142057,
                photo="https://telegra.ph/file/91c6683a0074d9dce03c1.jpg",
                caption=f"{bug_report}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("⌯ ᴠɪᴇᴡ ʙᴜɢ ⌯", url=f"{msg.link}")],
                        [
                            InlineKeyboardButton(
                                "⌯ ᴄʟᴏsᴇ ⌯", callback_data="close_send_photo"
                            )
                        ],
                    ]
                ),
            )
        else:
            await msg.reply_text(
                f"<b>» ɴᴏ ʙᴜɢ ᴛᴏ ʀᴇᴩᴏʀᴛ !</b>",
            )




@app.on_callback_query(filters.regex("close_send_photo"))
async def close_send_photo(_,  query :CallbackQuery):
    is_admin = await app.get_chat_member(query.message.chat.id, query.from_user.id)
    if not is_admin.privileges.can_delete_messages:
        await query.answer("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʀɪɢʜᴛs ᴛᴏ ᴄʟᴏsᴇ ᴛʜɪs.", show_alert=True)
    else:
        await query.message.delete()


