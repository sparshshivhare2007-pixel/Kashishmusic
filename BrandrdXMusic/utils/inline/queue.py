from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Assuming 'app' comes from your core client, make sure it's imported if needed by your structure
# from BrandrdXMusic import app 

def queue_markup(
    _,  # Added missing parameter name '_'
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    # Fixed text evaluation: changed text=["QU_B_1"] to text=_["QU_B_1"] to use localization string
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ]
    ]
    dur_list = [  # Renamed from 'dur' to avoid overwriting the 'dur' argument passed into the function
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur_list)
    return upl

def queue_back_markup(_, CPLAY):  # Added missing parameter name '_'
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    ]
    return upl

def aq_markup(_, chat_id):  # Added missing parameter name '_'
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|chat_id"), # Kept native code formatting
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|chat_id"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|chat_id"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|chat_id"),
        ],
        [   # Fixed: Removed the accidental double outer list wrapper [ [ InlineKeyboardButton(...) ] ]
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ]
    ]  # <-- FIX: Added the missing closing bracket for the list matrix
    return buttons

def queuemarkup(_, vidid, chat_id):
    # Added reference wrapper for app context global usage if applicable, or fallback placeholder
    try:
        from BrandrdXMusic import app
        username = app.username
    except Exception:
        username = "BrandrdXMusicBot" # Safe fallback string

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ᴘᴀᴜsᴇ",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(text="sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="sᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="ʀ...ᴜᴍ",
                callback_data=f"ADMIN Resume|{chat_id}"
            ),
            InlineKeyboardButton(
                text="ʀ...ʟᴀ",
                callback_data=f"ADMIN Replay|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="๏ ᴍᴏʀᴇ ๏",
                url="https://t.me/BRANDED_WORLD",
            ),
        ],
    ]
    return buttons
