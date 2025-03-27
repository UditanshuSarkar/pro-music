from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("● CʜᴀᴛGPT ●", callback_data="mplus HELP_ChatGPT"),
         InlineKeyboardButton("● ǫᴜᴏᴛʟʏ ●", callback_data="mplus HELP_Q"),
         InlineKeyboardButton("● sᴛɪᴄᴋᴇʀs ●", callback_data="mplus HELP_Sticker")],

        [InlineKeyboardButton("● Tᴀɢ-Aʟʟ ●", callback_data="mplus HELP_TagAll"),
         InlineKeyboardButton("● 𝖦ɪᴛʜᴜʙ ●", callback_data="mplus HELP_Github"),
         InlineKeyboardButton("● Exᴛʀᴀ ●", callback_data="mplus HELP_Extra")],

        [InlineKeyboardButton("● Aᴄᴛɪᴏɴ ●", callback_data="mplus HELP_Action"),
         InlineKeyboardButton("● Sᴇᴀʀᴄʜ ●", callback_data="mplus HELP_Search"),
         InlineKeyboardButton("● Gᴀᴍᴇs ●", callback_data="mplus HELP_Games")],    

        [InlineKeyboardButton("● ғᴏɴᴛ ●", callback_data="mplus HELP_Font"),
         InlineKeyboardButton("● ᴄᴏᴜᴘʟᴇs ●", callback_data="mplus HELP_Couples"),
         InlineKeyboardButton("● Ⓣ-ɢʀᴀᴘʜ ●", callback_data="mplus HELP_TG")],          

        [InlineKeyboardButton("● Rᴇᴀᴄᴛɪᴏɴ ●", callback_data="mplus HELP_Reaction"),
         InlineKeyboardButton("● Dᴇᴠᴇʟᴏᴘᴇʀ ●", callback_data="mplus HELP_Developer"),
         InlineKeyboardButton("● Rᴇϙᴜᴇsᴛ ●", callback_data="mplus HELP_Request")],

        [InlineKeyboardButton("<", callback_data="settings_back_helper"), 
         InlineKeyboardButton(">", callback_data="managebot123 settings_back_helper")]
              ]
